import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import data from given file path
file = 'https://raw.githubusercontent.com/ellie-cothren/Federal-Tax-Figures-E115/main/data/receipts_by_source_amount.csv'

df = pd.read_csv(file)
df = df.set_index('year')
print(df)


# create time series variables
ind_income = df['individual income taxes'].tolist()
corp_income = df['corporate income taxes'].tolist()
excise = df['excise taxes'].tolist()
other = df['other taxes'].tolist()
social_insurance = df['ss and retirement receipts (total)'].tolist()

revenue_source = [ind_income, corp_income, excise, social_insurance, other]
revenue_source =  np.divide(revenue_source, 1e3)    # converting values from 'millions usd' to 'billions usd'
labels = ['Individual Income Taxes', 'Corporate Income Taxes', 'Excise Taxes', 'Social Insurance and Retirement Receipts', 'Other Taxes']
year = list(range(1979,2023))


# create stacked plot
fig, ax = plt.subplots(figsize=(10,6))
ax.stackplot(year, revenue_source, labels = labels)
ax.legend(loc='upper left')
ax.set_title('U.S. Federal Tax Revenue', fontsize = 20)
ax.set_xlabel('Fiscal Year')
ax.set_ylabel('Revenue (in Billions)')


# save figure and display 
save_file = 'E115_Tax_Figures/stacked.png'
plt.savefig(save_file)

plt.show()

