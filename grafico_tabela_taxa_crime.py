#segue abaixo codigo para criar grafico da tabela taxa de criminalidade ,a tabela ainda precisa ser corrigida para leitura das demais colunas,
# com os tipos de natureza onde os numeros sao superior a 1.000.00

import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import plot, show


dataset = pd.read_csv("csv/taxa_crime_sp_alterada.csv",encoding='latin-1',sep=';')
tipos=0           #selecionar tipos de natureza atraves dos numeros
natureza = ["Homicidio Doloso por 100 mil habitantes",#0
             "Furto por 100 mil habitantes",#1
             "Roubo por 100 mil habitantes",#2
             "Furto e Roubo de Veículo por 100 mil habitantes",#3
             "Furto por 100 mil veículos",#4
             "Roubo por 100 mil veículos",#5
             "Furto e Roubo de Veículo por 100 mil veículos"]#6

locais=1 #selecionar locais atraves dos numeros
cidade = ["Sao Paulo",#0
          "Barueri",#1
          "Carapicuíba",#2
          "Cotia",#3
          "Diadema"]#4

dados = dataset[(dataset.Cidade == cidade[locais])].sort_values("Ano")


plt.style.use("ggplot")
#configurar o tamanho do grafico
plt.figure(figsize = (10,8)) 
sns.barplot(x= "Ano", y= natureza[tipos],data = dados, color="firebrick")
plt.xticks(rotation=90)
plt.title(natureza[tipos],fontsize = 14)
#descricao do eixos
plt.xlabel("Ano", fontsize = 10)
plt.ylabel("Numeros na cidade de "+ str(cidade[locais]), fontsize = 10);
#apresentar a tabela
plt.show()