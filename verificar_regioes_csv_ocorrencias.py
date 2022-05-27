import pandas as pd
import csv

file = pd.read_csv("csv/ocorrencias_mensais_crimes_sp.csv", encoding="utf-8")

file = file.fillna(value=0)

# arquivo recebe uma lista do file somente da coluna cidade
arquivo = csv.reader(file["Regiao"])

valor = 0
nomes = []
# for pecorre toda a lista do arquivo
for z, linha in enumerate(arquivo):
    # if exibe o conteudo da linha somente quando i for maior que valor,
    # valor e referencia para buscar nomes da cidades pulando todos os anos em que ela aparece
    if z >= valor:
        print("leitura: ", z, linha)
        # nomes insere o conteudo de linha, para armazenar os nomes da cidades que existe na tabela
        nomes.insert(z, linha)
        # valor e somado + 414, pois para cada nova cidade aparecer, e preciso pular 414 linhas
        valor = valor+414
        # apos a leitura de 276673 linhas contidas na tabela o loop termina
    if valor > 276673:
        break

for linhas in nomes:
    print(linhas)

# aqui exibe o tamanho da lista nomes para identificar a quantidade de cidade que existe na tabela
print("tamanho nomes: ", len(nomes))

texto = ""
totalOcorrenciaCidade = []
cidade = []
totalOcorrencias = 0
z = 4

dados1 = file[(file.Regiao == "Grande S�o Paulo (exclui a Capital)") & (
    file.Natureza == "FURTO DE VE�CULO")].sort_values("Ano")

for z, item in enumerate(dados1["Total"].loc[dados1["Ano"] == 2020]):
    totalOcorrenciaCidade.insert(z, item)

for z, item in enumerate(dados1["Cidade"].loc[dados1["Ano"] == 2020]):
    cidade.insert(z, item)

texto = texto + str(totalOcorrenciaCidade[z]) + "----" + str(cidade[z]) + "\n"
totalOcorrencias = totalOcorrencias + float(totalOcorrenciaCidade[z])

print(texto)
