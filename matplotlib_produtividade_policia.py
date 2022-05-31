import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns



dataframe = pd.read_csv("projeto_dataset/csv/ds_SSP_PolicyProductivity_SP-BR_utf8_2001-2021_v5.csv", encoding="utf-8")

cidade = "São Paulo"
natureza = "OCORRÊNCIAS DE PORTE DE ENTORPECENTES"

dados = dataframe[(dataframe.Cidade == cidade) & (dataframe.Natureza == natureza)].sort_values("Ano")
dados2 = dataframe[(dataframe.Cidade == cidade) & (dataframe.Natureza == "OCORRÊNCIAS DE TRÁFICO DE ENTORPECENTES")].sort_values("Ano")
dados3 = dataframe[(dataframe.Cidade == cidade) & (dataframe.Natureza == "Nº DE INFRATORES APREENDIDOS EM FLAGRANTE")].sort_values("Ano")

lista=[]
lista2=[]
lista3=[]

for i, item in enumerate(dados["Total"]):
    lista.insert(i,item)
for i, item in enumerate(dados2["Total"]):
    lista2.insert(i,item)
for i, item in enumerate(dados3["Total"]):
    lista3.insert(i,item)


plt.style.use("ggplot")
#configurar o tamanho do grafico
plt.figure(figsize = (10,8))
sns.barplot(x= "Ano", y="Total",data = dados, color="firebrick")
plt.xticks(rotation=90)
plt.title(natureza +" " + cidade,fontsize = 14)
#descricao do eixos
plt.xlabel("Ano", fontsize = 10)
plt.ylabel("numeros", fontsize = 10);
#apresentar a tabela
plt.show()

#grafico 1
df = pd.DataFrame({'OCORRÊNCIAS DE PORTE DE ENTORPECENTES - cidade São Paulo': lista}, index=dados["Ano"])
ax = df.plot.bar(rot=0)
plt.show()

#grafico 2
df = pd.DataFrame({"OCORRÊNCIAS DE PORTE DE ENTORPECENTES": lista,
                   "OCORRÊNCIAS DE TRÁFICO DE ENTORPECENTES": lista2,
                   "Nº DE INFRATORES APREENDIDOS EM FLAGRANTE": lista3}, index=dados["Ano"])
ax = df.plot.bar(rot=0)
plt.show()

