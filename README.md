# Picton Mahoney Fund Analytics

![Fund Performance](https://img.shields.io/badge/Status-Active-green)
![Python](https://img.shields.io/badge/Python-3.9-blue)
![License](https://img.shields.io/badge/License-MIT-blue)


## Introduction

This repository analyzes the fund performance for Picton Mahoney Asset Management listed on their [PMAM Performance and Returns](https://picton-mahoney-mutual-fund-profiles-master.picton-mahoney-staging.transmissionmedia.ca/funds/en-US/?searchTerm=) site. The analysis provides key performance metrics, evaluates the reliability of these metrics, and presents the findings in an easily accessible format.

## Core Steps

1. **Scraping**:
    - **Objective**: Extract comprehensive fund data from the PMAM Performance and Returns website.
    - **Process**:
        - Utilize web scraping techniques to navigate and retrieve relevant fund information.
        - Implement the `FundCrawler` class, leveraging the `crawl4ai` library, to automate data extraction.
        - Ensure accurate parsing of fund attributes such as Fund Name, APR, Sharpe Ratio, Max Drawdown, Inception Date, Asset Class, and Portfolio Managers.
    - **Tools**: Python's `requests`, `BeautifulSoup`, and `crawl4ai` libraries.

2. **Analysis**:
    - **Objective**: Compute essential performance metrics and assess their reliability.
    - **Process**:
        - Use the extracted data to calculate key performance indicators, including Sharpe Ratios and Annual Percentage Rates (APR).
        - Apply statistical methods to determine the confidence intervals for Sharpe Ratios, evaluating their believability and significance.
        - Filter and categorize funds based on the reliability of their Sharpe Ratios to ensure meaningful analysis.
    - **Tools**: Python's `pandas`, `math`, and statistical libraries.

3. **Update**:
    - **Objective**: Automate the presentation of analytics by updating the `README.md` file.
    - **Process**:
        - Generate Markdown-formatted analytics based on the computed metrics.
        - Insert the latest analytics into the designated section of the `README.md` file, ensuring seamless integration.
        - Utilize GitHub Actions to schedule daily updates, maintaining up-to-date analytics without manual intervention.
    - **Tools**: Python scripting, GitHub Actions for automation.

## Confidence Interval for Sharpe Ratio

### Overview

The Sharpe Ratio is a widely used metric to evaluate the risk-adjusted return of an investment. However, its reliability can be influenced by the sample size and variability in returns. To assess the believability of the Sharpe Ratio, this analysis employs confidence intervals.

### Approach

1. **Calculation of Confidence Interval**:
    - **Standard Error (SE)**: 
        \[
        SE = \sqrt{\frac{1 + \frac{Sharpe^2}{2}}{Days}}
        \]
        - *Where*:
            - *Sharpe*: The computed Sharpe Ratio.
            - *Days*: Number of days the fund has been active.
    - **Confidence Interval (CI)**:
        \[
        CI = Sharpe \pm (z \times SE)
        \]
        - *Where*:
            - *z*: Z-score corresponding to the desired confidence level (1.96 for 95% confidence).

2. **Interpretation**:
    - **Believable Sharpe Ratio**: If the lower bound of the CI > 0, indicating statistically significant positive performance.
    - **Not Believable Sharpe Ratio**: If the upper bound of the CI < 0, indicating negative performance.
    - **Marginal**: If the CI includes zero, suggesting uncertainty in the Sharpe Ratio's reliability.

### Significance

By computing the confidence intervals, the analysis ensures that only statistically reliable Sharpe Ratios are considered in performance evaluations, thereby enhancing the credibility of the insights derived.





<!-- ANALYTICS -->

## Daily Fund Performance Analytics

### Summary Statistics
### Correlation
**Correlation between Sharpe Ratio and APR:** 0.49

### Top 3 Funds by Sharpe Ratio
| fund_name                                             | fund_code   | asset_class          |   sharpe_ratio |   apr |
|:------------------------------------------------------|:------------|:---------------------|---------------:|------:|
| Picton Mahoney Fortified Alpha Alternative Fund — ETF | PFAA        | Multi-Asset Strategy |           1.62 |  7.54 |
| Picton Mahoney Fortified Alpha Alternative Fund — F   | PIC 3351    | Multi-Asset Strategy |           1.61 |  7.17 |
| Picton Mahoney Fortified Alpha Alternative Fund — FT  | PIC 3353    | Multi-Asset Strategy |           1.6  |  7.15 |

### Bottom 3 Funds by Sharpe Ratio
| fund_name                                                          | fund_code   | asset_class       |   sharpe_ratio |   apr |
|:-------------------------------------------------------------------|:------------|:------------------|---------------:|------:|
| Picton Mahoney Fortified Special Situations Alternative Fund — F   | PIC 3551    | Credit            |           0.12 |  3.48 |
| Picton Mahoney Fortified Special Situations Alternative Fund — ETF | PFSS        | Credit            |           0.12 |  3.49 |
| Picton Mahoney Fortified Core Bond Fund — A                        | PIC 8520    | Core Fixed Income |           0.23 |  6.99 |

### Top 3 Funds by APR
| fund_name                                                        | fund_code   | asset_class   |   apr |   apr |
|:-----------------------------------------------------------------|:------------|:--------------|------:|------:|
| Picton Mahoney Fortified Long Short Alternative Fund — F         | PIC 3201    | Equity        | 14.87 | 14.87 |
| Picton Mahoney Fortified Long Short Alternative Fund — ETF       | PFLS        | Equity        | 14.69 | 14.69 |
| Picton Mahoney Fortified Active Extension Alternative Fund — ETF | PFAE        | Equity        | 13.99 | 13.99 |

### Bottom 3 Funds by APR
| fund_name                                                          | fund_code   | asset_class   |   apr |   apr |
|:-------------------------------------------------------------------|:------------|:--------------|------:|------:|
| Picton Mahoney Fortified Special Situations Alternative Fund — F   | PIC 3551    | Credit        |  3.48 |  3.48 |
| Picton Mahoney Fortified Special Situations Alternative Fund — ETF | PFSS        | Credit        |  3.49 |  3.49 |
| Picton Mahoney Fortified Income Alternative Fund — A               | PIC 3500    | Credit        |  3.65 |  3.65 |

### Average Metrics by Category
#### Portfolio Managers
| portfolio_managers   |   sharpe_ratio |     apr |
|:---------------------|---------------:|--------:|
| Michael Kuan         |         0.9341 |  9.1453 |
| Michael Kimmel       |         0.9341 |  9.1453 |
| Dashmeet Singh       |         0.8988 |  5.8425 |
| David Picton         |         0.8782 |  9.4055 |
| Jeffrey Bradacs      |         0.8782 |  9.4055 |
| Neil Simons          |         0.8379 |  6.1614 |
| Craig Chilton        |         0.789  |  6.61   |
| Tom Savage           |         0.789  |  6.61   |
| Not specified        |         0.76   | 12.16   |
| Phil Mesman          |         0.6309 |  5.7318 |
| Sam Acton            |         0.6265 |  5.7    |
| Michael White        |         0.5462 |  5.765  |

#### Fund Names
| fund_name                                                             |   sharpe_ratio |   apr |
|:----------------------------------------------------------------------|---------------:|------:|
| Picton Mahoney Fortified Alpha Alternative Fund — ETF                 |           1.62 |  7.54 |
| Picton Mahoney Fortified Alpha Alternative Fund — F                   |           1.61 |  7.17 |
| Picton Mahoney Fortified Alpha Alternative Fund — FT                  |           1.6  |  7.15 |
| Picton Mahoney Fortified Long Short Alternative Fund — ETF            |           1.26 | 14.69 |
| Picton Mahoney Fortified Long Short Alternative Fund — F              |           1.26 | 14.87 |
| Picton Mahoney Fortified Market Neutral Alternative Fund — ETF        |           1.21 |  8.13 |
| Picton Mahoney Fortified Market Neutral Alternative Fund — F          |           1.21 |  7.89 |
| Picton Mahoney Fortified Alpha Alternative Fund — A                   |           1.18 |  6.18 |
| Picton Mahoney Fortified Long Short Alternative Fund — A              |           1.16 | 13.87 |
| Picton Mahoney Special Situations Fund — F                            |           1.02 |  7.46 |
| Picton Mahoney Fortified Market Neutral Alternative Fund — A          |           1.01 |  6.93 |
| Picton Mahoney Fortified Market Neutral Alternative Fund — FT         |           0.96 |  6.37 |
| Picton Mahoney Arbitrage Plus Fund — F                                |           0.95 |  9.3  |
| Picton Mahoney Arbitrage Fund — F                                     |           0.93 |  4.72 |
| Picton Mahoney Fortified Income Fund — FT                             |           0.92 |  5.33 |
| Picton Mahoney Arbitrage Plus Fund — V                                |           0.92 | 11.37 |
| Picton Mahoney Fortified Multi-Asset Fund — FT                        |           0.88 |  7.42 |
| Picton Mahoney Fortified Income Fund — F                              |           0.88 |  5.2  |
| Picton Mahoney Income Opportunities Fund — F                          |           0.87 |  5.78 |
| Picton Mahoney Fortified Multi-Asset Fund — F                         |           0.86 |  7.29 |
| Picton Mahoney Special Situations Fund — A                            |           0.86 |  6.53 |
| Picton Mahoney Arbitrage Plus Fund — A                                |           0.84 |  8.41 |
| Picton Mahoney Fortified Equity Fund — FT                             |           0.81 |  9.86 |
| Picton Mahoney Arbitrage Fund — V                                     |           0.8  |  6.21 |
| Picton Mahoney Fortified Equity Fund — F                              |           0.8  |  9.65 |
| Picton Mahoney Arbitrage Fund — B                                     |           0.8  |  4.27 |
| Picton Mahoney Absolute Alpha Fund — F                                |           0.79 |  6.61 |
| Picton Mahoney Long Short Equity Fund — A                             |           0.79 |  9.16 |
| Picton Mahoney Long Short Equity Fund — F                             |           0.78 |  8.93 |
| Picton Mahoney 130/30 Alpha Extension Fund — I                        |           0.76 | 12.16 |
| Picton Mahoney Fortified Arbitrage Alternative Fund — F               |           0.76 |  5.34 |
| Picton Mahoney Fortified Active Extension Alternative Fund — ETF      |           0.73 | 13.99 |
| Picton Mahoney Fortified Multi-Asset Fund — T                         |           0.73 |  6.41 |
| Picton Mahoney Fortified Equity Fund — T                              |           0.73 |  8.95 |
| Picton Mahoney Fortified Multi-Asset Fund — A                         |           0.72 |  6.3  |
| Picton Mahoney Fortified Income Fund — T                              |           0.72 |  4.38 |
| Picton Mahoney Fortified Income Fund — A                              |           0.71 |  4.32 |
| Picton Mahoney Fortified Active Extension Alternative Fund — F        |           0.71 | 13.16 |
| Picton Mahoney Fortified Equity Fund — A                              |           0.71 |  8.75 |
| Picton Mahoney Income Opportunities Fund — A                          |           0.67 |  4.74 |
| Picton Mahoney Fortified Active Extension Alternative Fund — A        |           0.65 | 12.2  |
| Picton Mahoney Absolute Alpha Fund — A                                |           0.56 |  5.49 |
| Picton Mahoney Fortified Income Alternative Fund — ETF                |           0.55 |  4.75 |
| Picton Mahoney Fortified Income Alternative Fund — F                  |           0.55 |  4.71 |
| Picton Mahoney Fortified Arbitrage Alternative Fund — A               |           0.54 |  4.38 |
| Picton Mahoney Fortified Core Bond Fund — F                           |           0.39 |  7.77 |
| Picton Mahoney Fortified Core Bond Fund — ETF                         |           0.39 |  8    |
| Picton Mahoney Fortified Multi-Strategy Alternative Fund — F          |           0.35 |  5.07 |
| Picton Mahoney Fortified Income Alternative Fund — A                  |           0.34 |  3.65 |
| Picton Mahoney Fortified Multi-Strategy Alternative Fund — ETF        |           0.33 |  4.99 |
| Picton Mahoney Fortified Inflation Opportunities Alternative Fund — F |           0.25 |  4.52 |
| Picton Mahoney Fortified Multi-Strategy Alternative Fund — A          |           0.25 |  4.12 |
| Picton Mahoney Fortified Core Bond Fund — A                           |           0.23 |  6.99 |
| Picton Mahoney Fortified Special Situations Alternative Fund — ETF    |           0.12 |  3.49 |
| Picton Mahoney Fortified Special Situations Alternative Fund — F      |           0.12 |  3.48 |

#### Asset Classes
| asset_class             |   sharpe_ratio |     apr |
|:------------------------|---------------:|--------:|
| Market Neutral Equity   |         1.0975 |  7.33   |
| Equity                  |         0.887  | 11.2972 |
| Merger Arbitrage        |         0.8733 |  7.38   |
| Multi-Asset             |         0.86   |  7.29   |
| Multi-Asset Strategy    |         0.7554 |  6.1754 |
| Alternative Mutual Fund |         0.65   |  4.86   |
| Credit                  |         0.6408 |  4.9092 |
| Core Fixed Income       |         0.3367 |  7.5867 |


<!-- END ANALYTICS -->
