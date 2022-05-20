import pandas as pd
from sklearn import datasets

#abrir o csv com pandas
dataset = pd.read_csv("projeto_dataset/csv/ocorrencias_mensais_crimes_sp.csv",encoding="utf-8")
#imprime os 5 dados da tabela
print(dataset.head())
#imprime somente dados da coluna Jan
print(dataset["Jan"])

#separar os dados da tabela, selecionando uma busca por nome da cidade e tipo de coluna Ano
cidade1 = dataset[(dataset.Cidade == "S�o Paulo")].sort_values("Ano")
#separar os dados da tabela, selecionando uma busca por nome da cidade e tipo de coluna Jan
cidade2 = dataset[(dataset.Cidade == "Barueri")].sort_values("Jan")


#apresentar os dados coletados somente por coluna Jan
print(cidade1["Jan"])
#apresentar dados coletados por cidade2 
print(">>", cidade2)

#pecorrer os dados de cidade apenas para coluna total sendo cidade dados de sao paulo
list = []
for i, item in enumerate(cidade1["Total"]):
    list.insert(i,item)

#pecorrer os dados de cidade apenas para coluna total sendo cidade dados de Barueri
list2 =[]
for i,item in enumerate(cidade2["Total"]):
    list2.insert(i,item)

text = ""
i =0
#aplicar loop para coletar dados da list e list 2 e armazenar em text, onde ficara os dados das duas cidades
while(i < len(list)):
    if i == 0:
        text = text + "Sao paulo ------  Barueri" +"\n"
    #somar os dados coletados
    text = text + str(list[i]) +" ----- " +str(list[i])+"\n"
    i = i+1

#apresentar dados coletados
print("valores\n ", text)    