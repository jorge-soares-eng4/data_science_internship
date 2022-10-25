#imports
from logging import handlers
from shutil import which
from tkinter.ttk import Style
from turtle import color, title
import seaborn as sns
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from matplotlib.colors import Normalize
import numpy as np
import matplotlib.legend_handler
import matplotlib.legend

#read
df = pd.read_csv('data.csv', sep=";")

#corte = df.corte.value_counts()
#print(corte)
#print(df)

sns.set_theme(style='darkgrid')

#plot
ax = plt.subplots()
norm = plt.Normalize(df["altura"].min(), df['altura'].max())
sm = plt.cm.ScalarMappable(norm=norm, cmap="RdBu")
sm.set_array([])

ax = sns.scatterplot(x='quilates',y='preço',
 hue="altura", palette="RdBu",
 size="plato",sizes=(40,300),
 style="corte", 
 edgecolor='black',
 linewidth=0.6,
 data=df,
)



#handle_size = handle[7:14]
#label_size = label[7:14]

#legend_size = ax.legend(handle[7:14], label[7:14], title="tamanho do plato", fontsize=40)

#ax.add_artist(legend_size)

plt.xscale("log")
ax.grid(True, which='both', axis="x", ls="-")

ax.xaxis.set_major_formatter(mticker.ScalarFormatter()) #coloca o ticker como valor inteiro

#ax.xaxis.set_minor_locator(mticker.LogLocator(base=10, subs=np.arange(0.1,1,0.1),numticks=10))

plt.title('Preço por Quilates')
plt.xlabel("Quilates(ct)")
plt.ylabel("Preço(k)")

ax.figure.colorbar(sm)
plt.show()