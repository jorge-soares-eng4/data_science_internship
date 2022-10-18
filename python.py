#imports
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#read
df = pd.read_csv('data.csv', sep=";")

corte = df.corte.value_counts()
print(corte)
#print(df)
sns.set_theme(style='darkgrid')

#plot


sns.scatterplot(
    x=df.quilates,
    y=df.preço,
    style=df.corte,
    size=df.plato, sizes=(30, 400),
    hue=df.altura,
)
plt.xscale("log")
plt.title('Preço por Quilates')
plt.xlabel("Quilates(ct)")
plt.ylabel("Preço(k)")
plt.legend(loc=4, title="deu certo")
plt.show()