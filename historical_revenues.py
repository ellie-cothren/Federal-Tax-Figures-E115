import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import data from given file path
file = 'https://raw.githubusercontent.com/ellie-cothren/Federal-Tax-Figures-E115/main/data/revenue_shares_historical.csv'

df = pd.read_csv(file)
df = df.set_index('year')

# set preferred plot style
style_pref = 'bmh'

plt.style.use(style_pref)


# create time series variables
ind_income = df['Individual Income Taxes'].tolist()
corp_income = df['Corporate Income Taxes'].tolist()
social_security = df['Social Insurance Tax'].tolist()
excise = df['Excise Tax'].tolist()
other = df['Other Taxes'].tolist()

fiscal_year = list(range(1934,2019))
revenue_share = [ind_income, corp_income, social_security, excise, other]
labels = ['Individual Income Taxes', 'Corporate Income Taxes', 'Social Insurance Tax', 'Excise Taxes', 'Other Taxes']

# create stacked plot
fig, ax = plt.subplots(figsize=(14,8))
ax.stackplot(fiscal_year, revenue_share, labels=labels)
ax.legend(loc='lower right', fontsize=12)
ax.set_title('U.S. Federal Tax Revenue by Source: 1934 to 2018', fontsize=22)
ax.set_xlabel('Fiscal Year')
ax.set_ylabel('Percentage of Total Revenue')

# save figure and display 
save_file = 'E115_Tax_Figures/figures/revenue_share_historical.png'
plt.savefig(save_file, dpi=1000)

plt.show()