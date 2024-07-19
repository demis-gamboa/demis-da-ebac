
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')
sns.lineplot(data=df, x='dia', y='venda')
plt.title('Preço da Gasolina X Longo do Tempo')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)
plt.savefig('gasolina.png')
