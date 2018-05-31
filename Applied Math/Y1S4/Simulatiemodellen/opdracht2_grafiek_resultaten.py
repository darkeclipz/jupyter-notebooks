# Imports
import matplotlib.pyplot as plt
import pandas as pd

# Data
descr = ['Variant 1', 'Variant 2', 'Variant 3']
len_avg = [6.25, 5.52, 6.52]
len_std = [0.56, 0.45, 0.59]
waittime_avg = [127.70, 112.34, 176.66]
waittime_std = [11.20, 8.78, 14.95]

df = pd.DataFrame({'Variant': descr, 'Rijlengte': len_avg, 'RijStd': len_std, 'Wachttijd': waittime_avg, 'WachtStd': waittime_std})

# Plotting
size = 8
font = {'size'   : 20}
matplotlib.rc('font', **font)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 7))
ax1.bar(df['Variant'], df['Rijlengte'], yerr=df['RijStd'], alpha=0.25, facecolor='black')
ax1.set_ylabel('Personen')
ax1.set_title('Gemiddelde rijlengte')
ax1.grid(ls='dashed')
ax2.bar(df['Variant'], df['Wachttijd'], yerr=df['WachtStd'], alpha=0.25, facecolor='black')
ax2.set_ylabel('Seconden')
ax2.set_title('Gemiddelde wachttijd')
ax2.grid(ls='dashed')

plt.show() # plt.savefig(sometitle.png)