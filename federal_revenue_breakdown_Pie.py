import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10,6)     # set default figure size
import numpy as np
import pandas as pd
from matplotlib.patches import Wedge

# import data from given file path
file = 'https://raw.githubusercontent.com/ellie-cothren/Federal-Tax-Figures-E115/main/data/receipts_by_source_amount.csv'
df = pd.read_csv(file)
df = df.set_index('year')


# define fiscal year of interest and data to plot
fy = 2022

ind_income = df.loc[fy]['individual income taxes']
corp_income = df.loc[fy]['corporate income taxes']
excise = df.loc[fy]['excise taxes']
other = df.loc[fy]['other taxes']
social_insurance = df.loc[fy]['ss and retirement receipts (total)']

revenues = [ind_income, corp_income, excise, social_insurance, other]

revenues =  np.divide(revenues, 1e3)    # converting values from 'millions usd' to 'billions usd'
labels = ['Individual Income Taxes', 'Corporate Income Taxes', 'Excise Taxes', 'Social Insurance and Retirement Receipts', 'Other']


# create pie chart
fig, ax = plt.subplots(figsize=(14,8))

def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n(${absolute:d} billion)"

wedges, texts, autotexts = ax.pie(revenues, autopct=lambda pct: func(pct, revenues),
                                  textprops=dict(color="w"),startangle=-45)

ax.legend(wedges, labels,
          title="Source",
          loc="center right",
          bbox_to_anchor=(1,0,0.5,1),
          fontsize = 10)

plt.setp(autotexts, size=10, weight="bold")

plt.suptitle('U.S. Federal Tax Revenues: Fiscal Year %i' %fy,
             fontsize = 20)
plt.title('Total Revenue = $%i billion' %sum(revenues))


# save figure to given file path and display
save_file = 'E115_Tax_Figures/pie_chart.png'
plt.savefig(save_file)

plt.show()


