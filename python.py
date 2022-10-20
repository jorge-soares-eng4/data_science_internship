#imports
from tkinter.ttk import Style
from turtle import color, title
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from matplotlib.colors import Normalize
#read
df = pd.read_csv('data.csv', sep=";")

corte = df.corte.value_counts()
print(corte)
#print(df)
sns.set_theme(style='darkgrid')

#plot
ax = plt.subplots()
norm = plt.Normalize(1.74, 1.84)
sm = plt.cm.ScalarMappable(norm=norm)
sm.set_array([])



ax = sns.scatterplot(x='altura',y='altura', hue="altura",data=df,)

plt.xscale("log")
plt.title('Preço por Quilates')
plt.xlabel("Quilates(ct)")
plt.ylabel("Preço(k)")
plt.legend(loc=4)

sns.scatterplot(
    x=df.quilates,
    y=df.preço,
    style=df.corte,
    size=df.plato, sizes=(0, 400),
    ax=ax,

)
ax.get_legend().remove()
ax.figure.colorbar(sm)
ax.set_title("altura")
plt.xscale("log")
plt.title('Preço por Quilates')
plt.xlabel("Quilates(ct)")
plt.ylabel("Preço(k)")
plt.legend(loc=4)
plt.show()


#sns.boxplot(x=df.quilates, y=df.preço)
#plt.show()