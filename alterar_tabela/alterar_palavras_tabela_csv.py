#----- segue abaixo codigo para alterar qualquer letra ou palavra da tabela 
# quando alterar a tabela csv nao deixar a tabela aberta pois a alterarcao sera negada

#abrir tabela escolhida para alterar palavra
with open("alterar_tabela/nova_tabela_taxa_crime.csv",encoding="latin-1")as dataset:

#O join()método string retorna uma string juntando todos os elementos de um iterável (lista, string, tupla), separados por um separador de string.
#toda string do dataset passa pelo loop e armazena no novoDf
 novoDf = ''.join([i for i in dataset])
 
 #replace alterar a palavra: valor a ser trocado↓ , novo valor↓
 novoDf = novoDf.replace(            "Homicídio",    "Homicidio") 
 #aqui vai substituir todas as palavras que possui ã, por somente a
 novoDf = novoDf.replace("ã","a")

 #abrir nova tabela vazia no formato csv, com 'w' para permitir a escrita sobre a tabela  
 novaTabela = open("alterar_tabela/nova_tabela_taxa_crime copy.csv","w") 
 #escrever na novaTabela o texto armazenado em novoDf com a funcao writelines
 novaTabela.writelines(novoDf) 
 #fechar a tabela
 novaTabela.close()