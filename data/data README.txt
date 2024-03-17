Data README

All datasets were pulled from the Tax Policy Center website (https://www.taxpolicycenter.org/statistics)
NOTE: datasets were downloaded as excel spreadsheets, but are in protected view and very stylized (optimal for looking at, but not optimal for data analysis). To make analysis easier, I took a few minutes to clean up the spreadsheets and save as a .csv file in a way that makes working with them in Python much easier


Dataset 1. avg_effective_tax_rates.csv
    url: https://www.taxpolicycenter.org/statistics/historical-average-federal-tax-rates-all-households
    variables: Average Total Federal Tax Rate (percent), Average Individual Income Tax Rate (percent), Average Payroll Tax Rate (percent), Average Corporate Income Tax Rate (percent), Average Excise Tax Rate (percent)
    observations from 1979 to 2019, for the following income groups: Lowest Quintile, Second Quintile, Middle Quintile, Fourth Quintile, Highest Quintile, All Quintiles, 81st - 90th Percentiles, 91st to 95th Percentiles, 96th to 99th Percentiles, Top 1 Percent
    original source: Congressional Budget Office (https://www.cbo.gov/publication/58353)


Dataset 2. receipts_by_source_amount.csv
    url: https://www.taxpolicycenter.org/statistics/amount-revenue-source
    variables: Individual Income Taxes, Corporation Income Taxes, Social Insurance and Retirement Receipts (Total, On-Budget, and Off-Budget), Excise Taxes, Other Taxes, Total Receipts (On-Budget and Off-Budget) - all variables given in millions of USD
    observations from 1934-2022 (with estimates for 2023-2028)
    original source: Office of Management and Budget, Historical Tables, Table 2.1 (http://www.whitehouse.gov/omb/budget/Historicals/


Dataset 3. receipts_by_source_pct.csv
    url: https://www.taxpolicycenter.org/statistics/percentage-revenue-source
    variables: Individual Income Taxes, Corporation Income Taxes, Social Insurance and Retirement Receipts (Total, On-Budget, and Off-Budget), Excise Taxes, Other Taxes, Total Receipts (On-Budget and Off-Budget) - all variables given as percent of total revenue
    observations from 1934-2022 (with estimates for 2023-2028)
    original source: Office of Management and Budget, Historical Tables, Table 2.2 (http://www.whitehouse.gov/omb/budget/Historicals/

NOTE: there was a weird break in the data between 1976 and 1977 labeled TQ - I wasn't sure how to deal with this, so for receipts_by_source_amount.csv and receipts_by_source_pct.csv I only used years 1979-2022 (this matched the time period for other datasets)


Dataset 4: revenue_shares_historical.csv
    url: https://www.taxpolicycenter.org/statistics/type-tax-share-federal-revenues-1934-2018
    variables: Individual Income taxes, Corporation Income Taxes, Social Insurance Tax, Excise Taxes, Other Taxes (percent of total revenue)
    observations from (1934 to 2018)
    original source: Office of Management and Budget, Historical Tables, Table 2.2 (http://whitehouse.gov/omb/budget/Historicals/


