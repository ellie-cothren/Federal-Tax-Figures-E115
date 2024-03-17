import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# import data from given file path
file = 'https://raw.githubusercontent.com/ellie-cothren/Federal-Tax-Figures-E115/main/data/avg_effective_tax_rates.csv'

df = pd.read_csv(file)
df.columns = 'year', 'measure', 'lowq', '2q', 'midq', '4q', 'highq', 'allq', '80to90p', '91to95p', '96to99p', 'top1p'

# set preferred plot style
style_pref = 'ggplot'
 
plt.style.use(style_pref)

# create stacked bar chart for a particular fiscal year (1979 to 2018)
fy = 2018

df_fy = df.loc[df.year == fy]
df_fy = df_fy.set_index('measure')

overall_rate = [df_fy.loc['Average Total Federal Tax Rate'][group] for group in ['lowq', '2q', 'midq', '4q', 'highq', '80to90p', '91to95p', '96to99p', 'top1p']]

quintiles = ['Lowest Quintile', 'Second Quintile', 'Middle Quintile', 'Fourth Quintile', 'Highest Quintile', '80th to 90th \n Percentile', '91st to 95th \n Percentile', '96th to 99th \n Percentile', 'Top 1 Percent']
effective_rates = {
    'Individual Income Tax': [df_fy.loc['Average Individual Income Tax Rate'][group] for group in ['lowq', '2q', 'midq', '4q', 'highq', '80to90p', '91to95p', '96to99p', 'top1p']],
    'Payroll Tax': [df_fy.loc['Average Payroll Tax Rate'][group] for group in ['lowq', '2q', 'midq', '4q', 'highq', '80to90p', '91to95p', '96to99p', 'top1p']],
    'Corporate Income Tax': [df_fy.loc['Average Corporate Income Tax Rate'][group] for group in ['lowq', '2q', 'midq', '4q', 'highq', '80to90p', '91to95p', '96to99p', 'top1p']],
    'Excise Tax': [df_fy.loc['Average Excise Tax Rate'][group] for group in ['lowq', '2q', 'midq', '4q', 'highq', '80to90p', '91to95p', '96to99p', 'top1p']]
}


data = pd.DataFrame(index = quintiles,
                    data = effective_rates)


overall_rate = np.round(overall_rate, 1)
labels = ["({}%)".format(rate) for rate in overall_rate]

ax = data.plot.bar(stacked=True, rot=0, figsize=(14,8), width=0.8)

ax.bar_label(ax.containers[3], labels = labels, fontsize = 14)
ax.set_ylabel('Average Tax Burden', fontsize = 12)
ax.grid(True)


# add horizontal lines at effective tax rate
# IMPORTANT: when changing the fiscal year, these lines should adjust automatically, but may require a little tweaking in order to look right (especially top 1 percent group)
              
ax.axhline(y=overall_rate[0], xmin=0.025, xmax=0.11, linewidth = 2, linestyle = '--', color='k', label='Effective Tax Rate (%)')            
ax.axhline(y=overall_rate[1], xmin=0.135, xmax=0.22, linewidth=2, linestyle = '--', color='k')
ax.axhline(y=overall_rate[2], xmin=0.244, xmax=0.33, linewidth=2, linestyle='--', color='k')
ax.axhline(y=overall_rate[3], xmin=0.35, xmax=0.43, linewidth=2, linestyle='--', color='k')
ax.axhline(y=overall_rate[4], xmin=0.46, xmax=0.54, linewidth=2, linestyle='--', color='k')
ax.axhline(y=overall_rate[5], xmin=0.565, xmax=0.65, linewidth=2, linestyle='--', color='k')
ax.axhline(y=overall_rate[6], xmin=0.672, xmax=0.755, linewidth=2, linestyle='--', color='k')
ax.axhline(y=overall_rate[7], xmin=0.78, xmax=0.865, linewidth=2, linestyle='--', color='k')
ax.axhline(y=overall_rate[8]-0.35, xmin=0.885, xmax=0.972, linewidth=2, linestyle='--', color='k')      # not sure why, but the line was blocking the (rate%) label, so it's adjusted downward a little bit

ax.legend()



plt.title('U.S. Federal Effective Tax Burdens: Fiscal Year %i' %fy,
             fontsize = 20)
plt.legend(fontsize=12)
plt.ylim(top=36)


# save figure and display
save_file = 'E115_Tax_Figures/figures/effective_rates_IncDist.png'
plt.savefig(save_file, dpi=1000)

plt.show()