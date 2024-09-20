from fund_crawler import FundCrawler
from fund_analyzer import FundPerformanceAnalyzer
import pandas as pd 
import re
import os

def main():
    base_url = 'https://performance.pictonmahoney.com/funds/en-US/'
    all_results = []
    crawler = FundCrawler()
    for fund in funds_dict:
        for fund_class in funds_dict[fund]:
            url = base_url + fund_class
            print(f"Crawling URL: {url}")  # Optionally, replace with logging
            result = crawler.extract_fund_data(url)
            if result:
                all_results.extend(result)

    if not all_results:
        print("No data extracted. Exiting.")
        return

    df  = pd.DataFrame(all_results)
    df = df.explode('portfolio_managers')
    analyzer = FundPerformanceAnalyzer(df)
    analytics_md = generate_analytics_markdown(analyzer)
    update_readme(analytics_md)

def generate_analytics_markdown(analyzer: FundPerformanceAnalyzer) -> str:
    summary_stats = analyzer.summary_statistics_md()
    correlation = analyzer.sharpe_apr_correlation_md()
    top_funds_sharpe = analyzer.get_top_funds_md(metric='sharpe_ratio', top_n=3)
    bottom_funds_sharpe = analyzer.get_bottom_funds_md(metric='sharpe_ratio', top_n=3)
    top_funds_apr = analyzer.get_top_funds_md(metric='apr', top_n=3)
    bottom_funds_apr = analyzer.get_bottom_funds_md(metric='apr', top_n=3)
    avg_pm = analyzer.get_average_metrics_md(category='portfolio_managers')
    avg_funds = analyzer.get_average_metrics_md(category='fund_name')
    avg_assets = analyzer.get_average_metrics_md(category='asset_class')

    analytics_md = f"""

### Summary Statistics
### Correlation
{correlation}

### Top 3 Funds by Sharpe Ratio
{top_funds_sharpe}

### Bottom 3 Funds by Sharpe Ratio
{bottom_funds_sharpe}

### Top 3 Funds by APR
{top_funds_apr}

### Bottom 3 Funds by APR
{bottom_funds_apr}

### Average Metrics by Category
#### Portfolio Managers
{avg_pm}

#### Fund Names
{avg_funds}

#### Asset Classes
{avg_assets}

"""
    return analytics_md

def update_readme(analytics_md: str):
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("README.md not found. Creating a new one.")
        with open(readme_path, "w") as f:
            f.write("# Fund Performance Analytics\n\n<!-- ANALYTICS -->\n<!-- END ANALYTICS -->\n")
    
    with open(readme_path, "r") as file:
        readme_content = file.read()

    pattern = r'<!-- ANALYTICS -->.*<!-- END ANALYTICS -->'
    new_analytics_section = f'<!-- ANALYTICS -->\n{analytics_md}\n<!-- END ANALYTICS -->'
    new_readme = re.sub(
        pattern,
        new_analytics_section,
        readme_content,
        flags=re.DOTALL
    )
    
    with open(readme_path, "w") as file:
        file.write(new_readme)
    
    print("README.md updated successfully.")

# Define funds_dict here or import it if defined elsewhere
funds_dict = {
    'PM Fortified Market Neutral Fund': ['PMFMA', 'PMFMF', 'PFMN', 'PMFMFT'],
    'PM Fortified Equity Fund' : ['PFEQA', 'PFEQF', 'PFEQFT', 'PFEQT'],
    'PM Fortified Long Short Equity Fund' : ['PMFLA', 'PMFLF', 'PFLS'],
    'PM Long Short Equity Fund': ['PMLSEA', 'PMLSEF'],
    'PM 130/30 Alpha Extension Fund': ['PMAEI'],
    'PM Fortified Active Extension Fund': ['PMFAA', 'PMFAF', 'PFAE'],
    'PM Fortified Income Alernative Fund': ['PMFIA', 'PMFIF', 'PFIA'],
    'PM Fortified Income Fund' : ['PFINCA', 'PFINCF', 'PFINCFT', 'PFINCT'],
    'PM Income Opportunities Fund': ['PMIOA', 'PMIOF'],
    'PM Fortified Special Situations Alternative Fund': ['PMSAA', 'PMSAF', 'PFSS'],
    'PM Special Situations Fund': ['PMSSA', 'PMSSF'],
    'PM Arbitrage Fund': ['PMAFF', 'PMAFB', 'PMAFV'],
    'PM Arbitrage Plus Fund': ['PMAPA', 'PMAPF', 'PMAPV'],
    'PM Fortified Arbitrage Alternative Fund': ['PFAAA', 'PFAAF'],
    'PM Absolute Alpha Fund': ['PMAAA', 'PMAAF'],
    'PM Fortified Alpha Alternative Fund': ['PFALA', 'PFALF', 'PFALE', 'PFALFT'],
    'PM Fortified Inflation Opportunities Alternative Fund': ['PLIOA', 'PLIOF'],
    'PM Fortified Multi-Asset Fund': ['PFMAA', 'PFMAF', 'PFMAFT', 'PFMAT'],
    'PM Fortified Multi-Strategy Alternative Fund': ['PMFSA', 'PMFSF', 'PFMS', 'PMFSFT'],
    'PM Fortified Core Bond Fund': ['PFCBA', 'PFCBF', 'PFCBE'] 
}

if __name__ == '__main__':
    main()