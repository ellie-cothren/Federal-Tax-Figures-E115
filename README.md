Read Me

All code pulls data from this repository, but any path for a .csv file can be substituted in (may require minor changes, but if the data is just updated for a more recent fiscal year and in the same format, the code should work without needing any changes

The code creates pretty high resolution images by default (dpi=1000), but this slows it down a little bit (only a few seconds). This can be easily changed if necessary. 

effective_rates_IncDist.py - creates a stacked bar chart to show average effective tax burdens for different income groups (quintiles, 81-90 percentiles, 91-95 percentile, 96-99 percentiles, and top 1 perrcent) broken up by tax type, and labels the overall effective tax rate for the income group, for a given fiscal year
    NOTE: the effective tax-rate labels will adjust when you change the fiscal year, but could require minor manual adjsutments to the line width/height


historical_revenues.py - creates a normalized stacked/area plot that shows individual income taxes, corporate income taxes, social insurance tax, excises taxes, and 'other' taxes as a share of total revenue from 1923 to 2018


revenue_breakdown_TS.py - creates a stacked/area plot that shows total federal tax revenues (made up of individual income taxes, corporate income taxes, excise taxes, social insurance and retirement receipts, and other taxes) from 1979 to 2022


revenue_share_breakdown_TS.py - works the same as revenue_breakdown_TS.py, but creates a normalized stacked/area plot that shows revenues from 1979 to 2022 as shares or total revenue


federal_revenue_breakdown_Pie.py - creates a pie chart showing the breakdown of federal tax revenues from individual income taxes, corporate income taxes, social insurance and retirement receipts, excise taxes and 'other' taxes as a percentage of total revenue, for a given fiscal year (default = 2022)


federal_revenue_breakdown_Donut.py - creates a donut chart showing the same info as the pie chart, but without percentages dispayed explicitly (focuses more on the amount of revenue in each category, but the visual still gives an idea of the percentage of total revenue)
    NOTE: some plot styles will make the lines/labels on this plot too difficult to read, but default plot style works for sure


NOTE: variables 'Social Insurance Tax' and 'Social Insurance and Retirement Receipts' are the same, I just follow whatever the variable name in the dataset I'm using is, but this can easily be changed.
