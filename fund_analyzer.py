# fund_analyzer.py
import pandas as pd
from datetime import datetime
import numpy as np
import math

class FundPerformanceAnalyzer:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe.copy()
        self._compute_days_since_inception()
        self._analyze_sharpe_ratios()
        self.believable_df = self.get_believable_df()

    #def _compute_days_since_inception(self):
    #    def calculate_days(date_str):
    #        try:
    #            inception_date = datetime.strptime(date_str, '%B %d, %Y')
    #            return (datetime.today() - inception_date).days
    #        except:
    #            return None
    #    self.df['days_since_inception'] = self.df['inception_date'].apply(calculate_days)

    def _compute_days_since_inception(self):
        """
        Computes the number of business days since the inception date for each entry in the DataFrame.
        """
        def calculate_business_days(date_str):
            try:
                # Parse the inception date string to a datetime object
                inception_date = datetime.strptime(date_str, '%B %d, %Y').date()
                today = datetime.today().date()
                
                # Convert dates to numpy datetime64[D] format
                inception_np = np.datetime64(inception_date)
                today_np = np.datetime64(today)
                
                # Calculate business days using numpy.busday_count
                business_days = np.busday_count(inception_np, today_np)
                
                return int(business_days)
            except Exception as e:
                # Optionally, log the exception e for debugging
                return None

        # Apply the calculate_business_days function to the 'inception_date' column
        self.df['days_since_inception'] = self.df['inception_date'].apply(calculate_business_days)

    def _compute_confidence_interval(self, sharpe, days, confidence=1.96):
        if pd.isnull(sharpe) or pd.isnull(days) or days == 0:
            return (None, None)
        try:
            se = math.sqrt((1 + (sharpe**2)/2) / days)
            lower = sharpe - confidence * se
            upper = sharpe + confidence * se
            return (lower, upper)
        except:
            return (None, None)

    def _analyze_sharpe_ratios(self):
        confidence_level = 1.96
        ci = self.df.apply(
            lambda row: self._compute_confidence_interval(row['sharpe_ratio'], row['days_since_inception'], confidence_level) 
            if not pd.isnull(row['sharpe_ratio']) else (None, None), axis=1
        )
        self.df[['sharpe_confidence_lower', 'sharpe_confidence_upper']] = pd.DataFrame(ci.tolist(), index=self.df.index)
        
        def flag_sharpe(row):
            lower, upper = row['sharpe_confidence_lower'], row['sharpe_confidence_upper']
            if lower is None or upper is None:
                return 'Insufficient Data'
            if lower > 0:
                return 'Believable'
            elif upper < 0:
                return 'Not Believable'
            else:
                return 'Marginal'
        
        self.df['sharpe_flag'] = self.df.apply(flag_sharpe, axis=1)

    def get_believable_df(self):
        return self.df[self.df['sharpe_flag'] == 'Believable']

    def rank_portfolio_managers(self):
        df = self.believable_df
        ranked = df.groupby('portfolio_managers').agg({
            'sharpe_ratio': 'mean',
            'apr': 'mean'
        }).reset_index()
        ranked = ranked.sort_values(['sharpe_ratio', 'apr'], ascending=[False, False])
        return ranked

    def rank_fund_names(self):
        df = self.believable_df
        ranked = df.groupby(['fund_name', 'fund_code', 'asset_class']).agg({
            'sharpe_ratio': 'mean',
            'apr': 'mean'
        }).reset_index()
        ranked = ranked.sort_values(['sharpe_ratio', 'apr'], ascending=[False, False])
        return ranked

    def rank_asset_classes(self):
        df = self.believable_df
        ranked = df.groupby('asset_class').agg({
            'sharpe_ratio': 'mean',
            'apr': 'mean'
        }).reset_index()
        ranked = ranked.sort_values(['sharpe_ratio', 'apr'], ascending=[False, False])
        return ranked

    def summary_statistics_md(self):
        df = self.believable_df
        stats = df[['sharpe_ratio', 'apr']].describe().loc[['mean', '50%', 'std']]
        stats.rename(index={'50%': 'median'}, inplace=True)
        return stats.round(2).to_markdown()

    def sharpe_apr_correlation_md(self):
        df = self.believable_df
        correlation = df['sharpe_ratio'].corr(df['apr'])
        return f"**Correlation between Sharpe Ratio and APR:** {correlation:.2f}"

    def get_top_funds_md(self, metric='sharpe_ratio', top_n=3):
        df = self.believable_df
        grouped = df.groupby(['fund_name', 'fund_code', 'asset_class']).agg({
            metric: 'mean',
            'apr': 'mean'
        }).reset_index()
        
        top_funds = grouped.sort_values(metric, ascending=False).head(top_n)
        return top_funds[['fund_name', 'fund_code', 'asset_class', metric, 'apr']].to_markdown(index=False)

    def get_bottom_funds_md(self, metric='sharpe_ratio', top_n=3):
        df = self.believable_df
        grouped = df.groupby(['fund_name', 'fund_code', 'asset_class']).agg({
            metric: 'mean',
            'apr': 'mean'
        }).reset_index()
        
        bottom_funds = grouped.sort_values(metric, ascending=True).head(top_n)
        return bottom_funds[['fund_name', 'fund_code', 'asset_class', metric, 'apr']].to_markdown(index=False)

    def get_average_metrics_md(self, category='portfolio_managers'):
        df = self.believable_df
        avg_metrics = df.groupby(category)[['sharpe_ratio', 'apr']].mean().sort_values('sharpe_ratio', ascending=False)
        return avg_metrics.round(4).to_markdown()
