# segue abaixo codigo para rescrever uma nova tabela

import csv

#-----seleciona a tabela a ser copiada, e abre ela com open propriedade nativa do python
dataset = open("alterar_tabela/taxa_crime_sp.csv", encoding="utf-8") 

#csv.reader Retorne um objeto leitor que irá iterar sobre as linhas no arquivo csv fornecido 
#permite acesso ao delimiter = ';' para separar e identificar as colunas na tabela
arquivo = csv.reader(dataset, delimiter =';')

#listaDf = lista data frame, para inserir a nova linha da tabela
listaDf = []
#nova variavel novoDF= novo dataframe, para receber todo o texto armazenado na lista 
novoDf= ""
#aplicacao do for para pecorrer a linha por linha da tabela
#enumerate método por retorna uma tupla contendo uma contagem (do início cujo padrão é 0) no caso (i, linha)
for i, linha in enumerate(arquivo):
    #listaDf recebe a nova linha da tabela a cada loop
    listaDf.insert(i,linha)
    #novoDf recebe a string propria adicionado + string da listaDf[i] na posicao i do loop for,
    #e ao final e adicionado um pular linha para que o texto possa seguir o formato da tabela
    novoDf = novoDf + str(listaDf[i]) + "\n"

#imprimir o texto do novoDf no terminal
print("arquivo: ", novoDf)
#abrir nova tabela vazia no formato csv, com 'w' para permitir a escrita sobre a tabela
novaTabela = open("alterar_tabela/nova_tabela_taxa_crime copy.csv","w") 
#escrever na novaTabela o texto armazenado em novoDf com a funcao writelines
novaTabela.writelines(novoDf) 
#fechar a tabela
novaTabela.close()



