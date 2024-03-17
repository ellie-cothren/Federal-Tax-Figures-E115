import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Wedge

# import data from given file path
file = 'https://raw.githubusercontent.com/ellie-cothren/Federal-Tax-Figures-E115/main/data/receipts_by_source_amount.csv'
df = pd.read_csv(file)
df = df.set_index('year')

# set preferred plot style
# IMPORTANT: lines drawn to labels won't show up or look good with every style (definitely works with default style)
style_pref = 'default'

plt.style.use(style_pref)

# define fiscal year of interest and data to plot
fy = 2022

ind_income = df.loc[fy]['individual income taxes']
corp_income = df.loc[fy]['corporate income taxes']
excise = df.loc[fy]['excise taxes']
other = df.loc[fy]['other taxes']
social_insurance = df.loc[fy]['ss and retirement receipts (total)']

revenues = [ind_income, corp_income, excise, social_insurance, other]

revenues =  np.divide(revenues, 1e3)    # converting values from 'millions usd' to 'billions usd'

labels = ['Individual Income Taxes', 'Corporate Income Taxes', 'Excise Taxes', 'Social Insurance and Retirement Receipts', 'Other Taxes']


# description for donut labels 

description = ["{}\n(${} billion)".format(label, revenue) for revenue, label in zip(revenues, labels)]


# create donut chart
fig, ax = plt.subplots(figsize=(14, 8), subplot_kw=dict(aspect="equal"))

wedges, texts = ax.pie(revenues, wedgeprops=dict(width=0.5), startangle= 55)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = f"angle,angleA=0,angleB={ang}"
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(description[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

plt.suptitle('U.S. Federal Tax Revenues: Fiscal Year %i' %fy,
             fontsize = 16)
plt.title('Total Revenue = $%i billion' %sum(revenues))


# save figure to given path and display

save_file = 'E115_Tax_Figures/figures/revenue_breakdown.png'
plt.savefig(save_file, dpi=1000)

plt.show()
 


