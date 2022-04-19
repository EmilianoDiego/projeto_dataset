# codigo abaixo apresenta apenas grafico dos dados da tabela

import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

#abrir tabela csv
dataset = pd.read_csv("csv/ocorrencias_mensais_crimes_sp.csv", encoding="latin-1")

#variaveis que possui nomes do tipo de natureza e nome da cidade
#tipo = "HOMICÍDIO DOLOSO"
tipo = "HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO"

#cidade = "São Paulo"
cidade = "Suzano"

#construir dados para alimentar o grafico
dados = dataset[(dataset.Natureza == tipo) & (dataset.Cidade == cidade)].sort_values("Ano")
# tamanho do grafico
plt.figure(figsize = (10,5))
#dados para o grafico posicao X, Y e valores. e cores das barras
sns.barplot(x = "Ano", y="Total",data = dados, color="firebrick")
plt.xticks(rotation=90)
#titulo para apresentar no grafico
plt.title("Homicidios dolosos - cidade de sao paulo",fontsize = 14)
#nomes posicao X na tabela
plt.xlabel("Ano", fontsize = 10)
#nomes posicao Y na tabela
plt.ylabel("numero de homicidios", fontsize = 10)
#apresentar a tabela
plt.show()
