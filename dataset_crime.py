import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


dataset = pd.read_csv('C:\\Users\\Diego\\dataset_projeto\\csv\\ds_SSP_ocorrencias_mensais_2001-2019.csv')
x = dataset.iloc[:,:-1]
print('dados sobre crimes na cidade de sao paulo')
print(x)
#dataset.shape

print(dataset.head(),"\n")
print(dataset.Natureza.value_counts(),"\n")
print(dataset.info(),"\n")

print(dataset.Jun.value_counts())

#Vejamos algumas tipificações de crimes (por exemplo 'HOMICÍDIO DOLOSO (2) em uma cidade específica (por exemplo 'São Paulo'
dataset_hom_dol_sampa = dataset[(dataset.Natureza == "HOMICÍDIO DOLOSO (2)") & (dataset.Cidade == "São Paulo")].sort_values("Ano")
print(dataset_hom_dol_sampa.head(2))

plt.figure(figsize = (10,5))
sns.barplot(x = "Ano", y="Total",data = dataset_hom_dol_sampa, color="firebrick")
plt.xticks(rotation=90)
plt.title("Homicidios dolosos - cidade de sao paulo",fontsize = 14)
plt.xlabel("Ano", fontsize = 10)
plt.ylabel("numero de homicidios", fontsize = 10);
plt.show()
