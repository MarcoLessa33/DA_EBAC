
#Importando Bibliotecas

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados do arquivo CSV

df = pd.read_csv('gasolina.csv')

# Criando o gráfico de linha

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='dia', y='venda')
plt.xlabel('DIAS')
plt.ylabel('Preço da Gasolina')
plt.title('Preço da Gasolina x Dias')
plt.grid(True)

# Salvando o gráfico

plt.savefig('gasolina.png')
plt.close()
