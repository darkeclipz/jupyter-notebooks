# Imports
import matplotlib.pyplot as plt
import pandas as pd

# Read in the data
df = pd.read_csv('prob_dist_opdracht2.csv', delimiter=';')
df['cumprob'] = df['prob'].cumsum()

# Create a plot
font = {'size'   : 20}
matplotlib.rc('font', **font)
plt.figure(figsize(20,7))
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.bar(df['art_count'], df['prob'], width=1, facecolor='black', alpha=0.25)
ax1.set_xlabel('Aantal artikelen')
ax1.set_ylabel('Kans op aantal artikelen')
ax1.set_title('Kans op aantal artikelen')
ax1.grid(ls='dashed')
ax2.bar(df['art_count'], df['cumprob'], width=1, facecolor='black', alpha=0.25)
ax2.set_xlabel('Aantal artikelen')
ax2.set_ylabel('Kans op aantal artikelen')
ax2.set_title('Kans op aantal artikelen (cumulatief)')
ax2.grid(ls='dashed')
plt.show()  # or: plt.savefig('fig1.jpg')