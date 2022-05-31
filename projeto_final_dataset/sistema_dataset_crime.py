
from typing import overload
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QPoint,QSize, QSequentialAnimationGroup,QParallelAnimationGroup, QRect
import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from pylab import plot, show
from sklearn.linear_model import LinearRegression
import webbrowser as wb
 



class Ui_MainWindow(object):

    pasta ="projeto_dataset/alterar_tabela/"        
#efeitos de sombra
    shadow = QGraphicsDropShadowEffect()
    shadow2 = QGraphicsDropShadowEffect()
    shadow3 = QGraphicsDropShadowEffect()
    shadow4 = QGraphicsDropShadowEffect()
    shadow5 = QGraphicsDropShadowEffect()
    shadow6 = QGraphicsDropShadowEffect()
    tabela = "" 
    buttonMarca1 = "background-color: rgb(255, 255, 255,0.0);"
    buttonMarca2 = "background-color: rgb(255, 255, 255,0.0);"
    buttonMarca3 = "background-color: rgb(255, 255, 255,0.0);"

    def style(self,valor):
            if(valor == 1 ):
                buttonMarca1 = ""
                buttonMarca2 = "0.0"
                buttonMarca3 = "0.0"
            elif(valor == 2):
                buttonMarca1 = "0.0"
                buttonMarca2 = ""
                buttonMarca3 = "0.0"
            elif(valor == 3):                
                buttonMarca1 = "0.0"
                buttonMarca2 = "0.0"
                buttonMarca3 = ""                   
            self.btn_ocorrencias.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 250,"+buttonMarca1+");\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(158, 199, 226, 255), stop:0.761364 rgba(255, 255, 255, 255));\n"
"\n"
"}")
            self.btn_taxa.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,"+buttonMarca2+");\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(158, 199, 226, 255), stop:0.761364 rgba(255, 255, 255, 255));\n"
"\n"
"}") 
            self.btn_policia.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,"+buttonMarca3+");\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(158, 199, 226, 255), stop:0.761364 rgba(255, 255, 255, 255));\n"
"\n"
"}")           

    def linkNoticia(self,noticia):
            if(noticia == 1):
                wb.open("https://www.ssp.sp.gov.br/LeNoticia.aspx?ID=54131")
            elif(noticia == 2):
                wb.open("https://www.ssp.sp.gov.br/noticia/LeFotos.aspx?id=19709")
            else:
                wb.open("https://www.ssp.sp.gov.br/noticia/LeFotos.aspx?id=19711")                

    def duas_cidades(self):    
        natureza = self.comboBox_comparacao.currentText()
        cidade = self.comboBox_primeiraCidade.currentText()
        cidade2 = self.comboBox_segundaCidade.currentText() 
        #verifica se os itens no combobox foram selecionados
        if (self.tabela == "Selecione") or (natureza == "Selecione") or (cidade == "Selecione") or (cidade2 == "Selecione"):
            self.frame_label_erro.show()
        #tabela TAXA_CRIME    
        elif self.tabela == "tabela_taxa_crime_sp.csv":
                self.frame_label_erro.hide()
                dataset = pd.read_csv(self.pasta + self.tabela,sep=';', encoding="utf-8")

                dados = dataset[(dataset.Cidade == cidade)].sort_values("Ano")
                dados_outra = dataset[(dataset.Cidade == cidade2)].sort_values("Ano")
                lista =[]
                for i, item in enumerate(dados[natureza]):
                        lista.insert(i, item)
                #outra cidade
                lista_outra =[]
                for i, item in enumerate(dados_outra[natureza]):
                        lista_outra.insert(i, item)

                #grafico de duas cidades
                #configurar o tamanho do grafico
                plt.rcParams["figure.figsize"] = (9,6)
                df = pd.DataFrame({natureza +" - " + cidade: lista,
                                   natureza +" - " + cidade2: lista_outra}, index=dados["Ano"])
                #grafico 1                   
                ax = df.plot.bar(rot=0)
                plt.show()
                #grafico 2
                lines = df.plot.line()
                plt.show()
        #tabela ocorrencias_mensais_crimes_sp.csv    
        elif self.tabela == "ds_SSP_ocorrencias_mensais_2001-2019 - Copy.csv":
                self.frame_label_erro.hide()
                #busca o dados da tabela csv             
                dataset = pd.read_csv(self.pasta +self.tabela, encoding="utf-8")
                dataset = dataset.fillna(value= 0)
                #busca os dados da tabela apartir do tipo de natureza em qual cidade e pelo periodo dos anos contidos na tabela    
                dados = dataset[(dataset.Natureza == natureza) & (dataset.Cidade == cidade)].sort_values("Ano")    
                dados_outra = dataset[(dataset.Natureza == natureza) & (dataset.Cidade == cidade2)].sort_values("Ano")
                lista =[]
                for i, item in enumerate(dados["Total"]):
                        lista.insert(i, item)   
                #outra cidade
                lista_outra =[]
                for i, item in enumerate(dados_outra["Total"]):
                        lista_outra.insert(i, item) 
                #grafico de duas cidades
                #configurar o tamanho do grafico
                plt.rcParams["figure.figsize"] = (9,6)
                df = pd.DataFrame({natureza +" - " + cidade: lista,
                                   natureza +" - " + cidade2: lista_outra}, index=dados["Ano"])
                #grafico 1                   
                ax = df.plot.bar(rot=0)
                plt.show()
                #grafico 2
                lines = df.plot.line()
                plt.show()

        #tabela tabela_policia_produtividade.csv    
        elif self.tabela == "tabela_policia_produtividade.csv":
                self.frame_label_erro.hide()
                dataset = pd.read_csv(self.pasta + self.tabela, encoding="utf-8")

                dados = dataset[(dataset.Cidade == cidade) & (dataset.Natureza == natureza)].sort_values("Ano")
                dados_outra = dataset[(dataset.Cidade == cidade2)& (dataset.Natureza == natureza)].sort_values("Ano")
                lista =[]
                for i, item in enumerate(dados["Total"]):
                        lista.insert(i, item)
                #outra cidade
                lista_outra =[]
                for i, item in enumerate(dados_outra["Total"]):
                        lista_outra.insert(i, item)
                #grafico de duas cidades
                #configurar o tamanho do grafico
                plt.rcParams["figure.figsize"] = (9,6)
                df = pd.DataFrame({natureza +" - " + cidade: lista,
                                   natureza +" - " + cidade2: lista_outra}, index=dados["Ano"])
                #grafico 1                   
                df.plot.bar(rot=0)
                plt.show()
                #grafico 2
                df.plot.line()
                plt.show()

    #busca criada para verificar graficos de 1 cidade    
    def opcao_selecionada(self):
        natureza = self.comboBox_TipoBusca.currentText()
        cidade = self.comboBox_Municipio.currentText() 
        #verifica se os itens no combobox foram selecionados
        if (self.tabela == "Selecione") or (natureza == "Selecione") or (cidade == "Selecione"):
            self.frame_label_erro.show()

        #tabela TAXA_CRIME    
        elif self.tabela == "tabela_taxa_crime_sp.csv":
                self.frame_label_erro.hide()
                dataset = pd.read_csv(self.pasta + self.tabela,sep=';', encoding="utf-8")
                dados = dataset[(dataset.Cidade == cidade)].sort_values("Ano")
                lista =[]
                for i, item in enumerate(dados[natureza]):
                        lista.insert(i, item)
                #grafico 1
                #configurar o tamanho do grafico
                plt.rcParams["figure.figsize"] = (9,6)
                df = pd.DataFrame({natureza: lista}, index=dados["Ano"])
                ax = df.plot.bar(rot=0)
                plt.show()

        #tabela OCORRENCIAS_MENSAIS
        elif self.tabela == "ds_SSP_ocorrencias_mensais_2001-2019 - Copy.csv":   
            self.frame_label_erro.hide() 
            #busca o dados da tabela csv             
            dataset = pd.read_csv(self.pasta + self.tabela, encoding="utf-8")
            dataset = dataset.fillna(value= 0)
            #busca os dados da tabela apartir do tipo de natureza em qual cidade e pelo periodo dos anos contidos na tabela    
            dados = dataset[(dataset.Natureza == natureza) & (dataset.Cidade == cidade)].sort_values("Ano")
            #envia os dados para a construcao do grafico com matplotlib 
            # #configurar o tamanho do grafico
            plt.rcParams["figure.figsize"] = (9,6)   
            sns.barplot(x = "Ano", y="Total",data = dados, color="blue")
            plt.xticks(rotation=90)
            plt.title(natureza +" "+ cidade,fontsize = 14)
            plt.xlabel("Ano", fontsize = 10)
            plt.ylabel("numeros de:"+ natureza, fontsize = 10)
            #apresenta o grafico
            plt.show()

        #tabela POLICIA_PRODUTIVIDADE
        elif self.tabela == "tabela_policia_produtividade.csv":
                self.frame_label_erro.hide() 
                #busca o dados da tabela csv 
                dataset = pd.read_csv(self.pasta+ self.tabela, encoding="utf-8")
                #busca os dados da tabela apartir do tipo de natureza em qual cidade e pelo periodo dos anos contidos na tabela
                dados = dataset[(dataset.Cidade == cidade) & (dataset.Natureza == natureza)].sort_values("Ano")
                lista=[]
                for i, item in enumerate(dados["Total"]):
                        lista.insert(i,item)
                #grafico 1
                #configurar o tamanho do grafico
                plt.rcParams["figure.figsize"] = (9,6)
                df = pd.DataFrame({natureza: lista}, index=dados["Ano"])
                ax = df.plot.bar(rot=0)
                plt.show()            

#metodo de controle do movimento do menu principal
    def toggleMenu(self,maxWidth, enable):
        if enable:  
            #get width
            width = self.frame_Mbuttons.width()
            maxExtend = maxWidth
            standard =10
            #set max width
            if width == 10:
                widthExtended = maxExtend
            else:
                widthExtended = standard

        self.animation = QPropertyAnimation(self.frame_Mbuttons, b"maximumWidth")
        self.animation.setDuration(600)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.start()      

    def animacaoPrevisao(self):
        self.shadow2.setBlurRadius(25)
        self.shadow2.setOffset(-5,10)
        self.frame_resultadoPrevisao.setGraphicsEffect(self.shadow2)

        self.anim_1 = QPropertyAnimation(self.frame_conection, b"size")
        self.anim_1.setEndValue(QSize(350, 150))
        self.anim_1.setDuration(2000)

        self.anim_2 = QPropertyAnimation(self.frame_resultadoPrevisao, b"size")
        self.anim_2.setEndValue(QSize(350, 150))
        self.anim_2.setDuration(2000)

        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()
                     

    def dataset(self):
        if(self.frame_Mbuttons.width() == 10):
                self.toggleMenu(300,True)    
        width2 = self.frame_previsao.width()
        maxExtend = 350
        standard =0
        #set max width
        if width2 == 0:
                widthExtended = maxExtend
        else:
                widthExtended = standard
        self.shadow6.setBlurRadius(25)
        self.shadow6.setOffset(-5,10)
        self.frame_previsao.setGraphicsEffect(self.shadow6)

        self.animationdata = QPropertyAnimation(self.frame_previsao, b"maximumWidth")
        self.animationdata.setDuration(600)
        self.animationdata.setStartValue(width2)
        self.animationdata.setEndValue(widthExtended)
        self.animationdata.start() 
    

    def previsao(self):
        if (self.comboBox_previsaoCidade.currentText() == "Selecione") or (self.comboBox_previsaoNatureza.currentText() == "Selecione"):
            self.frame_erroPrevisao.show()  

        elif self.tabela == "ds_SSP_ocorrencias_mensais_2001-2019 - Copy.csv":
  
                #inicia a animacao para previsao
                self.animacaoPrevisao()

                #buscar cidade e natureza selecionada
                cidadeP = self.comboBox_previsaoCidade.currentText()
                naturezaP = self.comboBox_previsaoNatureza.currentText() 
                #busca o dados da tabela            
                dataset = pd.read_csv(self.pasta + self.tabela, encoding="utf-8")
                #limpar tabela de valores NA
                dataset = dataset.fillna(value= 0)    
                #selecionar colunas necessarias para coleta de dados de total e ano atraves da cidade escolhida e o tipo de natureza escolhido
                dataset = dataset[(dataset.Cidade == cidadeP) & (dataset.Natureza == naturezaP)]
                #coletar dados da coluna
                dataset = dataset[["Total","Ano"]]
                #construir uma lista para cada coluna com dados da coluna da tabela
                lista = []
                for i , item in enumerate(dataset["Ano"]):
                        lista.insert(i, item)
                lista2 = []
                for y , item in enumerate(dataset["Total"]):
                        lista2.insert(y, item)
                #inverter os dados da coluna para se ajustar em ordem        
                lista = list(reversed(lista))
                lista2 = list(reversed(lista2))
                #passar os dados da lista em forma de matriz para as variaveis X e Y
                X = np.array(lista[13:22]).reshape((-1,1))
                y= np.array(lista2[13:22])
                #Dividindo os dados em Treino e Teste
                from sklearn.model_selection import train_test_split
                X_train,  X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=50)
                # criar modelo preditor
                modeloPreditor = LinearRegression()
                # iniciar aprendizado
                modeloPreditor.fit(X_train, y_train)
                coeficiente = pd.DataFrame(modeloPreditor.coef_)
                print("coeficiente ", coeficiente)
                # predições com os dados de teste
                y_predictions = modeloPreditor.predict(X_test)
                #construir graficos
                ax = sns.lmplot(x= "Ano", y = "Total", data = dataset)
                #configurar tamanho
                ax.fig.set_size_inches(6,3)
                ax.fig.suptitle("reta de regressao - Ano X total", fontsize = 18, y=1.02)
                ax.set_xlabels("Ano", fontsize =14)
                ax.set_ylabels("Total", fontsize = 14)
                plt.show()
                #construir grafico para predicao
                plt.scatter(X,y, color="red")
                plt.plot(X_test, y_predictions, color ="blue", linewidth=5)
                plt.show()

                prever =np.array([2021,2022,2023]).reshape((-1,1))
                y_predictions = modeloPreditor.predict(prever)
                listaPredicao =[]
                for w,item in enumerate(y_predictions):
                        listaPredicao.insert(w,item)
                self.label_resultadoAno1.setText(( str(int(listaPredicao[0]))))
                self.label_resultadoAno2.setText(( str(int(listaPredicao[1]))))
                self.label_resultadoAno3.setText(( str(int(listaPredicao[2]))))
                #extrair valores rquadrado
                self.label_resuConfianca.setText(( "{:.2f}".format(modeloPreditor.score(X, y)))+"%")

        elif self.tabela == "tabela_policia_produtividade.csv":  
                self.animacaoPrevisao()
                self.frame_label_erro.hide()
                cidadeP = self.comboBox_previsaoCidade.currentText()
                naturezaP = self.comboBox_previsaoNatureza.currentText() 
                #busca o dados da tabela csv             
                dataset = pd.read_csv(self.pasta + self.tabela, encoding="utf-8")
                dataset = dataset.fillna(value= 0)    
                # dados do csv referente a tabela de ocorrencias, na cidade de sao paulo de natureza = homicidio doloso
                dataset = dataset[(dataset.Cidade == cidadeP) & (dataset.Natureza == naturezaP)]
                dataset = dataset[["Total","Ano"]]
                lista = []
                for i , item in enumerate(dataset["Ano"]):
                        lista.insert(i, item)
                lista2 = []
                for y , item in enumerate(dataset["Total"]):
                        lista2.insert(y, item)
                lista = list(reversed(lista))
                lista2 = list(reversed(lista2))

                X = np.array(lista[13:22]).reshape((-1,1))
                y= np.array(lista2[13:22])

                from sklearn.model_selection import train_test_split

                X_train,  X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=50)

                modeloPreditor = LinearRegression()
                modeloPreditor.fit(X_train, y_train)
                coeficiente = pd.DataFrame(modeloPreditor.coef_)
                y_predictions = modeloPreditor.predict(X_test)

                ax = sns.lmplot(x= "Ano", y = "Total", data = dataset)
                ax.fig.set_size_inches(6,3)
                ax.fig.suptitle("reta de regressao - Ano X total", fontsize = 18, y=1.02)
                ax.set_xlabels("Ano", fontsize =14)
                ax.set_ylabels("Total", fontsize = 14)
                plt.show()

                plt.scatter(X,y, color="red")
                plt.plot(X_test, y_predictions, color ="blue", linewidth=2)
                plt.show()

                prever =np.array([2021,2022,2023]).reshape((-1,1))
                y_predictions = modeloPreditor.predict(prever)
                listaPredicao2 =[]
                for w,item in enumerate(y_predictions):
                        listaPredicao2.insert(w,item)
                self.label_resultadoAno1.setText(( str(int(listaPredicao2[0]))))
                self.label_resultadoAno2.setText(( str(int(listaPredicao2[1]))))
                self.label_resultadoAno3.setText(( str(int(listaPredicao2[2]))))
                self.label_resuConfianca.setText(( "{:.2f}".format(modeloPreditor.score(X, y)))+"%") 

        elif self.tabela == "tabela_taxa_crime_sp.csv":
                self.animacaoPrevisao()
                self.frame_label_erro.hide()
                cidadeP = self.comboBox_previsaoCidade.currentText()
                naturezaP = self.comboBox_previsaoNatureza.currentText()

                dataset3 = pd.read_csv(self.pasta +"tabela_taxa_crime_sp.csv", encoding="utf-8",sep=';')
                dataset3 = dataset3.fillna(value =0)
                dataset3 = dataset3[(dataset3.Cidade == cidadeP)]
                dataset3 = dataset3[[naturezaP,"Ano"]]
                print(dataset3.head(50))

                X = np.array(dataset3["Ano"]).reshape((-1,1))
                y= dataset3[naturezaP]

                from sklearn.model_selection import train_test_split

                X_train,  X_test, y_train, y_test = train_test_split(X,y, test_size=0.1, random_state=40)

                modeloPreditor = LinearRegression()

                modeloPreditor.fit(X_train, y_train)

                coeficiente = pd.DataFrame(modeloPreditor.coef_)

                y_predictions = modeloPreditor.predict(X_test)

                ax = sns.lmplot(x= "Ano", y = naturezaP, data = dataset3)
                ax.fig.set_size_inches(6,3)
                ax.fig.suptitle("reta de regressao - Ano X total", fontsize = 18, y=1.02)
                ax.set_xlabels("Ano", fontsize =14)
                ax.set_ylabels("Total", fontsize = 14)
                plt.show()

                plt.scatter(X,y, color="red")
                plt.plot(X_test, y_predictions, color ="blue", linewidth=2)
                plt.show()

                prever =np.array([2021,2022,2023]).reshape((-1,1))
                y_predictions = modeloPreditor.predict(prever)
                listaPredicao3 =[]
                for w,item in enumerate(y_predictions):
                        listaPredicao3.insert(w,item)
                self.label_resultadoAno1.setText(( str(int(listaPredicao3[0]))))
                self.label_resultadoAno2.setText(( str(int(listaPredicao3[1]))))
                self.label_resultadoAno3.setText(( str(int(listaPredicao3[2]))))
                self.label_resuConfianca.setText(( "{:.2f}".format(modeloPreditor.score(X, y)))+"%")
          


#metodo para tabela de ocorrencia
    def ocorrencia(self):
            self.style(1)
            if self.frame_lista.width() > 100:
                    self.animacaoLista()
            self.tabela = "ds_SSP_ocorrencias_mensais_2001-2019 - Copy.csv"
            if self.frame_lista.width() == 1 & self.frame_mapa.width() == 1 :
                    self.mapaSp()
            elif self.frame_lista.width() == 300:
                self.lista()
            elif self.frame_previsao.width() > 0:
                self.dataset()        

    def taxa_crime(self):
            self.style(2)
            if self.frame_lista.width() > 100:
                    self.animacaoLista()
            self.tabela = "tabela_taxa_crime_sp.csv"
            if self.frame_lista.width() == 1 & self.frame_mapa.width() == 1 :
                    self.mapaSp()
            elif self.frame_lista.width() == 300:
                self.lista()
            elif self.frame_previsao.width() > 0:
                self.dataset()    

    def policia_prod(self):
            self.style(3)
            if self.frame_lista.width() > 100:
                    self.animacaoLista()
            self.tabela = "tabela_policia_produtividade.csv"
            if self.frame_lista.width() == 1 & self.frame_mapa.width() == 1 :
                    self.mapaSp()
            elif self.frame_lista.width() == 300:
                self.lista()
            elif self.frame_previsao.width() > 0:
                self.dataset()                 

    #metodo de chamada do mapa
    def mapaSp(self):
            #get width
            width = self.frame_mapa.width()
            maxExtend = 890
            standard =1
            #set max width
            if width == 1:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            self.animation = QPropertyAnimation(self.frame_mapa, b"maximumWidth")
            self.animation.setDuration(800)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()  


    def animacaoDataset(self):

            effect = QGraphicsOpacityEffect(self.btn_dataset)
            self.btn_dataset.setGraphicsEffect(effect)
            self.anim_effectDataset = QPropertyAnimation(effect, b"opacity")
            self.anim_effectDataset.setStartValue(0)
            self.anim_effectDataset.setEndValue(1)
            self.anim_effectDataset.setDuration(1000)

            self.a = QPropertyAnimation(self.btn_dataset, b"size")
            self.a.setEndValue(QSize(100, 100))
            self.a.setDuration(400)

            self.b = QPropertyAnimation(self.btn_dataset, b"size")
            self.b.setEndValue(QSize(70, 70))
            self.b.setDuration(400) 

            self.anim_groupDataset = QParallelAnimationGroup()
            self.anim_groupDataset.addAnimation(self.anim_effectDataset)
            self.anim_groupDataset.addAnimation(self.a)

            self.anim_sequencialDataset = QSequentialAnimationGroup()    
            self.anim_sequencialDataset.addAnimation(self.anim_groupDataset)
            self.anim_sequencialDataset.addAnimation(self.b)
            self.anim_sequencialDataset.start() 

    #metodo de chamada da lista 
    def lista(self,regiao,regiao2):
        self.animacaoPrevisao()
        self.animacaoDataset()
        if self.frame_previsao.width() > 0:
                self.dataset()

        if self.tabela == "ds_SSP_ocorrencias_mensais_2001-2019 - Copy.csv":
                if regiao == "0":
                        self.frame_erro.show()    
                self.comboBox_Municipio.clear()
                self.comboBox_TipoBusca.clear()
                self.comboBox_primeiraCidade.clear()
                self.comboBox_segundaCidade.clear()
                self.comboBox_comparacao.clear()  
                self.comboBox_previsaoCidade.clear() 
                self.comboBox_previsaoNatureza.clear()  
                #preencher a lista com cidade e tipo de natureza de acordo com a regiao
                file = pd.read_csv(self.pasta+"ds_SSP_ocorrencias_mensais_2001-2019 - Copy.csv", encoding="utf-8")
                nature = file[(file.Cidade == "São Paulo") & (file.Ano == 2010)]
                listaNatureza=["Selecione"]
                for y, item2 in enumerate(nature["Natureza"]):
                        listaNatureza.insert(y, item2)   
                cidades =file[(file.Regiao == regiao) & (file.Ano == 2010) & (file.Natureza == "HOMICÍDIO DOLOSO (2)")]
                listaCidade =["Selecione"]
                for i, item in enumerate(cidades["Cidade"]):
                        listaCidade.insert(i,item)

        elif self.tabela == "tabela_taxa_crime_sp.csv": 
                if regiao2 == "0":
                        self.frame_erro.show()

                self.comboBox_Municipio.clear()
                self.comboBox_TipoBusca.clear()
                self.comboBox_primeiraCidade.clear()
                self.comboBox_segundaCidade.clear()
                self.comboBox_comparacao.clear()
                self.comboBox_previsaoCidade.clear() 
                self.comboBox_previsaoNatureza.clear()     
                #preencher a lista com cidade e tipo de natureza de acordo com a regiao
                file = pd.read_csv(self.pasta+"tabela_taxa_crime_sp.csv", encoding="utf-8", sep=";")
                cidades =file[(file.Regiao == regiao2) & (file.Ano == 2010)]
                listaCidade =["Selecione"]
                for i, item in enumerate(cidades["Cidade"]):
                        listaCidade.insert(i,item)
                listaNatureza=["Homicídio Doloso por 100 mil habitantes",
                                "Furto por 100 mil habitantes","Roubo por 100 mil habitantes",
                                "Furto e Roubo de Veículo por 100 mil habitantes",
                                "Furto por 100 mil veículos",
                                "Roubo por 100 mil veículos",
                                "Furto e Roubo de Veículo por 100 mil veículos","Selecione"]

        elif self.tabela == "tabela_policia_produtividade.csv": 
                if regiao == "0":
                        self.frame_erro.show()   
                self.comboBox_Municipio.clear()
                self.comboBox_TipoBusca.clear()
                self.comboBox_primeiraCidade.clear()
                self.comboBox_segundaCidade.clear()
                self.comboBox_comparacao.clear()
                self.comboBox_previsaoCidade.clear() 
                self.comboBox_previsaoNatureza.clear()     
                #preencher a lista com cidade e tipo de natureza de acordo com a regiao
                file = pd.read_csv(self.pasta+"tabela_policia_produtividade.csv", encoding="utf-8")
                nature = file[(file.Cidade == "São Paulo") & (file.Ano == 2010)]
                listaNatureza=["selecione"]
                for y, item2 in enumerate(nature["Natureza"]):
                        listaNatureza.insert(y, item2)   
                cidades =file[(file.Regiao == regiao) & (file.Ano == 2010) & (file.Natureza == "OCORRÊNCIAS DE PORTE DE ENTORPECENTES")]
                listaCidade =["Selecione"]
                for i, item in enumerate(cidades["Cidade"]):
                        listaCidade.insert(i,item)                                                

        self.comboBox_TipoBusca.addItems(list(reversed(listaNatureza)))  
        self.comboBox_Municipio.addItems(list(reversed(listaCidade)))
        self.comboBox_primeiraCidade.addItems(list(reversed(listaCidade)))  
        self.comboBox_segundaCidade.addItems(list(reversed(listaCidade)))
        self.comboBox_comparacao.addItems(list(reversed(listaNatureza)))      
        self.comboBox_previsaoCidade.addItems(list(reversed(listaCidade)))      
        self.comboBox_previsaoNatureza.addItems(list(reversed(listaNatureza)))      
        self.animacaoLista()


    def animacaoLista(self):    
        height = self.frame_lista.width()
        height2 = self.frame_noticias_2.width()
        maxExtend = 300
        standard =1
        noticiaMinimize = 0
        #set max width   
        if height == 1:
                widthExtended = maxExtend
                noticiaMinimize = 0
        else:
                widthExtended = standard
                noticiaMinimize = 271
        self.shadow = QGraphicsDropShadowEffect()  
        self.shadow.setBlurRadius(25)
        self.shadow.setOffset(-5,10)
        self.frame_lista.setGraphicsEffect(self.shadow)

        self.animation = QPropertyAnimation(self.frame_lista, b"maximumWidth")
        self.animation.setDuration(600)
        self.animation.setStartValue(height)
        self.animation.setEndValue(widthExtended)
         
        self.animation2 = QPropertyAnimation(self.frame_noticias_2, b"maximumWidth")
        self.animation2.setDuration(600)
        self.animation2.setStartValue(height2)
        self.animation2.setEndValue(noticiaMinimize)

        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.animation)
        self.anim_group.addAnimation(self.animation2)
        self.anim_group.start()              


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 848)
        MainWindow.setMaximumSize(QtCore.QSize(1250, 850))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(625, 400))
        self.centralwidget.setMaximumSize(QtCore.QSize(1250, 800))
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.frame_menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_menu.setEnabled(True)
        self.frame_menu.setMaximumSize(QtCore.QSize(1250, 100))
        self.frame_menu.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.132545, y1:0.676, x2:0.361, y2:1, stop:0.148299 rgba(21, 132, 188, 246), stop:0.971591 rgba(255, 255, 255, 239));")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_menu)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.frame_bt_Menu = QtWidgets.QFrame(self.frame_menu)
        self.frame_bt_Menu.setMinimumSize(QtCore.QSize(180, 80))
        self.frame_bt_Menu.setMaximumSize(QtCore.QSize(180, 80))
        self.frame_bt_Menu.setAutoFillBackground(False)
        self.frame_bt_Menu.setStyleSheet("background-color: rgb(255, 255, 255,0.0);")
        self.frame_bt_Menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bt_Menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bt_Menu.setObjectName("frame_bt_Menu")

        self.button_Mdataset = QtWidgets.QPushButton(self.frame_bt_Menu)
        self.button_Mdataset.setGeometry(QtCore.QRect(0, 20, 180, 51))
        self.button_Mdataset.setMaximumSize(QtCore.QSize(180, 100))
        self.button_Mdataset.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Segoe UI Emoji\";\n"
"border:none;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-bottom: 2px solid;\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0.965909, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 109, 180, 255));\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/logo_crime.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_Mdataset.setIcon(icon)
        self.button_Mdataset.setIconSize(QtCore.QSize(50, 50))
        self.button_Mdataset.setObjectName("button_Mdataset")
        self.horizontalLayout_2.addWidget(self.frame_bt_Menu)

        self.frame_logoCidade = QtWidgets.QFrame(self.frame_menu)
        self.frame_logoCidade.setMinimumSize(QtCore.QSize(400, 80))
        self.frame_logoCidade.setMaximumSize(QtCore.QSize(1000, 80))
        self.frame_logoCidade.setStyleSheet("background-color: rgb(255, 255, 255,0.0);")
        self.frame_logoCidade.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_logoCidade.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logoCidade.setObjectName("frame_logoCidade")

        self.label_Criminalidade = QtWidgets.QLabel(self.frame_logoCidade)
        self.label_Criminalidade.setGeometry(QtCore.QRect(50, 20, 271, 41))
        self.label_Criminalidade.setMaximumSize(QtCore.QSize(280, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_Criminalidade.setFont(font)
        self.label_Criminalidade.setStyleSheet("QLabel{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"    font: 87 16pt \"Arial Black\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_Criminalidade.setTextFormat(QtCore.Qt.AutoText)
        self.label_Criminalidade.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Criminalidade.setObjectName("label_Criminalidade")

        self.frame_logo_sp = QtWidgets.QFrame(self.frame_logoCidade)
        self.frame_logo_sp.setGeometry(QtCore.QRect(220, -10, 451, 121))
        self.frame_logo_sp.setMaximumSize(QtCore.QSize(451, 121))
        self.frame_logo_sp.setStyleSheet("\n"
"image: url(:/logo/logo_sp.png);\n"
"background-color: rgb(255, 255, 255,0.0);")
        self.frame_logo_sp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_logo_sp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo_sp.setObjectName("frame_logo_sp")
        self.horizontalLayout_2.addWidget(self.frame_logoCidade)
        self.verticalLayout_3.addWidget(self.frame_menu)

        self.frame_fundo = QtWidgets.QFrame(self.centralwidget)
        self.frame_fundo.setMinimumSize(QtCore.QSize(625, 410))
        self.frame_fundo.setMaximumSize(QtCore.QSize(1250, 800))
        self.frame_fundo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_fundo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_fundo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fundo.setObjectName("frame_fundo")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_fundo)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.frame_Mbuttons = QtWidgets.QFrame(self.frame_fundo)
        self.frame_Mbuttons.setMaximumSize(QtCore.QSize(10, 850))
        self.frame_Mbuttons.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.426, stop:0 rgba(0, 121, 182, 255), stop:0.732955 rgba(255, 255, 255, 228));\n"
"}")
        self.frame_Mbuttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_Mbuttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Mbuttons.setObjectName("frame_Mbuttons")

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_Mbuttons)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.frame_buttons = QtWidgets.QFrame(self.frame_Mbuttons)
        self.frame_buttons.setMaximumSize(QtCore.QSize(200, 150))
        self.frame_buttons.setStyleSheet("background-color: rgb(255, 255, 255,0.0);")
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_buttons)
        self.verticalLayout.setContentsMargins(10, 25, 0, 6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.btn_taxa = QtWidgets.QPushButton(self.frame_buttons)
        self.btn_taxa.setMaximumSize(QtCore.QSize(200, 100))
        self.btn_taxa.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(158, 199, 226, 255), stop:0.761364 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/button/taxa_crime.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_taxa.setIcon(icon1)
        self.btn_taxa.setIconSize(QtCore.QSize(35, 35))
        self.btn_taxa.setObjectName("btn_taxa")

        self.verticalLayout.addWidget(self.btn_taxa)

        self.btn_ocorrencias = QtWidgets.QPushButton(self.frame_buttons)
        self.btn_ocorrencias.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_ocorrencias.setMaximumSize(QtCore.QSize(200, 100))
        self.btn_ocorrencias.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(158, 199, 226, 255), stop:0.761364 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/button/ocorrencias.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ocorrencias.setIcon(icon2)
        self.btn_ocorrencias.setIconSize(QtCore.QSize(35, 35))
        self.btn_ocorrencias.setObjectName("btn_ocorrencias")

        self.verticalLayout.addWidget(self.btn_ocorrencias, 0, QtCore.Qt.AlignLeft)

        self.btn_policia = QtWidgets.QPushButton(self.frame_buttons)
        self.btn_policia.setMaximumSize(QtCore.QSize(200, 100))
        self.btn_policia.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(158, 199, 226, 255), stop:0.761364 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/button/policia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_policia.setIcon(icon3)
        self.btn_policia.setIconSize(QtCore.QSize(35, 35))
        self.btn_policia.setObjectName("btn_policia")

        self.verticalLayout.addWidget(self.btn_policia)
        self.verticalLayout_6.addWidget(self.frame_buttons)

        self.frame_button_regiao = QtWidgets.QFrame(self.frame_Mbuttons)
        self.frame_button_regiao.setMaximumSize(QtCore.QSize(0, 0))
        self.frame_button_regiao.setStyleSheet("background-color: rgb(255, 255, 255,0.0);")
        self.frame_button_regiao.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_button_regiao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_button_regiao.setObjectName("frame_button_regiao")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_button_regiao)
        self.verticalLayout_5.setContentsMargins(10, 25, 0, 6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.btn_pesquisaRegiao = QtWidgets.QPushButton(self.frame_button_regiao)
        self.btn_pesquisaRegiao.setMaximumSize(QtCore.QSize(0, 0))
        self.btn_pesquisaRegiao.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(158, 199, 226, 255), stop:0.761364 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/button/seta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pesquisaRegiao.setIcon(icon4)
        self.btn_pesquisaRegiao.setIconSize(QtCore.QSize(30, 30))
        self.btn_pesquisaRegiao.setObjectName("btn_pesquisaRegiao")

        self.verticalLayout_5.addWidget(self.btn_pesquisaRegiao)

        self.frame_pesquisaRegiao = QtWidgets.QFrame(self.frame_button_regiao)
        self.frame_pesquisaRegiao.setMaximumSize(QtCore.QSize(0, 0))
        self.frame_pesquisaRegiao.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_pesquisaRegiao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pesquisaRegiao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pesquisaRegiao.setObjectName("frame_pesquisaRegiao")

        self.comboBox_natureza = QtWidgets.QComboBox(self.frame_pesquisaRegiao)
        self.comboBox_natureza.setGeometry(QtCore.QRect(10, 30, 171, 21))
        self.comboBox_natureza.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_natureza.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_natureza.setObjectName("comboBox_natureza")

        self.label_natureza = QtWidgets.QLabel(self.frame_pesquisaRegiao)
        self.label_natureza.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.label_natureza.setStyleSheet("background-color: transparent;")
        self.label_natureza.setObjectName("label_natureza")

        self.label_ano = QtWidgets.QLabel(self.frame_pesquisaRegiao)
        self.label_ano.setGeometry(QtCore.QRect(10, 60, 111, 21))
        self.label_ano.setStyleSheet("background-color: transparent;")
        self.label_ano.setObjectName("label_ano")

        self.comboBox_ano = QtWidgets.QComboBox(self.frame_pesquisaRegiao)
        self.comboBox_ano.setGeometry(QtCore.QRect(10, 80, 171, 21))
        self.comboBox_ano.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_ano.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_ano.setObjectName("comboBox_ano")

        self.btn_regiao = QtWidgets.QPushButton(self.frame_pesquisaRegiao)
        self.btn_regiao.setGeometry(QtCore.QRect(50, 110, 81, 71))
        self.btn_regiao.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-bottom: 2px solid;\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.506, stop:0 rgba(0, 0, 0, 185), stop:1 rgba(255, 255, 255, 210));\n"
"\n"
"}")
        self.btn_regiao.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/button/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_regiao.setIcon(icon5)
        self.btn_regiao.setIconSize(QtCore.QSize(80, 80))
        self.btn_regiao.setObjectName("btn_regiao")

        self.verticalLayout_5.addWidget(self.frame_pesquisaRegiao)
        self.verticalLayout_6.addWidget(self.frame_button_regiao)

        self.frame_buttonPrevisao = QtWidgets.QFrame(self.frame_Mbuttons)
        self.frame_buttonPrevisao.setMaximumSize(QtCore.QSize(200, 300))
        self.frame_buttonPrevisao.setStyleSheet("background-color: rgb(255, 255, 255,0.0);")
        self.frame_buttonPrevisao.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_buttonPrevisao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttonPrevisao.setObjectName("frame_buttonPrevisao")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_buttonPrevisao)
        self.verticalLayout_4.setContentsMargins(10, 25, 0, 6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.btn_previsaoRegiao = QtWidgets.QPushButton(self.frame_buttonPrevisao)
        self.btn_previsaoRegiao.setMaximumSize(QtCore.QSize(0, 0))
        self.btn_previsaoRegiao.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(158, 199, 226, 255), stop:0.761364 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.btn_previsaoRegiao.setIcon(icon4)
        self.btn_previsaoRegiao.setIconSize(QtCore.QSize(30, 30))
        self.btn_previsaoRegiao.setObjectName("btn_previsaoRegiao")
        self.verticalLayout_4.addWidget(self.btn_previsaoRegiao)

        self.frame_previsao = QtWidgets.QFrame(self.frame_buttonPrevisao)
        self.frame_previsao.setMaximumSize(QtCore.QSize(0, 400))
        self.frame_previsao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_previsao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_previsao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_previsao.setObjectName("frame_previsao")

        self.label_regressao = QtWidgets.QLabel(self.frame_previsao)
        self.label_regressao.setGeometry(QtCore.QRect(30, 10, 151, 21))
        self.label_regressao.setStyleSheet("background-color: transparent;")
        self.label_regressao.setObjectName("label_regressao")

        self.label_CidadePrevisao = QtWidgets.QLabel(self.frame_previsao)
        self.label_CidadePrevisao.setGeometry(QtCore.QRect(20, 60, 151, 21))
        self.label_CidadePrevisao.setStyleSheet("background-color: transparent;")
        self.label_CidadePrevisao.setObjectName("label_cidadePrevisao")

        self.comboBox_previsaoCidade = QtWidgets.QComboBox(self.frame_previsao)
        self.comboBox_previsaoCidade.setGeometry(QtCore.QRect(10, 80, 182, 21))
        self.comboBox_previsaoCidade.setMaximumSize(QtCore.QSize(200, 21))
        self.comboBox_previsaoCidade.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_previsaoCidade.setObjectName("comboBox_previsaoCidade")
        
        self.label_previsaoNatureza = QtWidgets.QLabel(self.frame_previsao)
        self.label_previsaoNatureza .setGeometry(QtCore.QRect(20, 110, 151, 21))
        self.label_previsaoNatureza .setStyleSheet("background-color: transparent;")
        self.label_previsaoNatureza .setObjectName("label_previsaoNatureza")

        self.comboBox_previsaoNatureza = QtWidgets.QComboBox(self.frame_previsao)
        self.comboBox_previsaoNatureza.setGeometry(QtCore.QRect(10, 130, 182, 21))
        self.comboBox_previsaoNatureza.setMaximumSize(QtCore.QSize(300, 21))
        self.comboBox_previsaoNatureza.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_previsaoNatureza.setObjectName("comboBox_previsaoNatureza")


        self.btn_previsao = QtWidgets.QPushButton(self.frame_previsao)
        self.btn_previsao.setGeometry(QtCore.QRect(50, 180, 71, 61))
        self.btn_previsao.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-bottom: 2px solid;\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.506, stop:0 rgba(0, 0, 0, 227), stop:0.818182 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.btn_previsao.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/button/olho.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_previsao.setIcon(icon6)
        self.btn_previsao.setIconSize(QtCore.QSize(55, 55))
        self.btn_previsao.setObjectName("btn_previsao")

        self.frame_erroPrevisao = QtWidgets.QFrame(self.frame_previsao)
        self.frame_erroPrevisao.setGeometry(QtCore.QRect(10, -10, 170, 40))
        self.frame_erroPrevisao.setMaximumSize(QtCore.QSize(400, 60))
        self.frame_erroPrevisao.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_erroPrevisao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_erroPrevisao.setObjectName("frame_label_erro")

        self.label_errorPrevisao = QtWidgets.QLabel(self.frame_erroPrevisao)
        self.label_errorPrevisao.setGeometry(QtCore.QRect(0, 0, 170, 40))
        self.label_errorPrevisao.setMaximumSize(QtCore.QSize(350, 41))
        self.label_errorPrevisao.setStyleSheet("QLabel{\n"
"image: url(:/logo/quadroT.png);\n"
"    background-color: rgb(226, 75, 0);\n"
"}")
        self.label_errorPrevisao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_errorPrevisao.setObjectName("label_error")

        self.btn_xprevisao = QtWidgets.QPushButton(self.frame_erroPrevisao)
        self.btn_xprevisao.setGeometry(QtCore.QRect(140, 10, 35, 20))
        self.btn_xprevisao.setMaximumSize(QtCore.QSize(150, 100))
        self.btn_xprevisao.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 0, 0);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.0568182 rgba(255, 255, 255, 178), stop:0.193182 rgba(223, 223, 223, 248), stop:0.335227 rgba(245, 245, 245, 255), stop:0.573864 rgba(230, 230, 230, 255), stop:0.823864 rgba(235, 235, 235, 255), stop:0.965909 rgba(249, 249, 249, 255));\n"
"\n"
"}")
        self.btn_xprevisao.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/button/marca-x (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_xprevisao.setIcon(icon9)
        self.btn_xprevisao.setIconSize(QtCore.QSize(35, 35))
        self.btn_xprevisao.setObjectName("btn_x")

        self.verticalLayout_4.addWidget(self.frame_previsao)
        self.verticalLayout_6.addWidget(self.frame_buttonPrevisao)
        self.horizontalLayout.addWidget(self.frame_Mbuttons)

        self.frame_fundoMapa = QtWidgets.QFrame(self.frame_fundo)
        self.frame_fundoMapa.setMinimumSize(QtCore.QSize(690, 656))
        self.frame_fundoMapa.setMaximumSize(QtCore.QSize(690, 656))
        self.frame_fundoMapa.setStyleSheet("")
        self.frame_fundoMapa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_fundoMapa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fundoMapa.setObjectName("frame_fundoMapa")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_fundoMapa)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.frame_mapa = QtWidgets.QFrame(self.frame_fundoMapa)
        self.frame_mapa.setMaximumSize(QtCore.QSize(1, 656))
        self.frame_mapa.setStyleSheet("QFrame{\n"
"image: url(:/mapa/mapaE_sp.png);\n"
"background-color: transparent;\n"
"\n"
"}")
        self.frame_mapa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_mapa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mapa.setObjectName("frame_mapa")

        self.btn_baixadaSantista = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_baixadaSantista.setGeometry(QtCore.QRect(510, 420, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_baixadaSantista.setFont(font)
        self.btn_baixadaSantista.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_baixadaSantista.setText("")
        self.btn_baixadaSantista.setIconSize(QtCore.QSize(35, 35))
        self.btn_baixadaSantista.setAutoRepeat(False)
        self.btn_baixadaSantista.setObjectName("btn_baixadaSantista")

        self.btn_capital = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_capital.setGeometry(QtCore.QRect(520, 380, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_capital.setFont(font)
        self.btn_capital.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_capital.setText("")
        self.btn_capital.setIconSize(QtCore.QSize(35, 35))
        self.btn_capital.setAutoRepeat(False)
        self.btn_capital.setObjectName("btn_registro")

        self.btn_sorocaba = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_sorocaba.setGeometry(QtCore.QRect(370, 400, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_sorocaba.setFont(font)
        self.btn_sorocaba.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_sorocaba.setText("")
        self.btn_sorocaba.setIconSize(QtCore.QSize(35, 35))
        self.btn_sorocaba.setAutoRepeat(False)
        self.btn_sorocaba.setObjectName("btn_sorocaba")

        self.btn_marilia = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_marilia.setGeometry(QtCore.QRect(220, 280, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_marilia.setFont(font)
        self.btn_marilia.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_marilia.setText("")
        self.btn_marilia.setIconSize(QtCore.QSize(35, 35))
        self.btn_marilia.setAutoRepeat(False)
        self.btn_marilia.setObjectName("btn_marilia")

        self.btn_presidentePrudente = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_presidentePrudente.setGeometry(QtCore.QRect(100, 270, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_presidentePrudente.setFont(font)
        self.btn_presidentePrudente.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_presidentePrudente.setText("")
        self.btn_presidentePrudente.setIconSize(QtCore.QSize(35, 35))
        self.btn_presidentePrudente.setAutoRepeat(False)
        self.btn_presidentePrudente.setObjectName("btn_presidentePrudente")

        self.btn_aracatuba = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_aracatuba.setGeometry(QtCore.QRect(170, 190, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_aracatuba.setFont(font)
        self.btn_aracatuba.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_aracatuba.setText("")
        self.btn_aracatuba.setIconSize(QtCore.QSize(35, 35))
        self.btn_aracatuba.setAutoRepeat(False)
        self.btn_aracatuba.setObjectName("btn_aracatuba")

        self.btn_saoJoseRioPreto = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_saoJoseRioPreto.setGeometry(QtCore.QRect(240, 150, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_saoJoseRioPreto.setFont(font)
        self.btn_saoJoseRioPreto.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_saoJoseRioPreto.setText("")
        self.btn_saoJoseRioPreto.setIconSize(QtCore.QSize(35, 35))
        self.btn_saoJoseRioPreto.setAutoRepeat(False)
        self.btn_saoJoseRioPreto.setObjectName("btn_saoJoseRioPreto")

        self.btn_barretos = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_barretos.setGeometry(QtCore.QRect(330, 150, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_barretos.setFont(font)
        self.btn_barretos.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_barretos.setText("")
        self.btn_barretos.setIconSize(QtCore.QSize(35, 35))
        self.btn_barretos.setAutoRepeat(False)
        self.btn_barretos.setObjectName("btn_barretos")

        self.btn_franca = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_franca.setGeometry(QtCore.QRect(410, 140, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_franca.setFont(font)
        self.btn_franca.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_franca.setText("")
        self.btn_franca.setIconSize(QtCore.QSize(35, 35))
        self.btn_franca.setAutoRepeat(False)
        self.btn_franca.setObjectName("btn_franca")

        self.btn_ribeiraoPreto = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_ribeiraoPreto.setGeometry(QtCore.QRect(410, 200, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_ribeiraoPreto.setFont(font)
        self.btn_ribeiraoPreto.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_ribeiraoPreto.setText("")
        self.btn_ribeiraoPreto.setIconSize(QtCore.QSize(35, 35))
        self.btn_ribeiraoPreto.setAutoRepeat(False)
        self.btn_ribeiraoPreto.setObjectName("btn_ribeiraoPreto")

        self.btn_saoJoaoBoaVista = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_saoJoaoBoaVista.setGeometry(QtCore.QRect(470, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_saoJoaoBoaVista.setFont(font)
        self.btn_saoJoaoBoaVista.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_saoJoaoBoaVista.setText("")
        self.btn_saoJoaoBoaVista.setIconSize(QtCore.QSize(35, 35))
        self.btn_saoJoaoBoaVista.setAutoRepeat(False)
        self.btn_saoJoaoBoaVista.setObjectName("btn_saoJoaoBoaVista")

        self.btn_piracicaba = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_piracicaba.setGeometry(QtCore.QRect(420, 300, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_piracicaba.setFont(font)
        self.btn_piracicaba.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_piracicaba.setText("")
        self.btn_piracicaba.setIconSize(QtCore.QSize(35, 35))
        self.btn_piracicaba.setAutoRepeat(False)
        self.btn_piracicaba.setObjectName("btn_piracicaba")

        self.btn_bauru = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_bauru.setGeometry(QtCore.QRect(320, 300, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_bauru.setFont(font)
        self.btn_bauru.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_bauru.setText("")
        self.btn_bauru.setIconSize(QtCore.QSize(35, 35))
        self.btn_bauru.setAutoRepeat(False)
        self.btn_bauru.setObjectName("btn_bauru")

        self.btn_araraquara = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_araraquara.setGeometry(QtCore.QRect(360, 240, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_araraquara.setFont(font)
        self.btn_araraquara.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_araraquara.setText("")
        self.btn_araraquara.setIconSize(QtCore.QSize(35, 35))
        self.btn_araraquara.setAutoRepeat(False)
        self.btn_araraquara.setObjectName("btn_araraquara")

        self.btn_campinas = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_campinas.setGeometry(QtCore.QRect(480, 330, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_campinas.setFont(font)
        self.btn_campinas.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_campinas.setText("")
        self.btn_campinas.setIconSize(QtCore.QSize(35, 35))
        self.btn_campinas.setAutoRepeat(False)
        self.btn_campinas.setObjectName("btn_campinas")

        self.btn_taubate = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_taubate.setGeometry(QtCore.QRect(590, 350, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_taubate.setFont(font)
        self.btn_taubate.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_taubate.setText("")
        self.btn_taubate.setIconSize(QtCore.QSize(35, 35))
        self.btn_taubate.setAutoRepeat(False)
        self.btn_taubate.setObjectName("btn_taubate")

        self.btn_grande_sp = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_grande_sp.setGeometry(QtCore.QRect(500, 380, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_grande_sp.setFont(font)
        self.btn_grande_sp.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"color: rgb(255, 255, 255,0.0);\n"
"border-radius:12px solid;\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 135, 203);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"image: url(:/logo/logo_datasets.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(199, 199, 199);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_grande_sp.setText("")
        self.btn_grande_sp.setIconSize(QtCore.QSize(35, 35))
        self.btn_grande_sp.setAutoRepeat(False)
        self.btn_grande_sp.setObjectName("btn_grande_sp")

        self.frame_conection = QtWidgets.QFrame(self.frame_mapa)
        self.frame_conection.setGeometry(QtCore.QRect(40, 520, 0, 150))
        self.frame_conection.setMaximumSize(QtCore.QSize(600, 600))
        self.frame_conection.setStyleSheet("QFrame{\n"
"image: url(:/logo/conection.png);\n"        
"background-color: transparent;\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"\n"
"}")
        self.frame_conection.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_conection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_conection.setObjectName("frame_conection2")

        self.btn_dataset = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_dataset.setGeometry(QtCore.QRect(30,560, 0, 100))
        self.btn_dataset.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-bottom: 2px solid;\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.0511364 rgba(0, 0, 0, 253), stop:0.5625 rgba(22, 110, 174, 248), stop:0.880682 rgba(22, 110, 174, 248), stop:1 rgba(255, 255, 255, 248));\n"
"\n"
"}")
        self.btn_dataset.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/logo/logo_datasets.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_dataset.setIcon(icon7)
        self.btn_dataset.setIconSize(QtCore.QSize(55, 55))
        self.btn_dataset.setObjectName("btn_dataset")


        self.frame_resultadoPrevisao = QtWidgets.QFrame(self.frame_mapa)
        self.frame_resultadoPrevisao.setGeometry(QtCore.QRect(260, 530, 0, 121))
        self.frame_resultadoPrevisao.setMaximumSize(QtCore.QSize(350, 121))
        self.frame_resultadoPrevisao.setStyleSheet("image: url(:/logo/quadroT.png);\n"
"background-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius: 10px;")
        self.frame_resultadoPrevisao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_resultadoPrevisao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_resultadoPrevisao.setObjectName("frame_resultadoPrevisao")

        self.label_resuPrevisao = QtWidgets.QLabel(self.frame_resultadoPrevisao)
        self.label_resuPrevisao.setGeometry(QtCore.QRect(30, 10, 231, 21))
        self.label_resuPrevisao.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_resuPrevisao.setObjectName("label_resuPrevisao")

        self.label_ano2021 = QtWidgets.QLabel(self.frame_resultadoPrevisao)
        self.label_ano2021.setGeometry(QtCore.QRect(30, 30, 71, 21))
        self.label_ano2021.setObjectName("label_ano2021")

        self.label_ano2022 = QtWidgets.QLabel(self.frame_resultadoPrevisao)
        self.label_ano2022.setGeometry(QtCore.QRect(120, 30, 71, 21))
        self.label_ano2022.setObjectName("label_ano2022")

        self.label_ano2023 = QtWidgets.QLabel(self.frame_resultadoPrevisao)
        self.label_ano2023.setGeometry(QtCore.QRect(210, 30, 71, 21))
        self.label_ano2023.setObjectName("label_ano2023")

        self.label_resultadoAno1 = QtWidgets.QLabel(self.frame_resultadoPrevisao)
        self.label_resultadoAno1.setGeometry(QtCore.QRect(30, 50, 71, 21))
        self.label_resultadoAno1.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.label_resultadoAno1.setObjectName("label_resultadoAno1")

        self.label_resultadoAno2 = QtWidgets.QLabel(self.frame_resultadoPrevisao)
        self.label_resultadoAno2.setGeometry(QtCore.QRect(120, 50, 71, 21))
        self.label_resultadoAno2.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.label_resultadoAno2.setObjectName("label_resultadoAno2")

        self.label_resultadoAno3 = QtWidgets.QLabel(self.frame_resultadoPrevisao)
        self.label_resultadoAno3.setGeometry(QtCore.QRect(210, 50, 71, 21))
        self.label_resultadoAno3.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.label_resultadoAno3.setObjectName("label_resultadoAno3")

        self.label_nivelConfianca = QtWidgets.QLabel(self.frame_resultadoPrevisao)
        self.label_nivelConfianca.setGeometry(QtCore.QRect(30, 90, 111, 21))
        self.label_nivelConfianca.setStyleSheet("background-color: transparent;")
        self.label_nivelConfianca.setObjectName("label_nivelConfianca")

        self.label_resuConfianca = QtWidgets.QLabel(self.frame_resultadoPrevisao)
        self.label_resuConfianca.setGeometry(QtCore.QRect(150, 80, 120, 41))
        self.label_resuConfianca.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.label_resuConfianca.setObjectName("label_resuConfianca")

        self.btn_baixadaSantista.raise_()
        self.btn_capital.raise_()
        self.btn_sorocaba.raise_()
        self.btn_marilia.raise_()
        self.btn_presidentePrudente.raise_()
        self.btn_aracatuba.raise_()
        self.btn_saoJoseRioPreto.raise_()
        self.btn_barretos.raise_()
        self.btn_franca.raise_()
        self.btn_ribeiraoPreto.raise_()
        self.btn_saoJoaoBoaVista.raise_()
        self.btn_piracicaba.raise_()
        self.btn_bauru.raise_()
        self.btn_araraquara.raise_()
        self.btn_campinas.raise_()
        self.btn_taubate.raise_()
        self.btn_grande_sp.raise_()
        self.frame_conection.raise_()
        self.btn_dataset.raise_()
        self.frame_resultadoPrevisao.raise_()

        self.verticalLayout_2.addWidget(self.frame_mapa)
        self.horizontalLayout.addWidget(self.frame_fundoMapa)

        self.frame_noticias_2 = QtWidgets.QFrame(self.frame_fundo)
        self.frame_noticias_2.setMaximumSize(QtCore.QSize(290, 700))
        self.frame_noticias_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_noticias_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_noticias_2.setObjectName("frame_noticias_2")

        self.frame_noticias = QtWidgets.QFrame(self.frame_noticias_2)
        self.frame_noticias.setGeometry(QtCore.QRect(0, 0, 271, 671))
        self.frame_noticias.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_noticias.setMaximumSize(QtCore.QSize(290, 680))
        self.frame_noticias.setStyleSheet("background-color: rgb(255, 255, 255,0.0);")
        self.frame_noticias.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_noticias.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_noticias.setObjectName("frame_noticias")

        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_noticias)
        self.verticalLayout_7.setContentsMargins(10, 25, 0, 6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.frame_noticia1 = QtWidgets.QFrame(self.frame_noticias)
        self.frame_noticia1.setMinimumSize(QtCore.QSize(0, 250))
        self.frame_noticia1.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_noticia1.setStyleSheet("image: url(:/logo/noticia1.png);")
        self.frame_noticia1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_noticia1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_noticia1.setObjectName("frame_noticia1")
        self.shadow3.setBlurRadius(25)
        self.shadow3.setOffset(-5,10)
        self.frame_noticia1.setGraphicsEffect(self.shadow3)

        self.btn_noticia1 = QtWidgets.QPushButton(self.frame_noticia1)
        self.btn_noticia1.setGeometry(QtCore.QRect(50, 180, 151, 25))
        self.btn_noticia1.setMaximumSize(QtCore.QSize(200, 100))
        self.btn_noticia1.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.965909, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 109, 180, 255));\n"
"border:none;\n"
"border-radius: 10px;\n"
"image: url(:/logo/quadroT.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qconicalgradient(cx:1, cy:0.0170455, angle:0, stop:0 rgba(164, 162, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.btn_noticia1.setIconSize(QtCore.QSize(35, 35))
        self.btn_noticia1.setObjectName("btn_noticia1")

        self.verticalLayout_7.addWidget(self.frame_noticia1)
        self.frame_noticia2 = QtWidgets.QFrame(self.frame_noticias)
        self.frame_noticia2.setMinimumSize(QtCore.QSize(0, 250))
        self.frame_noticia2.setMaximumSize(QtCore.QSize(16777215, 250))
        self.frame_noticia2.setStyleSheet("image: url(:/logo/noticia2 (2).png);")
        self.frame_noticia2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_noticia2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_noticia2.setObjectName("frame_noticia2")
        self.shadow4.setBlurRadius(25)
        self.shadow4.setOffset(-5,10)
        self.frame_noticia2.setGraphicsEffect(self.shadow4)

        self.btn_noticia2 = QtWidgets.QPushButton(self.frame_noticia2)
        self.btn_noticia2.setGeometry(QtCore.QRect(60, 170, 151, 25))
        self.btn_noticia2.setMaximumSize(QtCore.QSize(200, 100))
        self.btn_noticia2.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.965909, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 109, 180, 255));\n"
"border:none;\n"
"border-radius: 10px;\n"
"image: url(:/logo/quadroT.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qconicalgradient(cx:1, cy:0.0170455, angle:0, stop:0 rgba(164, 162, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.btn_noticia2.setIconSize(QtCore.QSize(35, 35))
        self.btn_noticia2.setObjectName("btn_noticia2")

        self.verticalLayout_7.addWidget(self.frame_noticia2)

        self.frame_noticia3 = QtWidgets.QFrame(self.frame_noticias)
        self.frame_noticia3.setMinimumSize(QtCore.QSize(0, 250))
        self.frame_noticia3.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_noticia3.setStyleSheet("image: url(:/logo/noticia3.png);")
        self.frame_noticia3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_noticia3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_noticia3.setObjectName("frame_noticia3")
        self.shadow5.setBlurRadius(25)
        self.shadow5.setOffset(-5,10)
        self.frame_noticia3.setGraphicsEffect(self.shadow5)

        self.btn_noticia3 = QtWidgets.QPushButton(self.frame_noticia3)
        self.btn_noticia3.setGeometry(QtCore.QRect(70, 170, 151, 25))
        self.btn_noticia3.setMaximumSize(QtCore.QSize(200, 100))
        self.btn_noticia3.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.965909, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(0, 109, 180, 255));\n"
"border:none;\n"
"border-radius: 10px;\n"
"image: url(:/logo/quadroT.png);\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qconicalgradient(cx:1, cy:0.0170455, angle:0, stop:0 rgba(164, 162, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.btn_noticia3.setIconSize(QtCore.QSize(35, 35))
        self.btn_noticia3.setObjectName("btn_noticia3")

        self.verticalLayout_7.addWidget(self.frame_noticia3)
        self.horizontalLayout.addWidget(self.frame_noticias_2)

        self.frame_lista = QtWidgets.QFrame(self.frame_fundo)
        self.frame_lista.setMaximumSize(QtCore.QSize(1, 670))
        self.frame_lista.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_lista.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_lista.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_lista.setObjectName("frame_lista")

        self.label_icon_sp = QtWidgets.QLabel(self.frame_lista)
        self.label_icon_sp.setGeometry(QtCore.QRect(20, 20, 51, 31))
        self.label_icon_sp.setMaximumSize(QtCore.QSize(51, 31))
        self.label_icon_sp.setStyleSheet("QLabel{\n"
"image: url(:/logo/bandeira_sp.png);\n"
"    background-color: rgb(255, 255, 255,0.0);\n"
"}")
        self.label_icon_sp.setText("")
        self.label_icon_sp.setObjectName("label_icon_sp")
        self.label_estado = QtWidgets.QLabel(self.frame_lista)
        self.label_estado.setGeometry(QtCore.QRect(90, 30, 141, 16))
        self.label_estado.setMaximumSize(QtCore.QSize(141, 16))
        self.label_estado.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_estado.setObjectName("label_estado")
        self.label_Municipio = QtWidgets.QLabel(self.frame_lista)
        self.label_Municipio.setGeometry(QtCore.QRect(20, 130, 81, 31))
        self.label_Municipio.setMaximumSize(QtCore.QSize(81, 31))
        self.label_Municipio.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_Municipio.setObjectName("label_Municipio")
        self.comboBox_Municipio = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_Municipio.setGeometry(QtCore.QRect(20, 170, 251, 21))
        self.comboBox_Municipio.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_Municipio.setObjectName("comboBox_Municipio")

        self.label_busca = QtWidgets.QLabel(self.frame_lista)
        self.label_busca.setGeometry(QtCore.QRect(20, 210, 91, 16))
        self.label_busca.setMaximumSize(QtCore.QSize(91, 16))
        self.label_busca.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_busca.setObjectName("label_busca")
        self.comboBox_TipoBusca = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_TipoBusca.setGeometry(QtCore.QRect(20, 240, 251, 21))
        self.comboBox_TipoBusca.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_TipoBusca.setObjectName("comboBox_TipoBusca")
        
        self.btn_buscar_grafico = QtWidgets.QPushButton(self.frame_lista)
        self.btn_buscar_grafico.setGeometry(QtCore.QRect(60, 280, 150, 43))
        self.btn_buscar_grafico.setMaximumSize(QtCore.QSize(150, 100))
        self.btn_buscar_grafico.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-bottom: 2px solid;\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.0568182 rgba(255, 255, 255, 178), stop:0.193182 rgba(223, 223, 223, 248), stop:0.335227 rgba(245, 245, 245, 255), stop:0.573864 rgba(230, 230, 230, 255), stop:0.823864 rgba(235, 235, 235, 255), stop:0.965909 rgba(249, 249, 249, 255));\n"
"\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/button/icon_grafico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_buscar_grafico.setIcon(icon8)
        self.btn_buscar_grafico.setIconSize(QtCore.QSize(35, 35))
        self.btn_buscar_grafico.setObjectName("btn_buscar_grafico")

        self.frame_erro = QtWidgets.QFrame(self.frame_mapa)
        self.frame_erro.setGeometry(QtCore.QRect(100, 30, 400, 60))
        self.frame_erro.setMaximumSize(QtCore.QSize(400, 60))
        self.frame_erro.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_erro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_erro.setObjectName("frame_label_erro")

        self.label_error2 = QtWidgets.QLabel(self.frame_erro)
        self.label_error2.setGeometry(QtCore.QRect(0, 0, 350, 40))
        self.label_error2.setMaximumSize(QtCore.QSize(350, 41))
        self.label_error2.setStyleSheet("QLabel{\n"
"image: url(:/logo/quadroT.png);\n"
"    background-color: rgb(226, 75, 0);\n"
"}")
        self.label_error2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error2.setObjectName("label_error")

        self.btn_x2 = QtWidgets.QPushButton(self.frame_erro)
        self.btn_x2.setGeometry(QtCore.QRect(300, 10, 35, 20))
        self.btn_x2.setMaximumSize(QtCore.QSize(150, 100))
        self.btn_x2.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 0, 0);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.0568182 rgba(255, 255, 255, 178), stop:0.193182 rgba(223, 223, 223, 248), stop:0.335227 rgba(245, 245, 245, 255), stop:0.573864 rgba(230, 230, 230, 255), stop:0.823864 rgba(235, 235, 235, 255), stop:0.965909 rgba(249, 249, 249, 255));\n"
"\n"
"}")
        self.btn_x2.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/button/marca-x (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_x2.setIcon(icon9)
        self.btn_x2.setIconSize(QtCore.QSize(35, 35))
        self.btn_x2.setObjectName("btn_x")

        self.frame_label_erro = QtWidgets.QFrame(self.frame_lista)
        self.frame_label_erro.setGeometry(QtCore.QRect(30, -10, 250, 41))
        self.frame_label_erro.setMaximumSize(QtCore.QSize(250, 41))
        self.frame_label_erro.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_erro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_erro.setObjectName("frame_label_erro")

        self.label_error = QtWidgets.QLabel(self.frame_label_erro)
        self.label_error.setGeometry(QtCore.QRect(0, 0, 250, 40))
        self.label_error.setMaximumSize(QtCore.QSize(250, 41))
        self.label_error.setStyleSheet("QLabel{\n"
"image: url(:/logo/quadroT.png);\n"
"    background-color: rgb(226, 75, 0);\n"
"}")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")

        self.btn_x = QtWidgets.QPushButton(self.frame_label_erro)
        self.btn_x.setGeometry(QtCore.QRect(210, 10, 31, 20))
        self.btn_x.setMaximumSize(QtCore.QSize(150, 100))
        self.btn_x.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 0, 0);\n"
"border:none;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.0568182 rgba(255, 255, 255, 178), stop:0.193182 rgba(223, 223, 223, 248), stop:0.335227 rgba(245, 245, 245, 255), stop:0.573864 rgba(230, 230, 230, 255), stop:0.823864 rgba(235, 235, 235, 255), stop:0.965909 rgba(249, 249, 249, 255));\n"
"\n"
"}")
        self.btn_x.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/button/marca-x (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_x.setIcon(icon9)
        self.btn_x.setIconSize(QtCore.QSize(35, 35))
        self.btn_x.setObjectName("btn_x")

        self.label_duasCidades = QtWidgets.QLabel(self.frame_lista)
        self.label_duasCidades.setGeometry(QtCore.QRect(30, 400, 231, 16))
        self.label_duasCidades.setMaximumSize(QtCore.QSize(300, 16))
        self.label_duasCidades.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 87 10pt \"Arial Black\";\n"
"")
        self.label_duasCidades.setObjectName("label_duasCidades")
        self.comboBox_primeiraCidade = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_primeiraCidade.setGeometry(QtCore.QRect(20, 450, 251, 21))
        self.comboBox_primeiraCidade.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_primeiraCidade.setObjectName("comboBox_primeiraCidade")

        self.label_primeiraCidade = QtWidgets.QLabel(self.frame_lista)
        self.label_primeiraCidade.setGeometry(QtCore.QRect(20, 430, 100, 21))
        self.label_primeiraCidade.setMaximumSize(QtCore.QSize(100, 21))
        self.label_primeiraCidade.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_primeiraCidade.setAlignment(QtCore.Qt.AlignCenter)
        self.label_primeiraCidade.setObjectName("label_primeiraCidade")
        self.label_segundaCidade = QtWidgets.QLabel(self.frame_lista)
        self.label_segundaCidade.setGeometry(QtCore.QRect(20, 480, 100, 21))
        self.label_segundaCidade.setMaximumSize(QtCore.QSize(100, 21))
        self.label_segundaCidade.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_segundaCidade.setAlignment(QtCore.Qt.AlignCenter)
        self.label_segundaCidade.setObjectName("label_segundaCidade")
        self.comboBox_segundaCidade = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_segundaCidade.setGeometry(QtCore.QRect(20, 500, 251, 21))
        self.comboBox_segundaCidade.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_segundaCidade.setObjectName("comboBox_segundaCidade")
        
        self.comboBox_comparacao = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_comparacao.setGeometry(QtCore.QRect(20, 570, 251, 21))
        self.comboBox_comparacao.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_comparacao.setObjectName("comboBox_comparacao")
        
        self.label_comparacao = QtWidgets.QLabel(self.frame_lista)
        self.label_comparacao.setGeometry(QtCore.QRect(20, 550, 120, 21))
        self.label_comparacao.setMaximumSize(QtCore.QSize(120, 21))
        self.label_comparacao.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_comparacao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_comparacao.setObjectName("label_comparacao")

        self.btn_buscar2Cidades = QtWidgets.QPushButton(self.frame_lista)
        self.btn_buscar2Cidades.setGeometry(QtCore.QRect(50, 610, 181, 43))
        self.btn_buscar2Cidades.setMaximumSize(QtCore.QSize(200, 100))
        self.btn_buscar2Cidades.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-bottom: 2px solid;\n"
"border-bottom-color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.0568182 rgba(255, 255, 255, 178), stop:0.193182 rgba(223, 223, 223, 248), stop:0.335227 rgba(245, 245, 245, 255), stop:0.573864 rgba(230, 230, 230, 255), stop:0.823864 rgba(235, 235, 235, 255), stop:0.965909 rgba(249, 249, 249, 255));\n"
"\n"
"}")
        self.btn_buscar2Cidades.setIcon(icon8)
        self.btn_buscar2Cidades.setIconSize(QtCore.QSize(35, 35))
        self.btn_buscar2Cidades.setObjectName("btn_buscar2Cidades")

        self.label_umaCidade = QtWidgets.QLabel(self.frame_lista)
        self.label_umaCidade.setGeometry(QtCore.QRect(40, 100, 231, 16))
        self.label_umaCidade.setMaximumSize(QtCore.QSize(300, 16))
        self.label_umaCidade.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 87 10pt \"Arial Black\";\n"
"")
        self.label_umaCidade.setObjectName("label_umaCidade")
        self.horizontalLayout.addWidget(self.frame_lista)
        self.verticalLayout_3.addWidget(self.frame_fundo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #esconder o frame de erro
        self.frame_label_erro.hide()
        self.frame_erro.hide()
        self.frame_erroPrevisao.hide()

        #acao do buttons menu
        self.button_Mdataset.clicked.connect(lambda: Ui_MainWindow.toggleMenu(self,300,True))
        self.btn_ocorrencias.clicked.connect(self.ocorrencia)
        self.btn_taxa.clicked.connect(self.taxa_crime)
        self.btn_policia.clicked.connect(self.policia_prod)
        #acao do buttons regiao (1= ocorrencias/ 2 = taxa crime/)
        self.btn_grande_sp.clicked.connect(lambda: Ui_MainWindow.lista(self,"Grande São Paulo (exclui a Capital)","Grande S�o Paulo (exclui a Capital)"))
        self.btn_campinas.clicked.connect(lambda: Ui_MainWindow.lista(self,"Campinas","Campinas"))
        self.btn_aracatuba.clicked.connect(lambda: Ui_MainWindow.lista(self,"Araçatuba","0"))
        self.btn_araraquara.clicked.connect(lambda: Ui_MainWindow.lista(self,"0","0"))
        self.btn_baixadaSantista.clicked.connect(lambda: Ui_MainWindow.lista(self,"Santos","Santos"))
        self.btn_barretos.clicked.connect(lambda: Ui_MainWindow.lista(self,"0","0"))
        self.btn_bauru.clicked.connect(lambda: Ui_MainWindow.lista(self,"Bauru","Bauru"))
        self.btn_franca.clicked.connect(lambda: Ui_MainWindow.lista(self,"0","0"))
        self.btn_marilia.clicked.connect(lambda: Ui_MainWindow.lista(self,"0","0"))
        self.btn_piracicaba.clicked.connect(lambda: Ui_MainWindow.lista(self,"Piracicaba","0"))
        self.btn_capital.clicked.connect(lambda: Ui_MainWindow.lista(self,"Capital","Capital"))
        self.btn_barretos.clicked.connect(lambda: Ui_MainWindow.lista(self,"",""))
        self.btn_presidentePrudente.clicked.connect(lambda: Ui_MainWindow.lista(self,"Presidente Prudente","0"))
        self.btn_saoJoaoBoaVista.clicked.connect(lambda: Ui_MainWindow.lista(self,"0","0"))
        self.btn_saoJoseRioPreto.clicked.connect(lambda: Ui_MainWindow.lista(self,"São José do Rio Preto","0"))
        self.btn_ribeiraoPreto.clicked.connect(lambda: Ui_MainWindow.lista(self,"Ribeirão Preto","Ribeir�o Preto"))
        self.btn_sorocaba.clicked.connect(lambda: Ui_MainWindow.lista(self,"Sorocaba","Sorocaba"))
        #acao do buttons lista
        self.btn_x.clicked.connect(lambda: self.frame_label_erro.hide())
        self.btn_x2.clicked.connect(lambda: self.frame_erro.hide())
        self.btn_xprevisao.clicked.connect(lambda:self.frame_erroPrevisao.hide())

        self.btn_buscar_grafico.clicked.connect(self.opcao_selecionada)
        self.btn_buscar2Cidades.clicked.connect(self.duas_cidades)

        #acao do buttons dataset com lista previsao e lista regiao
        self.btn_dataset.clicked.connect(self.dataset)
        self.btn_previsao.clicked.connect(self.previsao)

        self.btn_noticia1.clicked.connect(lambda: Ui_MainWindow.linkNoticia(self,1))
        self.btn_noticia2.clicked.connect(lambda: Ui_MainWindow.linkNoticia(self,2))
        self.btn_noticia3.clicked.connect(lambda: Ui_MainWindow.linkNoticia(self,3))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_Mdataset.setText(_translate("MainWindow", "MENU DATASET"))
        self.label_Criminalidade.setText(_translate("MainWindow", "Dataset Criminalidade"))
        self.btn_taxa.setText(_translate("MainWindow", "Taxa de Criminalidade"))
        self.btn_ocorrencias.setText(_translate("MainWindow", " Ocorrencias "))
        self.btn_policia.setText(_translate("MainWindow", "Produtividade Policial"))
        self.btn_pesquisaRegiao.setText(_translate("MainWindow", "PESQUISAR SOBRE A REGIAO:"))
        self.label_natureza.setText(_translate("MainWindow", "NATUREZA: "))
        self.label_ano.setText(_translate("MainWindow", "ANO:"))
        self.btn_previsaoRegiao.setText(_translate("MainWindow", "PREVISAO SOBRE A REGIAO:"))
        self.label_regressao.setText(_translate("MainWindow", "APLICAR PREVISAO"))
        self.label_CidadePrevisao.setText(_translate("MainWindow", "CIDADE: "))
        self.label_previsaoNatureza.setText(_translate("MainWindow", "NATUREZA: "))
        self.label_resuPrevisao.setText(_translate("MainWindow", "resultado previsto:"))
        self.label_ano2021.setText(_translate("MainWindow", "ANO DE 2021"))
        self.label_ano2022.setText(_translate("MainWindow", "ANO DE 2022"))
        self.label_ano2023.setText(_translate("MainWindow", "ANO DE 2023"))
        self.label_resultadoAno1.setText(_translate("MainWindow", ""))
        self.label_resultadoAno2.setText(_translate("MainWindow", ""))
        self.label_resultadoAno3.setText(_translate("MainWindow", ""))
        self.label_nivelConfianca.setText(_translate("MainWindow", "NIVEL DE CONFIANCA:"))
        self.label_resuConfianca.setText(_translate("MainWindow", ""))
        self.btn_noticia1.setText(_translate("MainWindow", "Acessar noticia"))
        self.btn_noticia2.setText(_translate("MainWindow", "Acessar noticia"))
        self.btn_noticia3.setText(_translate("MainWindow", "Acessar noticia"))
        self.label_estado.setText(_translate("MainWindow", "ESTADO DE SAO PAULO"))
        self.label_Municipio.setText(_translate("MainWindow", "Municipio:"))
        self.label_busca.setText(_translate("MainWindow", "Tipo de Busca:"))
        self.btn_buscar_grafico.setText(_translate("MainWindow", "Buscar Grafico"))
        self.label_error.setText(_translate("MainWindow", "ERRO ao selecionar!"))
        self.label_error2.setText(_translate("MainWindow", "NAO possui DADOS para regiao selecionada!"))
        self.label_errorPrevisao.setText(_translate("MainWindow", "ERRO ao selecionar!"))
        self.label_duasCidades.setText(_translate("MainWindow", "GRAFICO PARA DUAS CIDADES:"))
        self.label_primeiraCidade.setText(_translate("MainWindow", "primeira cidade:"))
        self.label_segundaCidade.setText(_translate("MainWindow", "Segunda cidade:"))
        self.label_comparacao.setText(_translate("MainWindow", "Tipo de comparacao:"))
        self.btn_buscar2Cidades.setText(_translate("MainWindow", "Buscar por Comparacao"))
        self.label_umaCidade.setText(_translate("MainWindow", "GRAFICO PARA UMA CIDADE:"))
import images_sistema


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
