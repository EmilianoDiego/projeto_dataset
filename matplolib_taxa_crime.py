import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import plot, show


#dataset = pd.read_csv("alterar_tabela/nova_tabela_taxa_crime copy.csv",encoding='latin-1',sep=';')
dataset = pd.read_csv("alterar_tabela/tabela_09_05.csv",sep=';', encoding="utf-8")


cidade = "S�o Paulo"
dados = dataset[(dataset.Cidade == cidade)].sort_values("Ano")


#dados = dataset[(dataset.Cidade == "Barueri")].sort_values("Ano")
#foo = dados.explode("Furto por 100 mil habitantes")
#foo["Furto por 100 mil habitantes"] = foo["Furto por 100 mil habitantes"].astype('float')

#result = dados.explode("Homicidio Doloso por 100 mil habitantes").reset_index(drop=True)
#result = result.assign( valor=result["Homicidio Doloso por 100 mil habitantes"].astype(np.float32))

print("dados: \n", dados)
plt.style.use("ggplot")
#configurar o tamanho do grafico
plt.figure(figsize = (10,8)) 

sns.barplot(x= "Ano", y= "Furto por 100 mil habitantes",data = dados, color="firebrick")

plt.xticks(rotation=90)
plt.title("Furto por 100 mil habitantes " + "-- Cidade Sao paulo",fontsize = 14)
#descricao do eixos
plt.xlabel("Ano", fontsize = 10)
plt.ylabel("Numeros", fontsize = 10)
#apresentar a tabela
plt.show()

lista =[]
for i, item in enumerate(dados["Furto por 100 mil habitantes"]):
    lista.insert(i, item)
lista2 = []
for i, item in enumerate(dados["Furto por 100 mil veículos"]):
    lista2.insert(i, item)   
    lista3 = []
for i, item in enumerate(dados["Roubo por 100 mil habitantes"]):
    lista3.insert(i, item)  


df = pd.DataFrame({'furto por 100 mil habitantes': lista,
                   'Furto por 100 mil veículos': lista2}, index=dados["Ano"])
ax = df.plot.bar(rot=0)
plt.show()



df = pd.DataFrame({'furto por 100 mil habitantes': lista,
                   'Furto por 100 mil veículos': lista2,
                   'Roubo por 100 mil habitantes': lista3}, index=dados["Ano"])
ax = df.plot.bar(rot=0)
plt.show()