import pandas as pd

data = pd.read_csv("projeto_dataset/alterar_tabela/ds_SSP_ocorrencias_mensais_2001-2019 - Copy.csv",encoding="utf-8")

data = data[(data.Regiao == "Grande São Paulo (exclui a Capital)") & (data.Ano == 2019)& (data.Natureza == "HOMICÍDIO DOLOSO (2)")]

data = data[["Total","Cidade"]]

print(data.sort_values(by = ["Total"],ascending= False))