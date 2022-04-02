#definir area de trabalho
setwd("C:/Users/Diego/dataset_projeto/csv")

#importando base de dados
df <- read.csv("ds_SSP_ocorrencias_mensais_2001-2019.csv")
View(df)

#importando base de dados
db <- read.csv("ds_SSP_PolicyProductivity_SP-BR_utf8_2001-2021_v5.csv",header = TRUE, sep=";")
View(db)

#importando base de dados
dw <- read.csv("ds_SSP_CrimeRate_SP-BR_utf8_2001-2020_.csv",header = TRUE, sep=";")
View(dw)

#excluir variavel
#df$nome_da_coluna <- null

#identifcando os tipos de dados
str(df)
summary(df)

#selecionando variaveis
#buscar coluna
df[1]
#buscar uma coluna especifica
df$Natureza
df$Cidade
#apresenta dados sobre a coluna selecionada
summary(df$Natureza)
summary(df$Jan)


# criando uma nova variavel dentro da tabela
#df$nome_da_nova_coluna <- "a"

#adicionar valores dentro da nova coluna
#df$nome_da_nova_coluna <- c(1,1,1,NA,NA,NA,NA,NA)
