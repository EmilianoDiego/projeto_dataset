import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import plot, show


class crime:
    dataset = pd.read_csv("csv/ocorrencias_mensais_crimes_sp.csv",encoding="latin-1")

    nome = "HOMICÍDIO DOLOSO"
    cidade = "São Paulo"

    dados = dataset[(dataset.Natureza == nome) & (dataset.Cidade == cidade)].sort_values("Ano")
    dados2 = dataset[(dataset.Natureza == "TENTATIVA DE HOMICÍDIO") & (dataset.Cidade == cidade)].sort_values("Ano")
    dados3 = dataset[(dataset.Natureza == "LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO") & (dataset.Cidade == cidade)].sort_values("Ano")
    print(dados[" Jan"])

    plt.style.use("ggplot")
    #configurar o tamanho do grafico
    plt.figure(figsize = (10,8))
    sns.barplot(x= "Ano", y="Total",data = dados, color="firebrick")
    plt.xticks(rotation=90)
    plt.title(nome +" " + cidade,fontsize = 14)
    #descricao do eixos
    plt.xlabel("Ano", fontsize = 10)
    plt.ylabel("numero", fontsize = 10);
    #apresentar a tabela
    plt.show()


    lista=[]
    lista2=[]
    lista3=[]


    for i, item in enumerate(dados["Total"]):
        lista.insert(i,item)
        print(item)
    for i, item in enumerate(dados2["Total"]):
        lista2.insert(i,item)
    for i, item in enumerate(dados3["Total"]):
        lista3.insert(i,item)

    #grafico 2
    df = pd.DataFrame({"HOMICÍDIO DOLOSO": lista,
                   "TENTATIVA DE HOMICÍDIO": lista2,
                   "LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO": lista3}, index=dados["Ano"])
    ax = df.plot.bar(rot=0)
    plt.show()

    #grafico 6
    lines = df.plot.line()
    plt.show()
