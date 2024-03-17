import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# import data from given file path
file = 'https://raw.githubusercontent.com/ellie-cothren/Federal-Tax-Figures-E115/main/data/avg_effective_tax_rates.csv'

df = pd.read_csv(file)
df.columns = 'year', 'measure', 'lowq', '2q', 'midq', '4q', 'highq', 'allq', '80to90p', '91to95p', '96to99p', 'top1p'



# create stacked bar chart for a particular fiscal year (1979 to 2018)
fy = 2018

df_fy = df.loc[df.year == fy]
df_fy = df_fy.set_index('measure')

overall_rate = [df_fy.loc['Average Total Federal Tax Rate'][group] for group in ['lowq', '2q', 'midq', '4q', 'highq']]

quintiles = ['Lowest Quintile', 'Second Quintile', 'Middle Quintile', 'Fourth Quintile', 'Highest Quintile']
effective_rates = {
    'Individual Income Tax': [df_fy.loc['Average Individual Income Tax Rate'][group] for group in ['lowq', '2q', 'midq', '4q', 'highq']],
    'Payroll Tax': [df_fy.loc['Average Payroll Tax Rate'][group] for group in ['lowq', '2q', 'midq', '4q', 'highq']],
    'Corporate Income Tax': [df_fy.loc['Average Corporate Income Tax Rate'][group] for group in ['lowq', '2q', 'midq', '4q', 'highq']],
    'Excise Tax': [df_fy.loc['Average Excise Tax Rate'][group] for group in ['lowq', '2q', 'midq', '4q', 'highq']]
}

data = pd.DataFrame(index = quintiles,
                    data = effective_rates)


overall_rate = np.round(overall_rate, 1)
labels = ["({}%)".format(rate) for rate in overall_rate]

ax = data.plot.bar(stacked=True, rot=0, figsize=(14,8))

ax.bar_label(ax.containers[3], labels = labels, fontsize = 14)
ax.set_ylabel('Average Tax Rate', fontsize = 12)


plt.title('U.S. Federal Tax Revenues: Fiscal Year %i' %fy,
             fontsize = 20)
plt.grid(axis='y')
plt.legend(fontsize=12)


# save figure and display
save_file = 'E115_Tax_Figures/effective_rates.png'
plt.savefig(save_file)

plt.show()

