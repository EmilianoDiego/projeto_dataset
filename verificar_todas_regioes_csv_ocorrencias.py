import pandas as pd
import csv
import matplotlib.pyplot as plt

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
i = 0
b = 0
soma = 0

natureza = ["LATROCÍNIO", "ROUBO DE CARGA", "TOTAL DE ESTUPRO (4)"]
ano = [2015, 2016, 2017, 2018, 2019]
regiao = []

botaoRegiaoSelecionado = ["Norte", "Sudoeste", "Sudeste", "Oeste", "Leste"]
botaoNaturezaSelecionado = 0
botaoAnoSelecionado = 1

regiaoNorte=["São José dos Campos","Grande S�o Paulo (exclui a Capital)", "Ribeirão Preto"]
regiaoSudoeste=["S�o Jos� do Rio Preto"]
regiaoSudeste=["Sorocaba"]
regiaoOeste=["Presidente Prudente"]
regiaoLeste=["Piracicaba"]

h = 0
listaTotalCadaRegiao = []

while(h < 5):
    if(botaoRegiaoSelecionado[h] == "Norte"):
        regiao = regiaoNorte
    elif(botaoRegiaoSelecionado[h] == "Sudoeste"):
        regiao = regiaoSudoeste
    elif(botaoRegiaoSelecionado[h] == "Sudeste"):
        regiao = regiaoSudeste
    elif(botaoRegiaoSelecionado[h] == "Oeste"):
        regiao = regiaoOeste
    elif(botaoRegiaoSelecionado[h] == "Leste"):
        regiao = regiaoLeste


    while(b < len(regiao)):
        dados1 = file[(file.Regiao == regiao[b]) & (file.Natureza == natureza[botaoNaturezaSelecionado])].sort_values("Ano")

        for z, item in enumerate(dados1["Total"].loc[dados1["Ano"] == ano[botaoAnoSelecionado]]):
            totalOcorrenciaCidade.insert(z, item)

        for z, item in enumerate(dados1["Cidade"].loc[dados1["Ano"] == ano[botaoAnoSelecionado]]):
            cidade.insert(z, item)

        while(i < len(cidade)):
            texto = texto + str(totalOcorrenciaCidade[i]) + "----" + str(cidade[i]) + "\n"
            totalOcorrencias = totalOcorrencias + float(totalOcorrenciaCidade[i])
            i = i + 1

        soma = soma + totalOcorrencias
        print(regiaoNorte[b], totalOcorrencias)
        totalOcorrencias = 0
        b = b + 1

    print("Total Ocorrencia: ", soma) 
    listaTotalCadaRegiao.insert(h, soma)
    soma = 0 
    h = h + 1

print("Lista: ", listaTotalCadaRegiao)

regiaoNumero = [1,2,3,4,5]

#grafico 2
df = pd.DataFrame({"Total Ocorrência": listaTotalCadaRegiao}, index=regiaoNumero)
ax = df.plot.bar(rot=0)
plt.show()