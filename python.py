#imports
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#read
df = pd.read_csv('data.csv', sep=";")

#print(df)

sns.set_theme(style='darkgrid')

#plot
sns.scatterplot(
    x=df.quilates,
    y=df.preço,
    hue=df.corte,
    size=df.plato, sizes=(55, 300),
)

plt.xscale("log")

plt.legend(
    loc=4,
)

plt.title('Preço por Quilates')

plt.xlabel("Quilates(ct)")


plt.ylabel("Preço(k)")

plt.show()