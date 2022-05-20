import pandas as pd
import csv

file = pd.read_csv("projeto_dataset/csv/ocorrencias_mensais_crimes_sp.csv",encoding="latin-1")
#arquivo recebe uma lista do file somente da coluna cidade
arquivo = csv.reader(file["Cidade"])

valor= 0
nomes = []
#for pecorre toda a lista do arquivo
for i, linha in enumerate(arquivo):
    #if exibe o conteudo da linha somente quando i for maior que valor, 
    # valor e referencia para buscar nomes da cidades pulando todos os anos em que ela aparece
    if i >= valor :
     print("leitura: ", i,linha)
     #nomes insere o conteudo de linha, para armazenar os nomes da cidades que existe na tabela
     nomes.insert(i, linha)
     #valor e somado + 414, pois para cada nova cidade aparecer, e preciso pular 414 linhas
     valor = valor+414
     #apos a leitura de 276673 linhas contidas na tabela o loop termina
    if valor > 276673 :
        break

for linhas in nomes:
    print(linhas)  

#aqui exibe o tamanho da lista nomes para identificar a quantidade de cidade que existe na tabela
print("tamanho nomes: ", len(nomes))    
