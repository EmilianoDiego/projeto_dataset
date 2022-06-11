from ipaddress import v4_int_to_packed
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
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
    #arquivo das tabelas        
    pasta = "/home/usuario/python_study/novo_sistema/"  
    tabela = ""
    tabelaOcorrencia = "tabela_ocorrencia_alterada.csv"
    tabelaTaxa = "tabela_dados_taxaCrime.csv"
    tabelaPolicia = "tabela_dados_policia.csv"
    region ="0"

#efeitos de sombra sobre os frames
    shadow = QGraphicsDropShadowEffect()
    shadow2 = QGraphicsDropShadowEffect()
    shadow3 = QGraphicsDropShadowEffect()
    shadow4 = QGraphicsDropShadowEffect()
    shadow5 = QGraphicsDropShadowEffect()
    shadow6 = QGraphicsDropShadowEffect()
    shadowlabelError = QGraphicsDropShadowEffect()
    shadowlabelMapa = QGraphicsDropShadowEffect()
    shadowframePrevisao = QGraphicsDropShadowEffect()
    shadowGraficos = QGraphicsDropShadowEffect()      


    #metodo de etilo do button do menu princioal,para fixar quando escolhido
    def style(self,valor):
            #para ocorrencia
            if(valor == 1 ):
                buttonMarca1 = ""
                buttonMarca2 = "0.0"
                buttonMarca3 = "0.0"
            #para taxa 
            elif(valor == 2):
                buttonMarca1 = "0.0"
                buttonMarca2 = ""
                buttonMarca3 = "0.0"
            #para policia    
            elif(valor == 3):                
                buttonMarca1 = "0.0"
                buttonMarca2 = "0.0"
                buttonMarca3 = ""
            #mudancas no style do button                       
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
    #metodo para tabela de ocorrencia quando for selecionada chamar as animacoes e preparar para alimentar os comobox
    def ocorrencia(self):
            self.style(1)
            if self.tabWidget_lista.width() > 100:
                    self.animacaoLista()
                    self.limparDados()
            self.tabela = self.tabelaOcorrencia
            if self.tabWidget_lista.width() == 1 & self.frame_mapa.width() == 1 :
                    self.mapaSp()
            if self.frame_ranking2.width() > 0:
                self.animacaoRanking()
                self.limparDados()        

    def taxa_crime(self):
            self.style(2)
            if self.tabWidget_lista.width() > 100:
                    self.animacaoLista()
                    self.limparDados()
            self.tabela = self.tabelaTaxa
            if self.tabWidget_lista.width() == 1 & self.frame_mapa.width() == 1 :
                    self.mapaSp()
            if self.frame_ranking2.width() > 0:
                self.animacaoRanking()
                self.limparDados()    

    def policia_prod(self):
            self.style(3)
            if self.tabWidget_lista.width() > 100:
                    self.animacaoLista()
                    self.limparDados()
            self.tabela = self.tabelaPolicia
            if self.tabWidget_lista.width() == 1 & self.frame_mapa.width() == 1 :
                    self.mapaSp()
            if self.frame_ranking2.width() > 0:
                self.animacaoRanking()
                self.limparDados()

#metodo para direcionar os links da noticia para o site
    def linkNoticia(self,noticia):
            if(noticia == 1):
                wb.open("https://www.ssp.sp.gov.br/LeNoticia.aspx?ID=54131")
            elif(noticia == 2):
                wb.open("https://www.ssp.sp.gov.br/noticia/LeFotos.aspx?id=19709")
            else:
                wb.open("https://www.ssp.sp.gov.br/noticia/LeFotos.aspx?id=19711")


#metodo para criar os ranking das cidades na tabela
    def ranking(self):
            
        if (self.comboBox_rankingN.currentText() == "Selecione") or (self.region == "0"):
            self.frame_erroRanking.show()
            #tabela ocorrencia apresentar o ranking das cidades
        elif self.tabela == self.tabelaOcorrencia:
                naturezaR = self.comboBox_rankingN.currentText()
                self.frame_erroRanking.hide()
                data = pd.read_csv(self.pasta + self.tabelaOcorrencia , encoding="utf-8")
                data = data[(data.Regiao == self.region) & (data.Ano == 2020) & (data.Natureza == naturezaR)]
                data = data[["Total","Cidade"]]
                dat = data.sort_values(by = ["Total"],ascending=False)
                #criar lista para ranking ocorrencia
                listTotalRo=[]
                listCidadeRo=[]
                for chave, item in enumerate(dat["Cidade"]):
                        listCidadeRo.insert(chave, item)
                for chave2, item2 in enumerate(dat["Total"]):
                        listTotalRo.insert(chave2, item2)
                self.label_nomeRegiaoR.setText((self.region))
                self.label_cidadeP1.setText((str(listCidadeRo[0]))) 
                self.label_cidadeP2.setText((str(listCidadeRo[1])))
                self.label_cidadeP3.setText((str(listCidadeRo[2])))
                self.label_cidadeP4.setText((str(listCidadeRo[3]))) 
                self.label_cidadeP5.setText((str(listCidadeRo[4])))

                self.label_total1.setText((str(listTotalRo[0])))
                self.label_total2.setText((str(listTotalRo[1])))
                self.label_total3.setText((str(listTotalRo[2])))
                self.label_total4.setText((str(listTotalRo[3])))
                self.label_total5.setText((str(listTotalRo[4])))     

    #tabela policia apresentar o ranking das cidades
        elif self.tabela == self.tabelaPolicia:
                naturezaR = self.comboBox_rankingN.currentText()
                data = pd.read_csv(self.pasta + self.tabelaPolicia , encoding="utf-8")
                data = data[(data.Regiao == self.region) & (data.Ano == 2020) & (data.Natureza == naturezaR)]
                data = data[["Total","Cidade"]]
                dat = data.sort_values(by = ["Total"],ascending=False)
                #criar lista para ranking policia
                listTotalRp=[]
                listCidadeRp=[]
                for chave, item in enumerate(dat["Cidade"]):
                        listCidadeRp.insert(chave, item)
                for chave2, item2 in enumerate(dat["Total"]):
                        listTotalRp.insert(chave2, item2)
                self.label_nomeRegiaoR.setText((self.region))
                self.label_cidadeP1.setText((str(listCidadeRp[0]))) 
                self.label_cidadeP2.setText((str(listCidadeRp[1])))
                self.label_cidadeP3.setText((str(listCidadeRp[2])))
                self.label_cidadeP4.setText((str(listCidadeRp[3]))) 
                self.label_cidadeP5.setText((str(listCidadeRp[4])))

                self.label_total1.setText((str(listTotalRp[0])))
                self.label_total2.setText((str(listTotalRp[1])))
                self.label_total3.setText((str(listTotalRp[2])))
                self.label_total4.setText((str(listTotalRp[3])))
                self.label_total5.setText((str(listTotalRp[4])))

#tabela taxa apresentar o ranking das cidades
        elif self.tabela == self.tabelaTaxa:
                naturezaR = self.comboBox_rankingN.currentText()
                self.frame_erroRanking.hide()
                dataRt = pd.read_csv(self.pasta +self.tabelaTaxa, encoding="utf-8")

                dataRt = dataRt[(dataRt.Regiao == self.region) & (dataRt.Ano == 2020) & (dataRt[naturezaR])]
                dataRt = dataRt[[naturezaR,"Cidade"]]
                dataRt = dataRt.sort_values(by = [naturezaR],ascending=False)
                #criar lista para ranking taxa
                listTotalRt=[]
                listCidadeRt=[]
                for chaveRt, item in enumerate(dataRt["Cidade"]):
                        listCidadeRt.insert(chaveRt, item)
                        print(item)
                for chaveRt2, item2 in enumerate(dataRt[naturezaR]):
                        listTotalRt.insert(chaveRt2, item2)
                #aplicar controle para quando quandidade de cidade na regiao for menor que 5
                if(len(listCidadeRt)<5):
                        while(len(listCidadeRt) < 6):
                                indicador = 3
                                listCidadeRt.insert(indicador,"nao possui")
                                listTotalRt.insert(indicador, 0)
                                indicador = indicador +1

                self.label_nomeRegiaoR.setText((self.region))
                self.label_cidadeP1.setText((str(listCidadeRt[0]))) 
                self.label_cidadeP2.setText((str(listCidadeRt[1])))
                self.label_cidadeP3.setText((str(listCidadeRt[2])))
                self.label_cidadeP4.setText((str(listCidadeRt[3]))) 
                self.label_cidadeP5.setText((str(listCidadeRt[4])))

                self.label_total1.setText((str(listTotalRt[0])))
                self.label_total2.setText((str(listTotalRt[1])))
                self.label_total3.setText((str(listTotalRt[2])))
                self.label_total4.setText((str(listTotalRt[3])))
                self.label_total5.setText((str(listTotalRt[4])))                     
                    

        #metodo para previsao
    def previsao(self):
        if (self.comboBox_MunicipioP.currentText() == "Selecione") or (self.comboBox_naturezaP.currentText() == "Selecione"):
            self.frame_erroPrevisao.show()  
        #tabela ocorrencias
        elif self.tabela == self.tabelaOcorrencia:
                self.frame_erroPrevisao.hide()
                #buscar cidade e natureza selecionada
                cidadeP = self.comboBox_MunicipioP.currentText()
                naturezaP = self.comboBox_naturezaP.currentText() 
                #busca o dados da tabela            
                dataset = pd.read_csv(self.pasta + self.tabela, encoding="utf-8")
                #limpar tabela de valores NA
                dataset = dataset.fillna(value= 0)    
                #selecionar colunas necessarias para coleta de dados de total e ano atraves da cidade escolhida e o tipo de natureza escolhido
                dataset = dataset[(dataset.Cidade == cidadeP) & (dataset.Natureza == naturezaP)]
                #coletar dados da coluna
                dataset = dataset[["Total","Ano"]]
                #construir uma lista para cada coluna total e ano, com dados da coluna da tabela
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
                #aqui o periodo passado e do ano de 2013 ate 2020
                X = np.array(lista[13:20]).reshape((-1,1))
                y= np.array(lista2[13:20])
                #uso da biblioteca sklearn para uso e aplicacao de pretica de machine learnig
                #Dividindo os dados em Treino e Teste
                from sklearn.model_selection import train_test_split
                X_train,  X_test, y_train, y_test = train_test_split(X,y, test_size=0.5, random_state=50)
                # criar modelo preditor com o uso de regressao linear
                modeloPreditor = LinearRegression()
                # iniciar aprendizado para o modelo preditor
                modeloPreditor.fit(X_train, y_train)
                #captura informacao sobre o coeficiente 
                coeficiente = pd.DataFrame(modeloPreditor.coef_)
                # realiza predições com os dados de teste
                y_predictions = modeloPreditor.predict(X_test)
                #construir graficos para regressao linear sobre os dados da tabela
                ax = sns.lmplot(x= "Ano", y = "Total", data = dataset)
                #configurar tamanho
                ax.fig.set_size_inches(6,3)
                ax.fig.suptitle("reta de regressao - Ano X total", fontsize = 18, y=1.02)
                ax.set_xlabels("Ano", fontsize =14)
                ax.set_ylabels("Total", fontsize = 14)
                plt.show()
                #construir grafico para o periodo de predicao
                plt.scatter(X,y, color="red")
                plt.plot(X_test, y_predictions, color ="blue", linewidth=5)
                plt.show()
                #passar os dados dos proximos anos apartir d 2020 para prever
                prever =np.array([2021,2022,2023]).reshape((-1,1))
                y_predictions = modeloPreditor.predict(prever)
                #criar lista de predicao para 
                listaPredicao =[]
                for w,item in enumerate(y_predictions):
                        #if criado para correcao de valores negativos
                        if(item < 0):
                                item = 0
                                listaPredicao.insert(w,item)
                        else:        
                                listaPredicao.insert(w,item)
                #passar valores para o label text           
                self.label_resultadoAno1.setText(( str(int(listaPredicao[0]))))
                self.label_resultadoAno2.setText(( str(int(listaPredicao[1]))))
                self.label_resultadoAno3.setText(( str(int(listaPredicao[2]))))
                #extrair valores rquadrado
                self.label_resuConfianca.setText(( "{:.2f}".format(modeloPreditor.score(X, y)))+"%")
        #tabela policia
        elif self.tabela == self.tabelaPolicia:  
                self.frame_erroPrevisao.hide()
                cidadeP = self.comboBox_MunicipioP.currentText()
                naturezaP = self.comboBox_naturezaP.currentText() 
                #busca o dados da tabela csv             
                dataset = pd.read_csv(self.pasta + self.tabela, encoding="utf-8")
                dataset = dataset.fillna(value= 0)    

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

                X = np.array(lista[13:20]).reshape((-1,1))
                y= np.array(lista2[13:20])

                from sklearn.model_selection import train_test_split

                X_train,  X_test, y_train, y_test = train_test_split(X,y, test_size=0.5, random_state=50)

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
                        #if criado para correcao de valores negativos
                        if(item < 0):
                                item = 0
                                listaPredicao2.insert(w,item)
                        else:        
                                listaPredicao2.insert(w,item)
                        
                self.label_resultadoAno1.setText(( str(int(listaPredicao2[0]))))
                self.label_resultadoAno2.setText(( str(int(listaPredicao2[1]))))
                self.label_resultadoAno3.setText(( str(int(listaPredicao2[2]))))
                self.label_resuConfianca.setText(( "{:.2f}".format(modeloPreditor.score(X, y)))+"%") 
        #tabela taxa criminalidade
        elif self.tabela == self.tabelaTaxa:
                self.frame_erroPrevisao.hide()
                cidadeP = self.comboBox_MunicipioP.currentText()
                naturezaP = self.comboBox_naturezaP.currentText()

                dataset3 = pd.read_csv(self.pasta + self.tabelaTaxa, encoding="utf-8")
                dataset3 = dataset3.fillna(value =0)
                dataset3 = dataset3[(dataset3.Cidade == cidadeP)]
                dataset3 = dataset3[[naturezaP,"Ano"]]

                #criar lista para aplicar no modelo os ultimos 4 anos
                listaTaxa = []
                for i , item in enumerate(dataset3["Ano"]):
                        listaTaxa.insert(i, item)
                listaTaxa2 = []
                for y , item in enumerate(dataset3[naturezaP]):
                        listaTaxa2.insert(y, item)
                #passar os dados da lista em forma de matriz para as variaveis X e Y
                #aqui o periodo passado e do ano

                X = np.array(listaTaxa[14:22]).reshape((-1,1))
                y= np.array(listaTaxa2[14:22])                          

                from sklearn.model_selection import train_test_split
                X_train,  X_test, y_train, y_test = train_test_split(X,y, test_size=0.5, random_state=40)
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
                        #if criado para correcao de valores negativos
                        if(item < 0):
                                item = 0
                                listaPredicao3.insert(w,item)
                        else:        
                                listaPredicao3.insert(w,item)
                self.label_resultadoAno1.setText(( str(int(listaPredicao3[0]))))
                self.label_resultadoAno2.setText(( str(int(listaPredicao3[1]))))
                self.label_resultadoAno3.setText(( str(int(listaPredicao3[2]))))
                self.label_resuConfianca.setText(( "{:.2f}".format(modeloPreditor.score(X, y)))+"%")
          
    
    #metodo de chamada para animacao do mapa
    def mapaSp(self):
            #pegar tamanho do mapa atual 
            width = self.frame_mapa.width()
            #valor para extender o tamanho do mapa
            maxExtend = 650
            #valor padra
            standard =1

            if width == 1:
                widthExtended = maxExtend
            else:
                widthExtended = standard
            #aplicar a animacao para movimento de width    
            self.animation = QPropertyAnimation(self.frame_mapa, b"maximumWidth")
            #passar valor para tempo de animacao
            self.animation.setDuration(800)
            #passar valor inicia de width em que o frame esta
            self.animation.setStartValue(width)
            #passar valor final para o frame ficar
            self.animation.setEndValue(widthExtended)
            #inciar a animacao
            self.animation.start()

    #metodo para animacao da lista de graficos  (frame tabWidget_lista)    
    def animacaoLista(self):    
        height = self.tabWidget_lista.width()
        height2 = self.frame_fundoNoticias.width()
        maxExtend = 290
        standard =1
        noticiatamanho = 0
        #set max width   
        if height == 1:
                widthExtended = maxExtend
                noticiatamanho = 0
        else:
                widthExtended = standard
                noticiatamanho = 300
        #animacao somente tabwidget
        self.animation = QPropertyAnimation(self.tabWidget_lista, b"maximumWidth")
        self.animation.setDuration(600)
        self.animation.setStartValue(height)
        self.animation.setEndValue(widthExtended)
        #animacao somente para o frame de noticia
        self.animation2 = QPropertyAnimation(self.frame_fundoNoticias, b"maximumWidth")
        self.animation2.setDuration(600)
        self.animation2.setStartValue(height2)
        self.animation2.setEndValue(noticiatamanho)
        #criar animacao de grupo paralelo para unir as duas animacoes e acontecer ao mesmo tempo
        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.animation)
        self.anim_group.addAnimation(self.animation2)
        self.anim_group.start()      



    #metodo de controle do movimento do menu principal
    def toggleMenu(self,maxWidth, enable):
        if enable:  
            width = self.frame_Mbuttons.width()
            maxExtend = maxWidth
            standard =10
            if width == 10:
                widthExtended = maxExtend
            else:
                widthExtended = standard

        self.animation = QPropertyAnimation(self.frame_Mbuttons, b"maximumWidth")
        self.animation.setDuration(600)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.start()

    #metodo para aparesentar a lista de previsao
    def animacaoRanking(self):
        if(self.frame_Mbuttons.width() == 10):
                self.toggleMenu(300,True)    
        width2 = self.frame_ranking2.width()
        maxExtend = 350
        standard =0
        if width2 == 0:
                widthExtended = maxExtend
        else:
                widthExtended = standard

        self.animationdata = QPropertyAnimation(self.frame_ranking2, b"maximumWidth")
        self.animationdata.setDuration(600)
        self.animationdata.setStartValue(width2)
        self.animationdata.setEndValue(widthExtended)
        self.animationdata.start()              

#animacao para o button azul que acessa a lista de previsao
    def animacaoDataset(self):
            #aplicar efeito de sombra
            effect = QGraphicsOpacityEffect(self.btn_dataset)
            self.btn_dataset.setGraphicsEffect(effect)
            #aplicar animacao de efeito  transparente no button    
            self.anim_effectDataset = QPropertyAnimation(effect, b"opacity")
            self.anim_effectDataset.setStartValue(0)
            self.anim_effectDataset.setEndValue(1)
            self.anim_effectDataset.setDuration(2000)
            #aplicar animacao de tamanho do button    
            self.a = QPropertyAnimation(self.btn_dataset, b"size")
            self.a.setEndValue(QSize(100, 100))
            self.a.setDuration(400)
            #aplicar animacao para retornar ao tamanho original do button    
            self.b = QPropertyAnimation(self.btn_dataset, b"size")
            self.b.setEndValue(QSize(70, 70))
            self.b.setDuration(400) 
            #aplicar animacao paralela
            self.anim_groupDataset = QParallelAnimationGroup()
            self.anim_groupDataset.addAnimation(self.anim_effectDataset)
            self.anim_groupDataset.addAnimation(self.a)
            #aplicar animacao sequencial para grupo de animacao paralelo e animacao comum
            self.anim_sequencialDataset = QSequentialAnimationGroup()    
            self.anim_sequencialDataset.addAnimation(self.anim_groupDataset)
            self.anim_sequencialDataset.addAnimation(self.b)
            self.anim_sequencialDataset.start()  

        #metodo para limpar dados do combox e ranking
    def limparDados(self):
                self.comboBox_Municipio1.clear()
                self.comboBox_natureza1.clear()
                self.comboBox_primeiraCidade.clear()
                self.comboBox_segundaCidade.clear()
                self.comboBox_comparacao.clear()
                self.comboBox_MunicipioP.clear() 
                self.comboBox_naturezaP.clear() 
                self.comboBox_rankingN.clear()

                #limpar dados da lista de ranking
                self.label_nomeRegiaoR.setText((""))
                self.label_cidadeP1.setText(("")) 
                self.label_cidadeP2.setText((""))
                self.label_cidadeP3.setText((""))
                self.label_cidadeP4.setText(("")) 
                self.label_cidadeP5.setText((""))
                self.label_total1.setText((""))
                self.label_total2.setText((""))
                self.label_total3.setText((""))
                self.label_total4.setText((""))
                self.label_total5.setText((""))

    #metodo para alimentar a lista e prencher os combox com dados da regiao selecionada
    def lista(self,regiao,regiao2):
        #chamar animacao do button azul    
        self.animacaoDataset()
        #verificar a posicao do frame para fechar as tabelas caso esteja aberta
        if self.frame_ranking2.width() > 0:
                self.animacaoRanking()
                self.limparDados()
        #identificar regiao para tabela ocorrencias
        if self.tabela == self.tabelaOcorrencia:
                if regiao == "0":
                        #apresentar frame de erro
                        self.frame_label_erro_2.show()
                else:
                        self.frame_label_erro_2.hide()       
                self.region = regiao          
                self.limparDados()   
                #preencher a lista com cidade e tipo de natureza de acordo com a regiao
                file = pd.read_csv(self.pasta +self.tabelaOcorrencia, encoding="utf-8")
                nature = file[(file.Cidade == "São Paulo") & (file.Ano == 2010)]
                listaNatureza=["Selecione"]
                for y, item2 in enumerate(nature["Natureza"]):
                        listaNatureza.insert(y, item2)   
                cidades =file[(file.Regiao == regiao) & (file.Ano == 2010) & (file.Natureza == "HOMICÍDIO DOLOSO")]
                listaCidade =["Selecione"]
                for i, item in enumerate(cidades["Cidade"]):
                        listaCidade.insert(i,item)

        #identificar regiao para tabela taxa crime
        elif self.tabela == self.tabelaTaxa: 
                if regiao2 == "0":
                        self.frame_label_erro_2.show()
                else:
                        self.frame_label_erro_2.hide()                   
                self.region = regiao2
                self.limparDados()  
                #preencher a lista com cidade e tipo de natureza de acordo com a regiao
                file = pd.read_csv(self.pasta +self.tabelaTaxa, encoding="utf-8")
                cidades =file[(file.Regiao == regiao2) & (file.Ano == 2010)]
                listaCidade =["Selecione"]
                for i, item in enumerate(cidades["Cidade"]):
                        listaCidade.insert(i,item)
                #preencher lista de natureza para tabela taxa crime , devido ao formato da tabela
                listaNatureza=["Homicídio Doloso por 100 mil habitantes",
                                "Furto por 100 mil habitantes","Roubo por 100 mil habitantes",
                                "Furto e Roubo de Veículo por 100 mil habitantes",
                                "Furto por 100 mil veículos",
                                "Roubo por 100 mil veículos",
                                "Furto e Roubo de Veículo por 100 mil veículos","Selecione"]

        #identificar regiao para tabela produtividade policial
        elif self.tabela == self.tabelaPolicia: 
                if regiao == "0":
                        self.frame_label_erro_2.show()
                else:
                        self.frame_label_erro_2.hide()           
                self.region = regiao           
                self.limparDados()   
                #preencher a lista com cidade e tipo de natureza de acordo com a regiao
                file = pd.read_csv(self.pasta +self.tabelaPolicia, encoding="utf-8")
                nature = file[(file.Cidade == "São Paulo") & (file.Ano == 2010)]
                listaNatureza=["selecione"]
                for y, item2 in enumerate(nature["Natureza"]):
                        listaNatureza.insert(y, item2)   
                cidades =file[(file.Regiao == regiao) & (file.Ano == 2010) & (file.Natureza == "OCORRÊNCIAS DE PORTE DE ENTORPECENTES")]
                listaCidade =["Selecione"]
                for i, item in enumerate(cidades["Cidade"]):
                        listaCidade.insert(i,item)                                                
        #alimentar o combox com dados coletados
        self.comboBox_natureza1.addItems(list(reversed(listaNatureza)))  
        self.comboBox_Municipio1.addItems(list(reversed(listaCidade)))
        self.comboBox_primeiraCidade.addItems(list(reversed(listaCidade)))  
        self.comboBox_segundaCidade.addItems(list(reversed(listaCidade)))
        self.comboBox_comparacao.addItems(list(reversed(listaNatureza)))      
        self.comboBox_MunicipioP.addItems(list(reversed(listaCidade)))      
        self.comboBox_naturezaP.addItems(list(reversed(listaNatureza)))  
        self.comboBox_rankingN.addItems(list(reversed(listaNatureza)))     
        self.animacaoLista()

    #metodo criado para verificar graficos de 1 cidade    
    def opcao_selecionada(self):
        #pegar dados do combox
        natureza = self.comboBox_natureza1.currentText()
        cidade = self.comboBox_Municipio1.currentText() 
        #verifica se os itens no combobox foram selecionados
        if (self.tabela == "Selecione") or (natureza == "Selecione") or (cidade == "Selecione"):
            self.frame_erroGraficos.show()

        #tabela TAXA_CRIME    
        elif self.tabela == self.tabelaTaxa:
                self.frame_erroGraficos.hide()
                dataset = pd.read_csv(self.pasta + self.tabela, encoding="utf-8")
                dados = dataset[(dataset.Cidade == cidade)].sort_values("Ano")
                lista =[]
                for i, item in enumerate(dados[natureza]):
                        lista.insert(i, item)
                #grafico 1
                #configurar o tamanho do grafico
                plt.rcParams["figure.figsize"] = (12,6)
                df = pd.DataFrame({natureza: lista}, index=dados["Ano"])
                ax = df.plot.bar(rot=0)
                plt.show()

        #tabela OCORRENCIAS_MENSAIS
        elif self.tabela == self.tabelaOcorrencia:   
            self.frame_erroGraficos.hide() 
            #busca o dados da tabela csv             
            dataset = pd.read_csv(self.pasta + self.tabela, encoding="utf-8")
            dataset = dataset.fillna(value= 0)
            #busca os dados da tabela apartir do tipo de natureza em qual cidade e pelo periodo dos anos contidos na tabela    
            dados = dataset[(dataset.Natureza == natureza) & (dataset.Cidade == cidade)].sort_values("Ano")
            #envia os dados para a construcao do grafico com matplotlib 
            # #configurar o tamanho do grafico
            plt.rcParams["figure.figsize"] = (12,6)   
            sns.barplot(x = "Ano", y="Total",data = dados, color="blue")
            plt.xticks(rotation=90)
            plt.title(natureza +" "+ cidade,fontsize = 14)
            plt.xlabel("Ano", fontsize = 10)
            plt.ylabel("numeros de:"+ natureza, fontsize = 10)
            #apresenta o grafico
            plt.show()

        #tabela POLICIA_PRODUTIVIDADE
        elif self.tabela == self.tabelaPolicia:
                self.frame_erroGraficos.hide() 
                #busca o dados da tabela csv 
                dataset = pd.read_csv(self.pasta + self.tabela, encoding="utf-8")
                #busca os dados da tabela apartir do tipo de natureza em qual cidade e pelo periodo dos anos contidos na tabela
                dados = dataset[(dataset.Cidade == cidade) & (dataset.Natureza == natureza)].sort_values("Ano")
                lista=[]
                for i, item in enumerate(dados["Total"]):
                        lista.insert(i,item)
                #grafico 1
                #configurar o tamanho do grafico
                plt.rcParams["figure.figsize"] = (12,6)
                df = pd.DataFrame({natureza: lista}, index=dados["Ano"])
                ax = df.plot.bar(rot=0)
                plt.show()  

    #metodo para comparacao de duas cidades
    def duas_cidades(self):    
        natureza = self.comboBox_comparacao.currentText()
        cidade = self.comboBox_primeiraCidade.currentText()
        cidade2 = self.comboBox_segundaCidade.currentText() 
        #verifica se os itens no combobox foram selecionados
        if (self.tabela == "Selecione") or (natureza == "Selecione") or (cidade == "Selecione") or (cidade2 == "Selecione"):
            self.frame_erroGraficos.show()
        #tabela taxa crime    
        elif self.tabela == self.tabelaTaxa:
                self.frame_erroGraficos.hide()
                dataset = pd.read_csv(self.pasta + self.tabela, encoding="utf-8")

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
                plt.rcParams["figure.figsize"] = (12,6)
                df = pd.DataFrame({natureza +" - " + cidade: lista,
                                   natureza +" - " + cidade2: lista_outra}, index=dados["Ano"])
                #grafico 1                   
                ax = df.plot.bar(rot=0)
                plt.show()
                #grafico 2
                lines = df.plot.line()
                plt.show()

        #tabela ocorrencias    
        elif self.tabela == self.tabelaOcorrencia:
                self.frame_erroGraficos.hide()
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
                plt.rcParams["figure.figsize"] = (12,6)
                df = pd.DataFrame({natureza +" - " + cidade: lista,
                                   natureza +" - " + cidade2: lista_outra}, index=dados["Ano"])
                #grafico 1                   
                ax = df.plot.bar(rot=0)
                plt.show()
                #grafico 2
                lines = df.plot.line()
                plt.show()

        #tabela tabela policia    
        elif self.tabela == self.tabelaPolicia:
                self.frame_erroGraficos.hide()
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
                plt.rcParams["figure.figsize"] = (12,6)
                df = pd.DataFrame({natureza +" - " + cidade: lista,
                                   natureza +" - " + cidade2: lista_outra}, index=dados["Ano"])
                #grafico 1                   
                df.plot.bar(rot=0)
                plt.show()
                #grafico 2
                df.plot.line()
                plt.show()                            

    

#inicio da da construcao grafica
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 848)
        MainWindow.setMaximumSize(QtCore.QSize(1250, 850))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(100, 400))
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
        self.frame_fundo.setMinimumSize(QtCore.QSize(650, 410))
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
        self.frame_buttons.setMaximumSize(QtCore.QSize(250, 150))
        self.frame_buttons.setStyleSheet("background-color: rgb(255, 255, 255,0.0);")
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_buttons)
        self.verticalLayout.setContentsMargins(10, 25, 0, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_taxa = QtWidgets.QPushButton(self.frame_buttons)
        self.btn_taxa.setMaximumSize(QtCore.QSize(250, 100))
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
        self.btn_ocorrencias.setMaximumSize(QtCore.QSize(250, 100))
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
        self.verticalLayout.addWidget(self.btn_ocorrencias)
        self.btn_policia = QtWidgets.QPushButton(self.frame_buttons)
        self.btn_policia.setMaximumSize(QtCore.QSize(250, 100))
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

        self.frame_ranking = QtWidgets.QFrame(self.frame_Mbuttons)
        self.frame_ranking.setMaximumSize(QtCore.QSize(250, 500))
        self.frame_ranking.setStyleSheet("background-color: rgb(255, 255, 255,0.0);")
        self.frame_ranking.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ranking.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ranking.setObjectName("frame_ranking")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_ranking)
        self.verticalLayout_5.setContentsMargins(10, 25, 0, 6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.frame_ranking2 = QtWidgets.QFrame(self.frame_ranking)
        self.frame_ranking2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_ranking2.setMaximumSize(QtCore.QSize(0, 500))
        self.frame_ranking2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_ranking2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ranking2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ranking2.setObjectName("frame_ranking2")
        self.shadow2.setBlurRadius(25)
        self.shadow2.setOffset(-5,10)
        self.frame_ranking2.setGraphicsEffect(self.shadow2)

        self.label_resuPrevisao_2 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_resuPrevisao_2.setGeometry(QtCore.QRect(30, 60, 171, 21))
        self.label_resuPrevisao_2.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_resuPrevisao_2.setObjectName("label_resuPrevisao_2")

        self.label_regiaoR = QtWidgets.QLabel(self.frame_ranking2)
        self.label_regiaoR.setGeometry(QtCore.QRect(20, 90, 51, 21))
        self.label_regiaoR.setObjectName("label_regiaoR")

        self.label_ano2020 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_ano2020.setGeometry(QtCore.QRect(20, 110, 131, 21))
        self.label_ano2020.setObjectName("label_ano2020")

        self.label_nomeRegiaoR = QtWidgets.QLabel(self.frame_ranking2)
        self.label_nomeRegiaoR.setGeometry(QtCore.QRect(100, 90, 111, 21))
        self.label_nomeRegiaoR.setObjectName("label_nomeRegiaoR")

        self.label_posicao1 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_posicao1.setGeometry(QtCore.QRect(10, 200, 21, 21))
        self.label_posicao1.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.label_posicao1.setObjectName("label_posicao1")
        self.label_posicao2 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_posicao2.setGeometry(QtCore.QRect(10, 240, 21, 21))
        self.label_posicao2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.label_posicao2.setObjectName("label_posicao2")
        self.label_posicao3 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_posicao3.setGeometry(QtCore.QRect(10, 280, 21, 21))
        self.label_posicao3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.label_posicao3.setObjectName("label_posicao3")
        self.label_posicao4 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_posicao4.setGeometry(QtCore.QRect(10, 320, 21, 21))
        self.label_posicao4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.label_posicao4.setObjectName("label_posicao4")
        self.label_posicao5 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_posicao5.setGeometry(QtCore.QRect(10, 360, 21, 21))
        self.label_posicao5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.label_posicao5.setObjectName("label_posicao5")
        self.label_cidadeP1 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_cidadeP1.setGeometry(QtCore.QRect(40, 200, 111, 21))
        self.label_cidadeP1.setStyleSheet("")
        self.label_cidadeP1.setObjectName("label_cidadeP1")
        self.label_cidadeP2 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_cidadeP2.setGeometry(QtCore.QRect(40, 240, 111, 21))
        self.label_cidadeP2.setStyleSheet("")
        self.label_cidadeP2.setObjectName("label_cidadeP2")
        self.label_cidadeP3 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_cidadeP3.setGeometry(QtCore.QRect(40, 280, 111, 21))
        self.label_cidadeP3.setObjectName("label_cidadeP3")
        self.label_cidadeP4 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_cidadeP4.setGeometry(QtCore.QRect(40, 320, 111, 21))
        self.label_cidadeP4.setObjectName("label_cidadeP4")
        self.label_cidadeP5 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_cidadeP5.setGeometry(QtCore.QRect(40, 360, 111, 21))
        self.label_cidadeP5.setObjectName("label_cidadeP5")

        self.comboBox_rankingN = QtWidgets.QComboBox(self.frame_ranking2)
        self.comboBox_rankingN.setGeometry(QtCore.QRect(10, 140, 211, 21))
        self.comboBox_rankingN.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_rankingN.setObjectName("comboBox_rankingN")

        self.btn_ranking = QtWidgets.QPushButton(self.frame_ranking2)
        self.btn_ranking.setGeometry(QtCore.QRect(70, 400, 91, 43))
        self.btn_ranking.setMaximumSize(QtCore.QSize(150, 100))
        self.btn_ranking.setStyleSheet("QPushButton{\n"
"background-color: rgb(236, 236, 236);\n"
"    font: 75 9pt \"MS Shell Dlg 2\";\n"
"border-bottom: 2px solid;\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/button/ranki.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ranking.setIcon(icon4)
        self.btn_ranking.setIconSize(QtCore.QSize(35, 35))
        self.btn_ranking.setObjectName("btn_ranking")

        self.label_total1 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_total1.setGeometry(QtCore.QRect(170, 200, 51, 21))
        self.label_total1.setStyleSheet("")
        self.label_total1.setObjectName("label_total1")
        self.label_total2 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_total2.setGeometry(QtCore.QRect(170, 240, 51, 21))
        self.label_total2.setStyleSheet("")
        self.label_total2.setObjectName("label_total2")
        self.label_total3 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_total3.setGeometry(QtCore.QRect(170, 280, 51, 21))
        self.label_total3.setStyleSheet("")
        self.label_total3.setObjectName("label_total3")
        self.label_total4 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_total4.setGeometry(QtCore.QRect(170, 320, 51, 21))
        self.label_total4.setStyleSheet("")
        self.label_total4.setObjectName("label_total4")
        self.label_total5 = QtWidgets.QLabel(self.frame_ranking2)
        self.label_total5.setGeometry(QtCore.QRect(170, 360, 51, 21))
        self.label_total5.setStyleSheet("")
        self.label_total5.setObjectName("label_total5")

        self.frame_erroRanking = QtWidgets.QFrame(self.frame_ranking2)
        self.frame_erroRanking.setGeometry(QtCore.QRect(0, 10, 220, 41))
        self.frame_erroRanking.setMaximumSize(QtCore.QSize(250, 41))
        self.frame_erroRanking.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_erroRanking.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_erroRanking.setObjectName("frame_erroRanking")

        self.label_erroRanking = QtWidgets.QLabel(self.frame_erroRanking)
        self.label_erroRanking.setGeometry(QtCore.QRect(7, 0, 210, 30))
        self.label_erroRanking.setMaximumSize(QtCore.QSize(210, 30))
        self.label_erroRanking.setStyleSheet("QLabel{\n"
"image: url(:/logo/quadroT.png);\n"
"    background-color: rgb(226, 75, 0);\n"
"}")
        self.label_erroRanking.setAlignment(QtCore.Qt.AlignCenter)
        self.label_erroRanking.setObjectName("label_erroRanking")

        self.btn_XerroR = QtWidgets.QPushButton(self.frame_erroRanking)
        self.btn_XerroR.setGeometry(QtCore.QRect(170, 7, 31, 20))
        self.btn_XerroR.setMaximumSize(QtCore.QSize(150, 100))
        self.btn_XerroR.setStyleSheet("QPushButton{\n"
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
        self.btn_XerroR.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/button/marca-x (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_XerroR.setIcon(icon5)
        self.btn_XerroR.setIconSize(QtCore.QSize(35, 35))
        self.btn_XerroR.setObjectName("btn_XerroR")
        self.verticalLayout_5.addWidget(self.frame_ranking2)
        self.verticalLayout_6.addWidget(self.frame_ranking)
        self.frame_espaco = QtWidgets.QFrame(self.frame_Mbuttons)
        self.frame_espaco.setMaximumSize(QtCore.QSize(250, 50))
        self.frame_espaco.setStyleSheet("background-color: rgb(255, 255, 255,0.0);")
        self.frame_espaco.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_espaco.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_espaco.setObjectName("frame_espaco")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_espaco)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_6.addWidget(self.frame_espaco)
        self.horizontalLayout.addWidget(self.frame_Mbuttons)

        self.frame_fundoMapa = QtWidgets.QFrame(self.frame_fundo)
        self.frame_fundoMapa.setMinimumSize(QtCore.QSize(650, 690))
        self.frame_fundoMapa.setMaximumSize(QtCore.QSize(650, 690))
        self.frame_fundoMapa.setStyleSheet("")
        self.frame_fundoMapa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_fundoMapa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fundoMapa.setObjectName("frame_fundoMapa")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_fundoMapa)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.frame_mapa = QtWidgets.QFrame(self.frame_fundoMapa)
        self.frame_mapa.setMaximumSize(QtCore.QSize(1, 630))
        self.frame_mapa.setStyleSheet("QFrame{\n"
"image: url(:/mapa/mapaE_sp.png);\n"
"background-color: transparent;\n"
"\n"
"}")
        self.frame_mapa.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_mapa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mapa.setObjectName("frame_mapa")
        self.btn_baixadaSantista = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_baixadaSantista.setGeometry(QtCore.QRect(470, 330, 31, 31))
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
        self.btn_registro = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_registro.setGeometry(QtCore.QRect(360, 360, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_registro.setFont(font)
        self.btn_registro.setStyleSheet("QPushButton{\n"
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
        self.btn_registro.setText("")
        self.btn_registro.setIconSize(QtCore.QSize(35, 35))
        self.btn_registro.setAutoRepeat(False)
        self.btn_registro.setObjectName("btn_registro")
        self.btn_sorocaba = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_sorocaba.setGeometry(QtCore.QRect(340, 310, 31, 31))
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
        self.btn_marilia.setGeometry(QtCore.QRect(200, 200, 31, 31))
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
        self.btn_presidentePrudente.setGeometry(QtCore.QRect(100, 190, 31, 31))
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
        self.btn_aracatuba.setGeometry(QtCore.QRect(160, 110, 31, 31))
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
        self.btn_saoJoseRioPreto.setGeometry(QtCore.QRect(230, 70, 31, 31))
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
        self.btn_barretos.setGeometry(QtCore.QRect(310, 80, 31, 31))
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
        self.btn_franca.setGeometry(QtCore.QRect(380, 60, 31, 31))
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
        self.btn_ribeiraoPreto.setGeometry(QtCore.QRect(380, 120, 31, 31))
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
        self.btn_saoJoaoBoaVista.setGeometry(QtCore.QRect(430, 170, 31, 31))
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
        self.btn_piracicaba.setGeometry(QtCore.QRect(380, 220, 31, 31))
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
        self.btn_bauru.setGeometry(QtCore.QRect(290, 220, 31, 31))
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
        self.btn_araraquara.setGeometry(QtCore.QRect(340, 170, 31, 31))
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
        self.btn_campinas.setGeometry(QtCore.QRect(440, 240, 31, 31))
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
        self.btn_taubate.setGeometry(QtCore.QRect(550, 260, 31, 31))
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
        self.btn_grande_sp.setGeometry(QtCore.QRect(460, 290, 31, 31))
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
        self.btn_dataset = QtWidgets.QPushButton(self.frame_mapa)
        self.btn_dataset.setGeometry(QtCore.QRect(70, 400, 71, 61))
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/logo/logo_datasets.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_dataset.setIcon(icon6)
        self.btn_dataset.setIconSize(QtCore.QSize(55, 55))
        self.btn_dataset.setObjectName("btn_dataset")

        self.frame_label_erro_2 = QtWidgets.QFrame(self.frame_mapa)
        self.frame_label_erro_2.setGeometry(QtCore.QRect(220, 0, 330, 41))
        self.frame_label_erro_2.setMaximumSize(QtCore.QSize(330, 41))
        self.frame_label_erro_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_erro_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_erro_2.setObjectName("frame_label_erro_2")
        self.shadowlabelMapa.setBlurRadius(25)
        self.shadowlabelMapa.setOffset(-5,10)
        self.frame_label_erro_2.setGraphicsEffect(self.shadowlabelMapa)

        self.label_error_2 = QtWidgets.QLabel(self.frame_label_erro_2)
        self.label_error_2.setGeometry(QtCore.QRect(-10, 0, 320, 40))
        self.label_error_2.setMaximumSize(QtCore.QSize(320, 40))
        self.label_error_2.setStyleSheet("QLabel{\n"
"image: url(:/logo/quadroT.png);\n"
"    background-color: rgb(226, 75, 0);\n"
"}")
        self.label_error_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error_2.setObjectName("label_error_2")
        self.btn_X_erroM = QtWidgets.QPushButton(self.frame_label_erro_2)
        self.btn_X_erroM.setGeometry(QtCore.QRect(280, 10, 31, 20))
        self.btn_X_erroM.setMaximumSize(QtCore.QSize(150, 100))
        self.btn_X_erroM.setStyleSheet("QPushButton{\n"
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
        self.btn_X_erroM.setText("")
        self.btn_X_erroM.setIcon(icon5)
        self.btn_X_erroM.setIconSize(QtCore.QSize(35, 35))
        self.btn_X_erroM.setObjectName("btn_X_erroM")
        self.verticalLayout_2.addWidget(self.frame_mapa)

        self.frame_avisos = QtWidgets.QFrame(self.frame_fundoMapa)
        self.frame_avisos.setMaximumSize(QtCore.QSize(650, 200))
        self.frame_avisos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.frame_avisos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_avisos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_avisos.setObjectName("frame_avisos")

        self.tab_listaAviso = QtWidgets.QTabWidget(self.frame_avisos)
        self.tab_listaAviso.setGeometry(QtCore.QRect(-4, -1, 651, 201))
        self.tab_listaAviso.setStyleSheet("")
        self.tab_listaAviso.setObjectName("tab_listaAviso")
        self.tab_aviso = QtWidgets.QWidget()
        self.tab_aviso.setObjectName("tab_aviso")

        self.plainTextAviso = QtWidgets.QPlainTextEdit(self.tab_aviso)
        self.plainTextAviso.setGeometry(QtCore.QRect(10, 0, 631, 171))
        self.plainTextAviso.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextAviso.setObjectName("plainTextAviso")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/button/sinal-de-aviso.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_listaAviso.addTab(self.tab_aviso, icon7, "")
        self.tab_dicas = QtWidgets.QWidget()
        self.tab_dicas.setObjectName("tab_dicas")
        self.plainTextDicas = QtWidgets.QPlainTextEdit(self.tab_dicas)
        self.plainTextDicas.setGeometry(QtCore.QRect(10, 0, 631, 171))
        self.plainTextDicas.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextDicas.setObjectName("plainTextDicas")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/button/dica.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab_listaAviso.addTab(self.tab_dicas, icon8, "")
        self.verticalLayout_2.addWidget(self.frame_avisos)
        self.horizontalLayout.addWidget(self.frame_fundoMapa)

        self.frame_fundoNoticias = QtWidgets.QFrame(self.frame_fundo)
        self.frame_fundoNoticias.setMaximumSize(QtCore.QSize(350, 700))
        self.frame_fundoNoticias.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_fundoNoticias.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fundoNoticias.setObjectName("frame_fundoNoticias")

        self.frame_noticias = QtWidgets.QFrame(self.frame_fundoNoticias)
        self.frame_noticias.setGeometry(QtCore.QRect(40, 10, 232, 680))
        self.frame_noticias.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_noticias.setMaximumSize(QtCore.QSize(300, 680))
        self.frame_noticias.setStyleSheet("background-color: rgb(255, 255, 255,0.0);")
        self.frame_noticias.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_noticias.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_noticias.setObjectName("frame_noticias")

        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_noticias)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_noticias = QtWidgets.QLabel(self.frame_noticias)
        self.label_noticias.setMaximumSize(QtCore.QSize(300, 30))
        self.label_noticias.setStyleSheet("font: 87 9pt \"Arial Black\";\n"
"")
        self.label_noticias.setObjectName("label_noticias")
        self.verticalLayout_7.addWidget(self.label_noticias)

        self.frame_noticia1 = QtWidgets.QFrame(self.frame_noticias)
        self.frame_noticia1.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_noticia1.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_noticia1.setStyleSheet("image: url(:/logo/noticia1.png);")
        self.frame_noticia1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_noticia1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_noticia1.setObjectName("frame_noticia1")
        self.shadow3.setBlurRadius(25)
        self.shadow3.setOffset(-5,10)
        self.frame_noticia1.setGraphicsEffect(self.shadow3)

        self.btn_noticia1 = QtWidgets.QPushButton(self.frame_noticia1)
        self.btn_noticia1.setGeometry(QtCore.QRect(50, 160, 151, 25))
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
        self.frame_noticia2.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_noticia2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_noticia2.setStyleSheet("image: url(:/logo/noticia2 (2).png);")
        self.frame_noticia2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_noticia2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_noticia2.setObjectName("frame_noticia2")
        self.shadow4.setBlurRadius(25)
        self.shadow4.setOffset(-5,10)
        self.frame_noticia2.setGraphicsEffect(self.shadow4)

        self.btn_noticia2 = QtWidgets.QPushButton(self.frame_noticia2)
        self.btn_noticia2.setGeometry(QtCore.QRect(50, 150, 151, 25))
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
        self.frame_noticia3.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_noticia3.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_noticia3.setStyleSheet("image: url(:/logo/noticia3.png);")
        self.frame_noticia3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_noticia3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_noticia3.setObjectName("frame_noticia3")
        self.shadow5.setBlurRadius(25)
        self.shadow5.setOffset(-5,10)
        self.frame_noticia3.setGraphicsEffect(self.shadow5)

        self.btn_noticia3 = QtWidgets.QPushButton(self.frame_noticia3)
        self.btn_noticia3.setGeometry(QtCore.QRect(50, 140, 151, 25))
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
        self.horizontalLayout.addWidget(self.frame_fundoNoticias)
        self.tabWidget_lista = QtWidgets.QTabWidget(self.frame_fundo)
        self.tabWidget_lista.setMinimumSize(QtCore.QSize(0, 680))
        self.tabWidget_lista.setMaximumSize(QtCore.QSize(1, 680))
        self.tabWidget_lista.setObjectName("tabWidget_lista")
        self.shadow = QGraphicsDropShadowEffect()  
        self.shadow.setBlurRadius(25)
        self.shadow.setOffset(-5,10)
        self.tabWidget_lista.setGraphicsEffect(self.shadow)

        self.tab_graficos = QtWidgets.QWidget()
        self.tab_graficos.setObjectName("tab_graficos")
        self.frame_lista = QtWidgets.QFrame(self.tab_graficos)
        self.frame_lista.setGeometry(QtCore.QRect(0, 0, 320, 676))
        self.frame_lista.setMinimumSize(QtCore.QSize(0, 580))
        self.frame_lista.setMaximumSize(QtCore.QSize(320, 680))
        self.frame_lista.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_lista.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_lista.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_lista.setObjectName("frame_lista")

        self.label_icon_sp = QtWidgets.QLabel(self.frame_lista)
        self.label_icon_sp.setGeometry(QtCore.QRect(10, 50, 51, 31))
        self.label_icon_sp.setMaximumSize(QtCore.QSize(51, 31))
        self.label_icon_sp.setStyleSheet("QLabel{\n"
"image: url(:/logo/bandeira_sp.png);\n"
"    background-color: rgb(255, 255, 255,0.0);\n"
"}")
        self.label_icon_sp.setText("")
        self.label_icon_sp.setObjectName("label_icon_sp")
        self.label_estado = QtWidgets.QLabel(self.frame_lista)
        self.label_estado.setGeometry(QtCore.QRect(90, 60, 141, 16))
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
        self.comboBox_Municipio1 = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_Municipio1.setGeometry(QtCore.QRect(20, 160, 251, 21))
        self.comboBox_Municipio1.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_Municipio1.setObjectName("comboBox_Municipio1")
        self.comboBox_Municipio1.addItem("")
        self.comboBox_Municipio1.addItem("")
        self.comboBox_Municipio1.addItem("")
        self.comboBox_Municipio1.addItem("")
        self.comboBox_Municipio1.addItem("")
        self.comboBox_Municipio1.addItem("")
        self.label_busca = QtWidgets.QLabel(self.frame_lista)
        self.label_busca.setGeometry(QtCore.QRect(20, 200, 91, 16))
        self.label_busca.setMaximumSize(QtCore.QSize(91, 16))
        self.label_busca.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_busca.setObjectName("label_busca")
        self.comboBox_natureza1 = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_natureza1.setGeometry(QtCore.QRect(20, 220, 251, 21))
        self.comboBox_natureza1.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_natureza1.setObjectName("comboBox_natureza1")
        self.comboBox_natureza1.addItem("")
        self.comboBox_natureza1.addItem("")
        self.comboBox_natureza1.addItem("")
        self.comboBox_natureza1.addItem("")
        self.comboBox_natureza1.addItem("")
        self.btn_buscar_1Cidade = QtWidgets.QPushButton(self.frame_lista)
        self.btn_buscar_1Cidade.setGeometry(QtCore.QRect(50, 260, 150, 43))
        self.btn_buscar_1Cidade.setMaximumSize(QtCore.QSize(150, 100))
        self.btn_buscar_1Cidade.setStyleSheet("QPushButton{\n"
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
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/button/icon_grafico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_buscar_1Cidade.setIcon(icon9)
        self.btn_buscar_1Cidade.setIconSize(QtCore.QSize(35, 35))
        self.btn_buscar_1Cidade.setObjectName("btn_buscar_1Cidade")

        self.frame_erroGraficos = QtWidgets.QFrame(self.frame_lista)
        self.frame_erroGraficos.setGeometry(QtCore.QRect(30, 0, 250, 41))
        self.frame_erroGraficos.setMaximumSize(QtCore.QSize(250, 41))
        self.frame_erroGraficos.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_erroGraficos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_erroGraficos.setObjectName("frame_erroGraficos")

        self.label_erroGraficos = QtWidgets.QLabel(self.frame_erroGraficos)
        self.label_erroGraficos.setGeometry(QtCore.QRect(-10, 0, 250, 30))
        self.label_erroGraficos.setMaximumSize(QtCore.QSize(250, 41))
        self.label_erroGraficos.setStyleSheet("QLabel{\n"
"image: url(:/logo/quadroT.png);\n"
"    background-color: rgb(226, 75, 0);\n"
"}")
        self.label_erroGraficos.setAlignment(QtCore.Qt.AlignCenter)
        self.label_erroGraficos.setObjectName("label_erroGraficos")
        self.shadowGraficos.setBlurRadius(25)
        self.shadowGraficos.setOffset(-5,10)
        self.label_erroGraficos.setGraphicsEffect(self.shadowGraficos)

        self.btn_X_erroG = QtWidgets.QPushButton(self.frame_erroGraficos)
        self.btn_X_erroG.setGeometry(QtCore.QRect(200, 5, 31, 20))
        self.btn_X_erroG.setMaximumSize(QtCore.QSize(150, 100))
        self.btn_X_erroG.setStyleSheet("QPushButton{\n"
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
        self.btn_X_erroG.setText("")
        self.btn_X_erroG.setIcon(icon5)
        self.btn_X_erroG.setIconSize(QtCore.QSize(35, 35))
        self.btn_X_erroG.setObjectName("btn_X_erroG")
        self.label_duasCidades = QtWidgets.QLabel(self.frame_lista)
        self.label_duasCidades.setGeometry(QtCore.QRect(30, 390, 231, 16))
        self.label_duasCidades.setMaximumSize(QtCore.QSize(300, 16))
        self.label_duasCidades.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 87 10pt \"Arial Black\";\n"
"")
        self.label_duasCidades.setObjectName("label_duasCidades")
        self.comboBox_primeiraCidade = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_primeiraCidade.setGeometry(QtCore.QRect(20, 440, 251, 21))
        self.comboBox_primeiraCidade.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_primeiraCidade.setObjectName("comboBox_primeiraCidade")
        self.comboBox_primeiraCidade.addItem("")
        self.comboBox_primeiraCidade.addItem("")
        self.comboBox_primeiraCidade.addItem("")
        self.comboBox_primeiraCidade.addItem("")
        self.comboBox_primeiraCidade.addItem("")
        self.comboBox_primeiraCidade.addItem("")
        self.label_primeiraCidade = QtWidgets.QLabel(self.frame_lista)
        self.label_primeiraCidade.setGeometry(QtCore.QRect(20, 420, 100, 21))
        self.label_primeiraCidade.setMaximumSize(QtCore.QSize(100, 21))
        self.label_primeiraCidade.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_primeiraCidade.setAlignment(QtCore.Qt.AlignCenter)
        self.label_primeiraCidade.setObjectName("label_primeiraCidade")
        self.label_segundaCidade = QtWidgets.QLabel(self.frame_lista)
        self.label_segundaCidade.setGeometry(QtCore.QRect(20, 470, 100, 21))
        self.label_segundaCidade.setMaximumSize(QtCore.QSize(100, 21))
        self.label_segundaCidade.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_segundaCidade.setAlignment(QtCore.Qt.AlignCenter)
        self.label_segundaCidade.setObjectName("label_segundaCidade")
        self.comboBox_segundaCidade = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_segundaCidade.setGeometry(QtCore.QRect(20, 490, 251, 21))
        self.comboBox_segundaCidade.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_segundaCidade.setObjectName("comboBox_segundaCidade")
        self.comboBox_segundaCidade.addItem("")
        self.comboBox_segundaCidade.addItem("")
        self.comboBox_segundaCidade.addItem("")
        self.comboBox_segundaCidade.addItem("")
        self.comboBox_segundaCidade.addItem("")
        self.comboBox_segundaCidade.addItem("")
        self.comboBox_comparacao = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_comparacao.setGeometry(QtCore.QRect(20, 540, 251, 21))
        self.comboBox_comparacao.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_comparacao.setObjectName("comboBox_comparacao")
        self.comboBox_comparacao.addItem("")
        self.comboBox_comparacao.addItem("")
        self.comboBox_comparacao.addItem("")
        self.comboBox_comparacao.addItem("")
        self.comboBox_comparacao.addItem("")
        self.comboBox_comparacao.addItem("")
        self.label_comparacao = QtWidgets.QLabel(self.frame_lista)
        self.label_comparacao.setGeometry(QtCore.QRect(20, 520, 190, 21))
        self.label_comparacao.setMaximumSize(QtCore.QSize(190, 21))
        self.label_comparacao.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_comparacao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_comparacao.setObjectName("label_comparacao")
        self.btn_buscar2Cidades = QtWidgets.QPushButton(self.frame_lista)
        self.btn_buscar2Cidades.setGeometry(QtCore.QRect(50, 580, 181, 43))
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
        self.btn_buscar2Cidades.setIcon(icon9)
        self.btn_buscar2Cidades.setIconSize(QtCore.QSize(35, 35))
        self.btn_buscar2Cidades.setObjectName("btn_buscar2Cidades")
        self.label_umaCidade = QtWidgets.QLabel(self.frame_lista)
        self.label_umaCidade.setGeometry(QtCore.QRect(40, 110, 231, 16))
        self.label_umaCidade.setMaximumSize(QtCore.QSize(300, 16))
        self.label_umaCidade.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 87 10pt \"Arial Black\";\n"
"")
        self.label_umaCidade.setObjectName("label_umaCidade")
        self.tabWidget_lista.addTab(self.tab_graficos, icon9, "")
        self.tab_previsao = QtWidgets.QWidget()
        self.tab_previsao.setObjectName("tab_previsao")
        self.frame_previsao_2 = QtWidgets.QFrame(self.tab_previsao)
        self.frame_previsao_2.setGeometry(QtCore.QRect(-1, -1, 301, 661))
        self.frame_previsao_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_previsao_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_previsao_2.setObjectName("frame_previsao_2")
        self.label_aplicarP = QtWidgets.QLabel(self.frame_previsao_2)
        self.label_aplicarP.setGeometry(QtCore.QRect(90, 60, 111, 21))
        self.label_aplicarP.setStyleSheet("background-color: transparent;")
        self.label_aplicarP.setTextFormat(QtCore.Qt.AutoText)
        self.label_aplicarP.setObjectName("label_aplicarP")

        self.frame_erroPrevisao = QtWidgets.QFrame(self.frame_previsao_2)
        self.frame_erroPrevisao.setGeometry(QtCore.QRect(30, 10, 220, 41))
        self.frame_erroPrevisao.setMaximumSize(QtCore.QSize(250, 41))
        self.frame_erroPrevisao.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_erroPrevisao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_erroPrevisao.setObjectName("frame_erroPrevisao")

        self.label_erroPrevisao = QtWidgets.QLabel(self.frame_erroPrevisao)
        self.label_erroPrevisao.setGeometry(QtCore.QRect(7, 0, 210, 30))
        self.label_erroPrevisao.setMaximumSize(QtCore.QSize(210, 30))
        self.label_erroPrevisao.setStyleSheet("QLabel{\n"
"image: url(:/logo/quadroT.png);\n"
"    background-color: rgb(226, 75, 0);\n"
"}")
        self.label_erroPrevisao.setAlignment(QtCore.Qt.AlignCenter)
        self.label_erroPrevisao.setObjectName("label_erroPrevisao")
        self.shadowframePrevisao.setBlurRadius(25)
        self.shadowframePrevisao.setOffset(-5,10)
        self.label_erroPrevisao.setGraphicsEffect(self.shadowframePrevisao)

        self.btn_X_erroP = QtWidgets.QPushButton(self.frame_erroPrevisao)
        self.btn_X_erroP.setGeometry(QtCore.QRect(170, 7, 31, 20))
        self.btn_X_erroP.setMaximumSize(QtCore.QSize(150, 100))
        self.btn_X_erroP.setStyleSheet("QPushButton{\n"
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
        self.btn_X_erroP.setText("")
        self.btn_X_erroP.setIcon(icon5)
        self.btn_X_erroP.setIconSize(QtCore.QSize(35, 35))
        self.btn_X_erroP.setObjectName("btn_X_erroP")
        self.btn_previsao = QtWidgets.QPushButton(self.frame_previsao_2)
        self.btn_previsao.setGeometry(QtCore.QRect(100, 200, 71, 61))
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
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/button/olho.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_previsao.setIcon(icon10)
        self.btn_previsao.setIconSize(QtCore.QSize(55, 55))
        self.btn_previsao.setObjectName("btn_previsao")
        self.comboBox_MunicipioP = QtWidgets.QComboBox(self.frame_previsao_2)
        self.comboBox_MunicipioP.setGeometry(QtCore.QRect(20, 110, 251, 21))
        self.comboBox_MunicipioP.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_MunicipioP.setObjectName("comboBox_MunicipioP")
        self.comboBox_MunicipioP.addItem("")
        self.comboBox_MunicipioP.addItem("")
        self.comboBox_MunicipioP.addItem("")
        self.comboBox_MunicipioP.addItem("")
        self.comboBox_MunicipioP.addItem("")
        self.comboBox_MunicipioP.addItem("")
        self.label_Municipio_P = QtWidgets.QLabel(self.frame_previsao_2)
        self.label_Municipio_P.setGeometry(QtCore.QRect(20, 80, 81, 31))
        self.label_Municipio_P.setMaximumSize(QtCore.QSize(81, 31))
        self.label_Municipio_P.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_Municipio_P.setObjectName("label_Municipio_P")
        self.label_natureza_P = QtWidgets.QLabel(self.frame_previsao_2)
        self.label_natureza_P.setGeometry(QtCore.QRect(20, 140, 91, 16))
        self.label_natureza_P.setMaximumSize(QtCore.QSize(91, 16))
        self.label_natureza_P.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_natureza_P.setObjectName("label_natureza_P")
        self.comboBox_naturezaP = QtWidgets.QComboBox(self.frame_previsao_2)
        self.comboBox_naturezaP.setGeometry(QtCore.QRect(20, 160, 251, 21))
        self.comboBox_naturezaP.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_naturezaP.setObjectName("comboBox_naturezaP")
        self.comboBox_naturezaP.addItem("")
        self.comboBox_naturezaP.addItem("")
        self.comboBox_naturezaP.addItem("")
        self.comboBox_naturezaP.addItem("")
        self.comboBox_naturezaP.addItem("")

        self.label_resuConfianca = QtWidgets.QLabel(self.frame_previsao_2)
        self.label_resuConfianca.setGeometry(QtCore.QRect(200, 470, 120, 41))
        self.label_resuConfianca.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.label_resuConfianca.setObjectName("label_resuConfianca")

        self.label_ano2021 = QtWidgets.QLabel(self.frame_previsao_2)
        self.label_ano2021.setGeometry(QtCore.QRect(30, 320, 90, 21))
        self.label_ano2021.setObjectName("label_ano2021")

        self.label_nivelConfianca = QtWidgets.QLabel(self.frame_previsao_2)
        self.label_nivelConfianca.setGeometry(QtCore.QRect(30, 480, 160, 21))
        self.label_nivelConfianca.setStyleSheet("background-color: transparent;")
        self.label_nivelConfianca.setObjectName("label_nivelConfianca")

        self.label_ano2023 = QtWidgets.QLabel(self.frame_previsao_2)
        self.label_ano2023.setGeometry(QtCore.QRect(30, 420, 90, 21))
        self.label_ano2023.setObjectName("label_ano2023")

        self.label_resultadoAno3 = QtWidgets.QLabel(self.frame_previsao_2)
        self.label_resultadoAno3.setGeometry(QtCore.QRect(150, 420, 71, 21))
        self.label_resultadoAno3.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.label_resultadoAno3.setObjectName("label_resultadoAno3")

        self.label_ano2022 = QtWidgets.QLabel(self.frame_previsao_2)
        self.label_ano2022.setGeometry(QtCore.QRect(30, 370, 90, 21))
        self.label_ano2022.setObjectName("label_ano2022")
        self.label_resultadoAno2 = QtWidgets.QLabel(self.frame_previsao_2)
        self.label_resultadoAno2.setGeometry(QtCore.QRect(150, 370, 71, 21))
        self.label_resultadoAno2.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.label_resultadoAno2.setObjectName("label_resultadoAno2")

        self.label_resultadoAno1 = QtWidgets.QLabel(self.frame_previsao_2)
        self.label_resultadoAno1.setGeometry(QtCore.QRect(150, 320, 71, 21))
        self.label_resultadoAno1.setStyleSheet("color: rgb(170, 0, 0);\n"
"font: 87 10pt \"Arial Black\";")
        self.label_resultadoAno1.setObjectName("label_resultadoAno1")

        self.label_resuPrevisao = QtWidgets.QLabel(self.frame_previsao_2)
        self.label_resuPrevisao.setGeometry(QtCore.QRect(70, 280, 130, 21))
        self.label_resuPrevisao.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_resuPrevisao.setObjectName("label_resuPrevisao")

        self.tabWidget_lista.addTab(self.tab_previsao, icon10, "")
        self.horizontalLayout.addWidget(self.tabWidget_lista)
        self.verticalLayout_3.addWidget(self.frame_fundo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_listaAviso.setCurrentIndex(0)
        self.tabWidget_lista.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #esconder o frame de erro
        self.frame_erroGraficos.hide()
        self.frame_label_erro_2.hide()
        self.frame_erroPrevisao.hide()
        self.frame_erroRanking.hide()
        #acao do buttons menu
        self.button_Mdataset.clicked.connect(lambda: Ui_MainWindow.toggleMenu(self,300,True))
        self.btn_ocorrencias.clicked.connect(self.ocorrencia)
        self.btn_taxa.clicked.connect(self.taxa_crime)
        self.btn_policia.clicked.connect(self.policia_prod)
        #acao do buttons regiao (1= ocorrencias e policia / 2 = taxa crime/)
        self.btn_grande_sp.clicked.connect(lambda: Ui_MainWindow.lista(self,"Grande São Paulo (exclui a Capital)","Grande S�o Paulo (exclui a Capital)"))
        self.btn_campinas.clicked.connect(lambda: Ui_MainWindow.lista(self,"Campinas","Campinas"))
        self.btn_aracatuba.clicked.connect(lambda: Ui_MainWindow.lista(self,"Araçatuba","Ara�atuba"))
        self.btn_araraquara.clicked.connect(lambda: Ui_MainWindow.lista(self,"0","0"))
        self.btn_baixadaSantista.clicked.connect(lambda: Ui_MainWindow.lista(self,"Santos","Santos"))
        self.btn_barretos.clicked.connect(lambda: Ui_MainWindow.lista(self,"0","0"))
        self.btn_bauru.clicked.connect(lambda: Ui_MainWindow.lista(self,"Bauru","Bauru"))
        self.btn_franca.clicked.connect(lambda: Ui_MainWindow.lista(self,"0","0"))
        self.btn_marilia.clicked.connect(lambda: Ui_MainWindow.lista(self,"0","0"))
        self.btn_piracicaba.clicked.connect(lambda: Ui_MainWindow.lista(self,"Piracicaba","0"))
        self.btn_presidentePrudente.clicked.connect(lambda: Ui_MainWindow.lista(self,"Presidente Prudente","Presidente Prudente"))
        self.btn_saoJoaoBoaVista.clicked.connect(lambda: Ui_MainWindow.lista(self,"0","0"))
        self.btn_saoJoseRioPreto.clicked.connect(lambda: Ui_MainWindow.lista(self,"São José do Rio Preto","S�o Jos� do Rio Preto"))
        self.btn_ribeiraoPreto.clicked.connect(lambda: Ui_MainWindow.lista(self,"Ribeirão Preto","Ribeir�o Preto"))
        self.btn_sorocaba.clicked.connect(lambda: Ui_MainWindow.lista(self,"Sorocaba","Sorocaba"))
        self.btn_taubate.clicked.connect(lambda: Ui_MainWindow.lista(self,"São José dos Campos","S�o Jos� dos Campos"))
        self.btn_registro.clicked.connect(lambda: Ui_MainWindow.lista(self,"0","0"))
        #acao do buttons lista

        self.btn_X_erroG.clicked.connect(lambda: self.frame_erroGraficos.hide())
        self.btn_X_erroM.clicked.connect(lambda: self.frame_label_erro_2.hide())
        self.btn_X_erroP.clicked.connect(lambda:self.frame_erroPrevisao.hide())
        self.btn_XerroR.clicked.connect(lambda:self.frame_erroRanking.hide())

        self.btn_buscar_1Cidade.clicked.connect(self.opcao_selecionada)
        self.btn_buscar2Cidades.clicked.connect(self.duas_cidades)

        #acao do buttons dataset com lista previsao e lista regiao
        self.btn_dataset.clicked.connect(self.animacaoRanking)
        self.btn_previsao.clicked.connect(self.previsao)
        self.btn_ranking.clicked.connect(self.ranking)

        self.btn_noticia1.clicked.connect(lambda: Ui_MainWindow.linkNoticia(self,1))
        self.btn_noticia2.clicked.connect(lambda: Ui_MainWindow.linkNoticia(self,2))
        self.btn_noticia3.clicked.connect(lambda: Ui_MainWindow.linkNoticia(self,3))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_Mdataset.setText(_translate("MainWindow", "MENU DATASET"))
        self.label_Criminalidade.setText(_translate("MainWindow", "Dataset Criminalidade"))
        self.btn_taxa.setText(_translate("MainWindow", "Taxa de Criminalidade"))
        self.btn_ocorrencias.setText(_translate("MainWindow", "Registro de Ocorrencias"))
        self.btn_policia.setText(_translate("MainWindow", "Produtividade Policial"))
        self.label_resuPrevisao_2.setText(_translate("MainWindow", "RANKING da cidades:"))
        self.label_regiaoR.setText(_translate("MainWindow", "REGIAO:"))
        self.label_ano2020.setText(_translate("MainWindow", "ANO:                 2020"))
        self.label_nomeRegiaoR.setText(_translate("MainWindow", ""))
        self.label_posicao1.setText(_translate("MainWindow", "1 -"))
        self.label_posicao2.setText(_translate("MainWindow", "2 -"))
        self.label_posicao3.setText(_translate("MainWindow", "3 -"))
        self.label_posicao4.setText(_translate("MainWindow", "4 -"))
        self.label_posicao5.setText(_translate("MainWindow", "5 -"))
        self.label_cidadeP1.setText(_translate("MainWindow", ""))
        self.label_cidadeP2.setText(_translate("MainWindow", ""))
        self.label_cidadeP3.setText(_translate("MainWindow", ""))
        self.label_cidadeP4.setText(_translate("MainWindow", ""))
        self.label_cidadeP5.setText(_translate("MainWindow", ""))

        self.btn_ranking.setText(_translate("MainWindow", " Ranking"))
        self.label_total1.setText(_translate("MainWindow", ""))
        self.label_total2.setText(_translate("MainWindow", ""))
        self.label_total3.setText(_translate("MainWindow", ""))
        self.label_total4.setText(_translate("MainWindow", ""))
        self.label_total5.setText(_translate("MainWindow", ""))
        self.label_erroRanking.setText(_translate("MainWindow", "ERRO ao selecionar!"))
        self.label_error_2.setText(_translate("MainWindow", "ESSA REGIAO NAO POSSUI DADOS SUFICIENTES!"))
        self.plainTextAviso.setPlainText(_translate("MainWindow", "Usos (e alguns abusos) das Estatísticas Oficiais de Criminalidade\n"
"\n"
"    As estatísticas oficiais de criminalidade são utilizadas regularmente em todos os países para retratar a situação da segurança pública, mas devemos lembrar que estes dados devem sempre ser interpretados com prudência, pois os dados oficiais de criminalidade estão sujeitos a uma série de limites de validade e confiabilidade: eles são antes um retrato do processo social de notificação de crimes do que um retrato fiel do universo dos crimes realmente cometidos num determinado local.\n"
"    Para que um crime faça parte das estatísticas oficiais são necessárias três etapas sucessivas:\n"
"o crime deve ser detectado, notificado às autoridades policiais e por último registrado no boletim deocorrência. \n"
"Pesquisas de vitimização realizadas no Brasil sugerem que, em média, os organismos policiais registram apenas um\n"
"terço dos crimes ocorridos, percentual que varia de acordo com o delito. Além disso, o aumento das estatísticas\n"
"oficiais de criminalidade podem estar refletindo flutuações causadas por práticas policiais mais ou menos intensas, ou por modificações de ordem legislativa, ou administrativa.\n"
"\n"
"fonte: http://www.ssp.sp.gov.br/Estatistica"))
        self.tab_listaAviso.setTabText(self.tab_listaAviso.indexOf(self.tab_aviso), _translate("MainWindow", "AVISO"))
        self.plainTextDicas.setPlainText(_translate("MainWindow", "    Dicas de segurança da Polícia Civil:\n"
"\n"
"    Na residência:\n"
"· Verifique sempre se as portas e os portões estão bem fechados. Evite correntes com cadeados virados para o lado de fora da casa.\n"
"·  Se você recebe periodicamente jornais e revistas, suspenda a entrega, ou peça que algum vizinho ou parente recolha para você.  A acumulação de jornais e correspondências na porta da casa, podem chamar a atenção de bandidos.\n"
"·  Alarmes e sensores de presença ajudam a evitar transtornos.\n"
"\n"
"    Nas ruas:\n"
"Evite ostentar objetos de valor como celulares, relógios, pulseiras e joias.\n"
"· Evite passar em locais mal iluminados.\n"
"· Se perceber que está sendo seguido, entre em algum estabelecimento comercial.\n"
"· Não abra a sua carteira ou bolsa na frente de estranhos. Separe pequenas quantias para pagamentos de passagens, cafés, etc.\n"
"\n"
"    Nos bancos:\n"
"· Não converse, nem aceite a ajuda de estranhos.\n"
"· Proteja-se no momento de fazer saques e depósitos.\n"
"· Se, ao sair do banco, o pneu do carro estiver vazio, volte e confie seu dinheiro à guarda do gerente. Só então providencie a troca, pelo estepe. Você estará evitando a ação de ladrões que roubam seu dinheiro, enquanto você troca o pneu.\n"
"No transporte coletivo:\n"
"\n"
"    cuidados no transporte coletivo\n"
"· Mantenha bolsa, carteira, pacotes ou sacolas na frente de seu corpo.\n"
"· Em ônibus com poucos passageiros, procure viajar próximo ao motorista.\n"
"·Ande sempre com o dinheiro da passagem contado.\n"
"· Evite ficar sozinho, em pontos de ônibus isolados.\n"
"· Nos trens urbanos, evite andar em vagões vazios, principalmente à noite.\n"
"\n"
"    Nos terminais rodoviários, ferroviários e aeroportos:\n"
"· Não aceite a ajuda de pessoas não credenciadas, interessadas em carregar sua bagagem.\n"
"· Nunca deixe sua bagagem sem alguém de confiança olhando.\n"
"· Cuidado com os menores, sob sua responsabilidade.\n"
"· Ao despachar qualquer bagagem, inclusive de mão, verifique se estão bem fechadas.\n"
"· Coloque identificação visível em todas as bagagens.\n"
"\n"
"    Nas praias\n"
"· Nunca leve objetos de valor à praia.\n"
"·Nunca deixe seus pertences sozinhos. Peça a alguém de confiança para olhar, enquanto vai tomar banho de mar.\n"
"·Não aceite bebida de estranhos. Podem estar adulteradas, com algum tipo de narcótico.\n"
"· Evite tomar banho de mar em locais que você não conhece.\n"
"· Se beber, não entre no mar.\n"
"\n"
"    No carro:\n"
"· Nunca deixe objetos de valor no interior do veículo.\n"
"· Ao sair, mesmo que por alguns segundos, levante os vidros, tranque as portas e o porta-malas, e se possível, ligue o alarme.\n"
"· Procure estacionar em locais vigiados por pessoas de confiança e, se possível, em locais iluminados e visíveis.\n"
"· Não dê caronas a estranhos.\n"
"· Procure não se aproximar do seu carro e nem entrar, se perceber a presença de pessoas suspeitas nas proximidades.\n"
"· Se desconfiar que está sendo seguido, dirija-se ao posto policial mais próximo.\n"
"\n"
""))
        self.tab_listaAviso.setTabText(self.tab_listaAviso.indexOf(self.tab_dicas), _translate("MainWindow", "DICAS DE PROTECAO"))
        self.label_noticias.setText(_translate("MainWindow", "    ULTIMAS NOTICIAS DA SEMANA:"))
        self.btn_noticia1.setText(_translate("MainWindow", "Acessar noticia"))
        self.btn_noticia2.setText(_translate("MainWindow", "Acessar noticia"))
        self.btn_noticia3.setText(_translate("MainWindow", "Acessar noticia"))
        self.label_estado.setText(_translate("MainWindow", "ESTADO DE SAO PAULO"))
        self.label_Municipio.setText(_translate("MainWindow", "Municipio:"))

        self.label_busca.setText(_translate("MainWindow", "Natureza:"))

        self.btn_buscar_1Cidade.setText(_translate("MainWindow", "Buscar Grafico"))
        self.label_erroGraficos.setText(_translate("MainWindow", "ERRO ao selecionar!"))
        self.label_duasCidades.setText(_translate("MainWindow", "GRAFICO PARA DUAS CIDADES:"))
 
        self.label_primeiraCidade.setText(_translate("MainWindow", "primeira cidade:"))
        self.label_segundaCidade.setText(_translate("MainWindow", "Segunda cidade:"))

 
        self.label_comparacao.setText(_translate("MainWindow", "Tipo de natureza da comparacao:"))
        self.btn_buscar2Cidades.setText(_translate("MainWindow", "Buscar por Comparacao"))
        self.label_umaCidade.setText(_translate("MainWindow", "GRAFICO PARA UMA CIDADE:"))
        self.tabWidget_lista.setTabText(self.tabWidget_lista.indexOf(self.tab_graficos), _translate("MainWindow", "GRAFICOS"))
        self.label_aplicarP.setText(_translate("MainWindow", "APLICAR PREVISAO "))
        self.label_erroPrevisao.setText(_translate("MainWindow", "ERRO ao selecionar!"))

        self.label_Municipio_P.setText(_translate("MainWindow", "Municipio:"))
        self.label_natureza_P.setText(_translate("MainWindow", "Natureza:"))

        self.label_resuConfianca.setText(_translate("MainWindow", "XXXX"))
        self.label_ano2021.setText(_translate("MainWindow", "ANO DE 2021"))
        self.label_nivelConfianca.setText(_translate("MainWindow", "NIVEL DE CONFIANCA:"))
        self.label_ano2023.setText(_translate("MainWindow", "ANO DE 2023"))
        self.label_resultadoAno3.setText(_translate("MainWindow", "XXXX"))
        self.label_ano2022.setText(_translate("MainWindow", "ANO DE 2022"))
        self.label_resultadoAno2.setText(_translate("MainWindow", "XXXX"))
        self.label_resultadoAno1.setText(_translate("MainWindow", "XXXX"))
        self.label_resuPrevisao.setText(_translate("MainWindow", "resultado previsto:"))
        self.tabWidget_lista.setTabText(self.tabWidget_lista.indexOf(self.tab_previsao), _translate("MainWindow", "PREVISAO"))
#importar arquivo com dados das imagem da interface        
import sistema_crime_images


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
