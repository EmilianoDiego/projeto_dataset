# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_sp.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

import threading
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QRect
import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import threading
import time
import csv


class Ui_MainWindow(threading.Thread):
    tabela = "Selecione"
    shadow = QGraphicsDropShadowEffect()  
    shadow2 = QGraphicsDropShadowEffect()  
    natureza = []  
    cidade =[] 
    cidade2=[]

    def lista_cidade(self,pular,quantidade,tabela,tipo):
        if tipo == 1:    
                file = pd.read_csv("projeto_dataset/alterar_tabela/" + tabela,encoding="utf-8", sep=';')
                #arquivo recebe uma lista do file somente da coluna cidade
                arquivo = csv.reader(file["Cidade"])
        elif tipo == 2:    
                file = pd.read_csv("projeto_dataset/alterar_tabela/" +tabela,encoding = "utf-8")
                #arquivo recebe uma lista do file somente da coluna cidade
                arquivo = csv.reader(file["Cidade"])
        elif tipo == 3:    
                file = pd.read_csv("projeto_dataset/alterar_tabela/" + tabela,encoding="utf-8")
                #arquivo recebe uma lista do file somente da coluna cidade
                arquivo = csv.reader(file["Cidade"])                
        valor =0
        #for pecorre toda a lista do arquivo
        for i, item in enumerate(arquivo):
        #if exibe o conteudo da linha somente quando i for maior que valor, 
        # valor e referencia para buscar nomes da cidades pulando todos os anos em que ela aparece
                if i >= valor :
                        text= "-"
                        text = text  + str(item)
                        print(text)
        #nomes insere o conteudo de linha, para armazenar os nomes da cidades que existe na tabela
                        #self.cidade.insert(i, text)
        #valor e somado + pular, pois para cada nova cidade aparecer, e preciso pular x linhas
                        valor = valor+ pular
        #apos a leitura de quantidade linhas contidas na tabela o loop termina
                        if valor > quantidade :
                                break                       


    def duas_cidades(self):    
        natureza = self.comboBox_natureza2.currentText()
        cidade = self.comboBox_cidade1.currentText()
        cidade2 = self.comboBox_cidade2.currentText() 
        #verifica se os itens no combobox foram selecionados
        if (self.tabela == "Selecione") or (natureza == "Selecione") or (cidade == "Selecione") or (cidade2 == "Selecione"):
            self.frame_erro.show()
        #tabela TAXA_CRIME    
        elif self.tabela == "tabela_taxa_crime_sp.csv":
                self.frame_erro.hide()
                dataset = pd.read_csv("projeto_dataset/alterar_tabela/" + self.tabela,sep=';', encoding="utf-8")

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
                plt.rcParams["figure.figsize"] = (12,8)
                df = pd.DataFrame({natureza +" - " + cidade: lista,
                                   natureza +" - " + cidade2: lista_outra}, index=dados["Ano"])
                #grafico 1                   
                ax = df.plot.bar(rot=0)
                plt.show()
                #grafico 2
                lines = df.plot.line()
                plt.show()
        #tabela ocorrencias_mensais_crimes_sp.csv    
        elif self.tabela == "ocorrencias_mensais_crimes_sp.csv":
                self.frame_erro.hide()
                #busca o dados da tabela csv             
                dataset = pd.read_csv("projeto_dataset/alterar_tabela/" +self.tabela, encoding="latin-1")
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
                plt.rcParams["figure.figsize"] = (12,8)
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
                self.frame_erro.hide()
                dataset = pd.read_csv("projeto_dataset/alterar_tabela/" + self.tabela, encoding="utf-8")

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
                plt.rcParams["figure.figsize"] = (12,8)
                df = pd.DataFrame({natureza +" - " + cidade: lista,
                                   natureza +" - " + cidade2: lista_outra}, index=dados["Ano"])
                #grafico 1                   
                ax = df.plot.bar(rot=0)
                plt.show()
                #grafico 2
                lines = df.plot.line()
                plt.show()                   

    #busca criada para verificar graficos de 1 cidade    
    def opcao_selecionada(self):
        natureza = self.comboBox_natureza .currentText()
        cidade = self.comboBox_Municipio.currentText() 
        #verifica se os itens no combobox foram selecionados
        if (self.tabela == "Selecione") or (natureza == "Selecione") or (cidade == "Selecione"):
            self.frame_erro.show()

        #tabela TAXA_CRIME    
        elif self.tabela == "tabela_taxa_crime_sp.csv":
                self.frame_erro.hide()
                dataset = pd.read_csv("projeto_dataset/alterar_tabela/" + self.tabela,sep=';', encoding="utf-8")
                dados = dataset[(dataset.Cidade == cidade)].sort_values("Ano")
                lista =[]
                for i, item in enumerate(dados[natureza]):
                        lista.insert(i, item)
                #grafico 1
                #configurar o tamanho do grafico
                plt.rcParams["figure.figsize"] = (12,8)
                df = pd.DataFrame({natureza: lista}, index=dados["Ano"])
                ax = df.plot.bar(rot=0)
                plt.show()

        #tabela OCORRENCIAS_MENSAIS
        elif self.tabela == "ocorrencias_mensais_crimes_sp.csv":   
            self.frame_erro.hide() 
            #busca o dados da tabela csv             
            dataset = pd.read_csv("projeto_dataset/alterar_tabela/" + self.tabela, encoding="latin-1")
            #busca os dados da tabela apartir do tipo de natureza em qual cidade e pelo periodo dos anos contidos na tabela    
            dados = dataset[(dataset.Natureza == natureza) & (dataset.Cidade == cidade)].sort_values("Ano")
            #envia os dados para a construcao do grafico com matplotlib 
            # #configurar o tamanho do grafico
            plt.rcParams["figure.figsize"] = (12,8)   
            sns.barplot(x = "Ano", y="Total",data = dados, color="blue")
            plt.xticks(rotation=90)
            plt.title(natureza +" "+ cidade,fontsize = 14)
            plt.xlabel("Ano", fontsize = 10)
            plt.ylabel("numeros de:"+ natureza, fontsize = 10)
            #apresenta o grafico
            plt.show()

        #tabela POLICIA_PRODUTIVIDADE
        elif self.tabela == "tabela_policia_produtividade.csv":
                self.frame_erro.hide() 
                #busca o dados da tabela csv 
                dataset = pd.read_csv("projeto_dataset/alterar_tabela/"+ self.tabela, encoding="utf-8")
                #busca os dados da tabela apartir do tipo de natureza em qual cidade e pelo periodo dos anos contidos na tabela
                dados = dataset[(dataset.Cidade == cidade) & (dataset.Natureza == natureza)].sort_values("Ano")
                lista=[]
                for i, item in enumerate(dados["Total"]):
                        lista.insert(i,item)
                #grafico 1
                #configurar o tamanho do grafico
                plt.rcParams["figure.figsize"] = (12,8)
                df = pd.DataFrame({natureza: lista}, index=dados["Ano"])
                ax = df.plot.bar(rot=0)
                plt.show()        

#metodo de chamada da lista 
    def lista(self): 
        #get width
        #height = self.frame_lista.height()
        height = self.frame_lista.width()
        maxExtend = 300
        standard =1
           #set max width   
        if height == 1:
                widthExtended = maxExtend
        else:
                widthExtended = standard

        #self.shadow2.setBlurRadius(25)
        #self.shadow2.setOffset(-5,10)
        #self.frame_mapa_sp_2.setGraphicsEffect(self.shadow2)

        self.shadow.setBlurRadius(25)
        self.shadow.setOffset(-5,10)
        self.frame_lista.setGraphicsEffect(self.shadow)

        #self.animation = QPropertyAnimation(self.frame_lista, b"maximumHeight")
        self.animation = QPropertyAnimation(self.frame_lista, b"maximumWidth")
        self.animation.setDuration(600)
        self.animation.setStartValue(height)
        self.animation.setEndValue(widthExtended)
        self.animation.start()
#metodo de chamada do mapa
    def mapaSp(self):
            #get width
            width = self.frame_mapa_sp_2.width()
            maxExtend = 890
            standard =1
            #set max width
            if width == 1:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            self.animation = QPropertyAnimation(self.frame_mapa_sp_2, b"maximumWidth")
            self.animation.setDuration(800)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.start()
            

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
     
    def outra_chamada(self):
            #criar nova chamada para evento do button
            #     
            click_thread = Ui_MainWindow(self.lista())
            click_thread.start


    def taxa_crime(self):
            self.comboBox_Municipio.clear()
            self.comboBox_natureza.clear()
            self.comboBox_cidade1.clear()
            self.comboBox_cidade2.clear()
            self.comboBox_natureza2.clear()
            self.natureza =["Selecione","Homicídio Doloso por 100 mil habitantes",
            "Furto por 100 mil habitantes","Roubo por 100 mil habitantes",
            "Furto e Roubo de Veículo por 100 mil habitantes",
            "Furto por 100 mil veículos",
            "Roubo por 100 mil veículos",
            "Furto e Roubo de Veículo por 100 mil veículos"] 
            
            self.cidade = ["Selecione","S�o Paulo","Barueri","Carapicu�ba","Cotia","Diadema","Embu das Artes","Ferraz de Vasconcelos","Francisco Morato",
                           "Franco da Rocha","Guarulhos","Itapecerica da Serra","Itapevi","Itaquaquecetuba","Jandira","Mau�","Osasco","Santo Andr�","Jandira",
                           "Mogi das Cruzes","Campinas","Jacare�"]
            self.comboBox_natureza.addItems(self.natureza)  
            self.comboBox_Municipio.addItems(self.cidade)
            self.comboBox_cidade1.addItems(self.cidade)  
            self.comboBox_cidade2.addItems(self.cidade)
            self.comboBox_natureza2.addItems(self.natureza)
            self.tabela = "tabela_taxa_crime_sp.csv"
            if self.frame_lista.width() == 1 & self.frame_mapa_sp_2.width() == 1 :
                    self.mapaSp()
            if self.frame_lista.width() == 300:
                self.lista()
    

    def ocorrencia(self):
            self.comboBox_Municipio.clear()
            self.comboBox_natureza.clear()
            self.comboBox_cidade1.clear()
            self.comboBox_cidade2.clear()
            self.comboBox_natureza2.clear()
            self.natureza = ["Selecione","HOMICÍDIO DOLOSO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO",
                "HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO","Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO",
                "HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO","HOMICÍDIO CULPOSO OUTROS",
                "TENTATIVA DE HOMICÍDIO","LESÃO CORPORAL SEGUIDA DE MORTE",
                "LESÃO CORPORAL DOLOSA","LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO",
                "LESÃO CORPORAL CULPOSA - OUTRAS","LATROCÍNIO","Nº DE VÍTIMAS EM LATROCÍNIO",
                "TOTAL DE ESTUPRO","ESTUPRO","ESTUPRO DE VULNERÁVEL",
                "TOTAL DE ROUBO - OUTROS","ROUBO - OUTROS","ROUBO DE VEÍCULO","ROUBO A BANCO",
                "ROUBO DE CARGA","FURTO - OUTROS","FURTO DE VEÍCULO"] 
            self.cidade = ["Selecione","São Paulo","Franco da Rocha","São Lourenço da Serra","Suzano","Taboão da Serra",
              "Vargem Grande Paulista","Aparecida","Areias","Bragança Paulista","Santo André",
              "Campinas""Diadema","Itanhaém","Itapecerica da Serra","Itapevi","Cotia","Ilhabela","São Roque","Itatinga","Boituva","Santos","Cajati","Jaú","Jardinópolis","Santana de Parnaíba","Osasco"]
            self.comboBox_natureza .addItems(self.natureza)  
            self.comboBox_Municipio.addItems(self.cidade)
            self.comboBox_cidade1.addItems(self.cidade)  
            self.comboBox_cidade2.addItems(self.cidade)
            self.comboBox_natureza2.addItems(self.natureza)
            self.tabela = "ocorrencias_mensais_crimes_sp.csv"
            if self.frame_lista.width() == 1 & self.frame_mapa_sp_2.width() == 1 :
                    self.mapaSp()
            if self.frame_lista.width() == 300:
                self.lista()


    def policia_prod(self):
            self.comboBox_Municipio.clear()
            self.comboBox_natureza.clear()
            self.comboBox_cidade1.clear()
            self.comboBox_cidade2.clear()
            self.comboBox_natureza2.clear()
            self.natureza = ["Selecione","OCORRÊNCIAS DE PORTE DE ENTORPECENTES","Nº DE INFRATORES APREENDIDOS EM FLAGRANTE","OCORRÊNCIAS DE TRÁFICO DE ENTORPECENTES",
                             "OCORRÊNCIAS DE APREENSÃO DE ENTORPECENTES(1)","OCORRÊNCIAS DE PORTE ILEGAL DE ARMA","Nº DE ARMAS DE FOGO APREENDIDAS","Nº DE FLAGRANTES LAVRADOS",
                             "Nº DE INFRATORES APREENDIDOS EM FLAGRANTE","Nº DE INFRATORES APREENDIDOS POR MANDADO","Nº DE PESSOAS PRESAS EM FLAGRANTE","Nº DE PESSOAS PRESAS POR MANDADO",
                             "Nº DE PRISÕES EFETUADAS","Nº DE VEÍCULOS RECUPERADOS","TOT. DE INQUÉRITOS POLICIAIS INSTAURADOS"]  
            
            self.cidade = ["Selecione","São Paulo","Arujá","Barueri","Biritiba Mirim","Caieiras","Cajamar","Carapicuíba","Cotia","Diadema","Embu das Artes","Embu Guaçú",
                           "Ferraz de Vasconcelos","Itaquaquecetuba","Francisco Morato","Guarulhos","Jandira","Mairiporã","Suzano","Taboão da Serra"]
            self.comboBox_natureza .addItems(self.natureza)  
            self.comboBox_Municipio.addItems(self.cidade)
            self.comboBox_cidade1.addItems(self.cidade)  
            self.comboBox_cidade2.addItems(self.cidade)
            self.comboBox_natureza2.addItems(self.natureza)
            self.tabela = "tabela_policia_produtividade.csv"
            if self.frame_lista.width() == 1 & self.frame_mapa_sp_2.width() == 1 :
                    self.mapaSp()
            if self.frame_lista.width() == 300:
                self.lista()          
 





    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 850)
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

        self.frame_logo2_2 = QtWidgets.QFrame(self.frame_menu)
        self.frame_logo2_2.setMinimumSize(QtCore.QSize(400, 80))
        self.frame_logo2_2.setMaximumSize(QtCore.QSize(800, 80))
        self.frame_logo2_2.setStyleSheet("background-color: rgb(255, 255, 255,0.0);")
        self.frame_logo2_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_logo2_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo2_2.setObjectName("frame_logo2_2")

        self.label_dataset = QtWidgets.QLabel(self.frame_logo2_2)
        self.label_dataset.setGeometry(QtCore.QRect(80, 20, 251, 41))
        self.label_dataset.setMaximumSize(QtCore.QSize(251, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_dataset.setFont(font)
        self.label_dataset.setStyleSheet("QLabel{\n"
"background-color: rgb(255, 255, 255,0.0);\n"
"    font: 75 16pt \"MS Shell Dlg 2\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_dataset.setTextFormat(QtCore.Qt.AutoText)
        self.label_dataset.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dataset.setObjectName("label_dataset")

        self.frame_logo_sp = QtWidgets.QFrame(self.frame_logo2_2)
        self.frame_logo_sp.setGeometry(QtCore.QRect(240, -10, 451, 121))
        self.frame_logo_sp.setMaximumSize(QtCore.QSize(451, 121))
        self.frame_logo_sp.setStyleSheet("\n"
"image: url(:/logo/logo_sp.png);\n"
"background-color: rgb(255, 255, 255,0.0);")
        self.frame_logo_sp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_logo_sp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo_sp.setObjectName("frame_logo_sp")
        self.horizontalLayout_2.addWidget(self.frame_logo2_2)

        self.frame_logo1 = QtWidgets.QFrame(self.frame_menu)
        self.frame_logo1.setMinimumSize(QtCore.QSize(100, 80))
        self.frame_logo1.setMaximumSize(QtCore.QSize(200, 80))
        self.frame_logo1.setStyleSheet("background-color: rgb(255, 255, 255,0.0);")
        self.frame_logo1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_logo1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo1.setObjectName("frame_logo1")
        self.frame_logo2 = QtWidgets.QFrame(self.frame_logo1)
        self.frame_logo2.setGeometry(QtCore.QRect(110, 10, 71, 61))
        self.frame_logo2.setMaximumSize(QtCore.QSize(71, 61))
        self.frame_logo2.setStyleSheet("QFrame{\n"
"image: url(:/logo/logo_datasets.png);\n"
"\n"
"}")
        self.frame_logo2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_logo2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo2.setObjectName("frame_logo2")
        self.horizontalLayout_2.addWidget(self.frame_logo1)
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
        self.frame_Mbuttons.setMaximumSize(QtCore.QSize(10, 800))
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
        self.frame_buttons.setMaximumSize(QtCore.QSize(200, 159))
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
        self.verticalLayout_6.addWidget(self.frame_buttons, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.frame_Mbuttons)

        self.frame_mapa_sp = QtWidgets.QFrame(self.frame_fundo)
        self.frame_mapa_sp.setMaximumSize(QtCore.QSize(1190, 656))
        self.frame_mapa_sp.setStyleSheet("")
        self.frame_mapa_sp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_mapa_sp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mapa_sp.setObjectName("frame_mapa_sp")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_mapa_sp)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.frame_mapa_sp_2 = QtWidgets.QFrame(self.frame_mapa_sp)
        self.frame_mapa_sp_2.setMaximumSize(QtCore.QSize(1, 656))
        self.frame_mapa_sp_2.setStyleSheet("QFrame{\n"
"image: url(:/mapa/mapaE_sp.png);\n"
"}")
        self.frame_mapa_sp_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_mapa_sp_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_mapa_sp_2.setObjectName("frame_mapa_sp_2")

        self.btn_grande_sp_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_grande_sp_2.setGeometry(QtCore.QRect(470, 380, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_grande_sp_2.setFont(font)
        self.btn_grande_sp_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_grande_sp_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_grande_sp_2.setAutoRepeat(False)
        self.btn_grande_sp_2.setObjectName("btn_grande_sp_2")
        self.btn_sorocaba_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_sorocaba_2.setGeometry(QtCore.QRect(340, 400, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_sorocaba_2.setFont(font)
        self.btn_sorocaba_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_sorocaba_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_sorocaba_2.setAutoRepeat(False)
        self.btn_sorocaba_2.setObjectName("btn_sorocaba_2")
        self.btn_registro_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_registro_2.setGeometry(QtCore.QRect(360, 450, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_registro_2.setFont(font)
        self.btn_registro_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_registro_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_registro_2.setAutoRepeat(False)
        self.btn_registro_2.setObjectName("btn_registro_2")
        self.btn_taubate_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_taubate_2.setGeometry(QtCore.QRect(560, 350, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_taubate_2.setFont(font)
        self.btn_taubate_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_taubate_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_taubate_2.setAutoRepeat(False)
        self.btn_taubate_2.setObjectName("btn_taubate_2")
        self.btn_bauru_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_bauru_2.setGeometry(QtCore.QRect(290, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_bauru_2.setFont(font)
        self.btn_bauru_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_bauru_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_bauru_2.setAutoRepeat(False)
        self.btn_bauru_2.setObjectName("btn_bauru_2")
        self.btn_ribeiraoPreto_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_ribeiraoPreto_2.setGeometry(QtCore.QRect(380, 200, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_ribeiraoPreto_2.setFont(font)
        self.btn_ribeiraoPreto_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_ribeiraoPreto_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_ribeiraoPreto_2.setAutoRepeat(False)
        self.btn_ribeiraoPreto_2.setObjectName("btn_ribeiraoPreto_2")
        self.btn_aracatuba_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_aracatuba_2.setGeometry(QtCore.QRect(150, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_aracatuba_2.setFont(font)
        self.btn_aracatuba_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_aracatuba_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_aracatuba_2.setAutoRepeat(False)
        self.btn_aracatuba_2.setObjectName("btn_aracatuba_2")
        self.btn_saoJoseBoaVista_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_saoJoseBoaVista_2.setGeometry(QtCore.QRect(460, 240, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_saoJoseBoaVista_2.setFont(font)
        self.btn_saoJoseBoaVista_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_saoJoseBoaVista_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_saoJoseBoaVista_2.setAutoRepeat(False)
        self.btn_saoJoseBoaVista_2.setObjectName("btn_saoJoseBoaVista_2")
        self.btn_saojoseriopreto_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_saojoseriopreto_2.setGeometry(QtCore.QRect(210, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_saojoseriopreto_2.setFont(font)
        self.btn_saojoseriopreto_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_saojoseriopreto_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_saojoseriopreto_2.setAutoRepeat(False)
        self.btn_saojoseriopreto_2.setObjectName("btn_saojoseriopreto_2")
        self.btn_campinas_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_campinas_2.setGeometry(QtCore.QRect(450, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_campinas_2.setFont(font)
        self.btn_campinas_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_campinas_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_campinas_2.setAutoRepeat(False)
        self.btn_campinas_2.setObjectName("btn_campinas_2")
        self.btn_marilia_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_marilia_2.setGeometry(QtCore.QRect(190, 290, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_marilia_2.setFont(font)
        self.btn_marilia_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_marilia_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_marilia_2.setAutoRepeat(False)
        self.btn_marilia_2.setObjectName("btn_marilia_2")
        self.btn_Pprudente_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_Pprudente_2.setGeometry(QtCore.QRect(80, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_Pprudente_2.setFont(font)
        self.btn_Pprudente_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_Pprudente_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_Pprudente_2.setAutoRepeat(False)
        self.btn_Pprudente_2.setObjectName("btn_Pprudente_2")
        self.btn_barretos_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_barretos_2.setGeometry(QtCore.QRect(310, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_barretos_2.setFont(font)
        self.btn_barretos_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_barretos_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_barretos_2.setAutoRepeat(False)
        self.btn_barretos_2.setObjectName("btn_barretos_2")
        self.btn_franca_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_franca_2.setGeometry(QtCore.QRect(390, 140, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_franca_2.setFont(font)
        self.btn_franca_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_franca_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_franca_2.setAutoRepeat(False)
        self.btn_franca_2.setObjectName("btn_franca_2")
        self.btn_santista_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_santista_2.setGeometry(QtCore.QRect(480, 420, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_santista_2.setFont(font)
        self.btn_santista_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_santista_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_santista_2.setAutoRepeat(False)
        self.btn_santista_2.setObjectName("btn_santista_2")
        self.btn_piracicaba_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_piracicaba_2.setGeometry(QtCore.QRect(380, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_piracicaba_2.setFont(font)
        self.btn_piracicaba_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_piracicaba_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_piracicaba_2.setAutoRepeat(False)
        self.btn_piracicaba_2.setObjectName("btn_piracicaba_2")
        self.btn_araraquara_2 = QtWidgets.QPushButton(self.frame_mapa_sp_2)
        self.btn_araraquara_2.setGeometry(QtCore.QRect(340, 240, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.btn_araraquara_2.setFont(font)
        self.btn_araraquara_2.setStyleSheet("QPushButton{\n"
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
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0.409, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.994318 rgba(178, 176, 169, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(0, 0, 0);\n"
"border-radius:12px solid;\n"
"}")
        self.btn_araraquara_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_araraquara_2.setAutoRepeat(False)
        self.btn_araraquara_2.setObjectName("btn_araraquara_2")
        self.verticalLayout_2.addWidget(self.frame_mapa_sp_2)
        self.horizontalLayout.addWidget(self.frame_mapa_sp)

        self.frame_lista = QtWidgets.QFrame(self.frame_fundo)
        self.frame_lista.setMaximumSize(QtCore.QSize(1, 700))
        #cor anterior
        #qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0.0568182 rgba(255, 255, 255, 178), stop:0.193182 rgba(223, 223, 223, 248), stop:0.335227 rgba(245, 245, 245, 255), stop:0.573864 rgba(230, 230, 230, 255), stop:0.823864 rgba(235, 235, 235, 255), stop:0.965909 rgba(249, 249, 249, 255));
        self.frame_lista.setStyleSheet("background-color: rgb(255, 255, 255);\n")
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
        self.label_Municipio.setGeometry(QtCore.QRect(30, 90, 81, 31))
        self.label_Municipio.setMaximumSize(QtCore.QSize(81, 31))
        self.label_Municipio.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_Municipio.setObjectName("label_Municipio")

        self.comboBox_Municipio = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_Municipio.setGeometry(QtCore.QRect(30, 120, 251, 21))
        self.comboBox_Municipio.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_Municipio.setObjectName("comboBox_Municipio")
        self.comboBox_Municipio.addItems(self.cidade)

        self.label_busca = QtWidgets.QLabel(self.frame_lista)
        self.label_busca.setGeometry(QtCore.QRect(30, 260, 91, 16))
        self.label_busca.setMaximumSize(QtCore.QSize(91, 16))
        self.label_busca.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_busca.setObjectName("label_busca")

        self.label_icon_pessoas = QtWidgets.QLabel(self.frame_lista)
        self.label_icon_pessoas.setGeometry(QtCore.QRect(20, 180, 61, 41))
        self.label_icon_pessoas.setMaximumSize(QtCore.QSize(61, 41))
        self.label_icon_pessoas.setStyleSheet("QLabel{\n"
"\n"
"    image: url(:/logo/populacao.png);\n"
"    background-color: rgb(255, 255, 255,0.0);\n"
"}")
        self.label_icon_pessoas.setText("")
        self.label_icon_pessoas.setObjectName("label_icon_pessoas")

        self.label__populacao = QtWidgets.QLabel(self.frame_lista)
        self.label__populacao.setGeometry(QtCore.QRect(90, 190, 81, 21))
        self.label__populacao.setMaximumSize(QtCore.QSize(81, 21))
        self.label__populacao.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label__populacao.setAlignment(QtCore.Qt.AlignCenter)
        self.label__populacao.setObjectName("label__populacao")

        self.comboBox_natureza = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_natureza .setGeometry(QtCore.QRect(30, 280, 251, 21))
        self.comboBox_natureza .setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_natureza .setObjectName("comboBox_2")
        self.comboBox_natureza .addItems(self.natureza)

        self.label_quantidade = QtWidgets.QLabel(self.frame_lista)
        self.label_quantidade.setGeometry(QtCore.QRect(180, 190, 81, 21))
        self.label_quantidade.setMaximumSize(QtCore.QSize(81, 21))
        self.label_quantidade.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_quantidade.setAlignment(QtCore.Qt.AlignCenter)
        self.label_quantidade.setObjectName("label_quantidade")

        self.btn_buscar_grafico = QtWidgets.QPushButton(self.frame_lista)
        self.btn_buscar_grafico.setGeometry(QtCore.QRect(70, 320, 150, 43))
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/button/icon_grafico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_buscar_grafico.setIcon(icon4)
        self.btn_buscar_grafico.setIconSize(QtCore.QSize(35, 35))
        self.btn_buscar_grafico.setObjectName("btn_buscar_grafico")

        self.label_comparacao = QtWidgets.QLabel(self.frame_lista)
        self.label_comparacao.setGeometry(QtCore.QRect(60, 400, 230, 16))
        self.label_comparacao.setMaximumSize(QtCore.QSize(230, 16))
        self.label_comparacao.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 90 9pt \"MS Shell Dlg 2\";")
        self.label_comparacao.setObjectName("label_cidade1")

        self.label_cidade1 = QtWidgets.QLabel(self.frame_lista)
        self.label_cidade1.setGeometry(QtCore.QRect(30, 425, 91, 16))
        self.label_cidade1.setMaximumSize(QtCore.QSize(91, 16))
        self.label_cidade1.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_cidade1.setObjectName("label_cidade1")

        self.comboBox_cidade1 = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_cidade1.setGeometry(QtCore.QRect(30, 450, 251, 21))
        self.comboBox_cidade1.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_cidade1.setObjectName("comboBox_cidade1")
        self.comboBox_cidade1.addItems(self.cidade)

        self.label_cidade2 = QtWidgets.QLabel(self.frame_lista)
        self.label_cidade2.setGeometry(QtCore.QRect(30, 475, 91, 16))
        self.label_cidade2.setMaximumSize(QtCore.QSize(91, 16))
        self.label_cidade2.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_cidade2.setObjectName("label_cidade1")

        self.comboBox_cidade2 = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_cidade2.setGeometry(QtCore.QRect(30, 500, 251, 21))
        self.comboBox_cidade2.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_cidade2.setObjectName("comboBox_cidade2")
        self.comboBox_cidade2.addItems(self.cidade)

        self.label_natureza2 = QtWidgets.QLabel(self.frame_lista)
        self.label_natureza2.setGeometry(QtCore.QRect(30, 525, 150, 16))
        self.label_natureza2.setMaximumSize(QtCore.QSize(150, 16))
        self.label_natureza2.setStyleSheet("background-color: rgb(255, 255, 255,0.0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_natureza2.setObjectName("label_cidade1")

        self.comboBox_natureza2 = QtWidgets.QComboBox(self.frame_lista)
        self.comboBox_natureza2.setGeometry(QtCore.QRect(30, 550, 251, 21))
        self.comboBox_natureza2.setMaximumSize(QtCore.QSize(251, 21))
        self.comboBox_natureza2.setObjectName("comboBox_cidade2")
        self.comboBox_natureza2.addItems(self.cidade)

        self.btn_comparar = QtWidgets.QPushButton(self.frame_lista)
        self.btn_comparar.setGeometry(QtCore.QRect(50, 600, 200, 43))
        self.btn_comparar.setMaximumSize(QtCore.QSize(200, 100))
        self.btn_comparar.setStyleSheet("QPushButton{\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/button/icon_grafico.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_comparar.setIcon(icon4)
        self.btn_comparar.setIconSize(QtCore.QSize(35, 35))
        self.btn_comparar.setObjectName("btn_comparar")


        #frame error
        self.frame_erro = QtWidgets.QFrame(self.frame_lista)
        self.frame_erro.setGeometry(QtCore.QRect(30, 0, 250, 41))
        self.frame_erro.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_erro.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"border-radius:5px;")
        self.frame_erro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_erro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_erro.setObjectName("frame_erro")

        self.label_error = QtWidgets.QLabel(self.frame_erro)
        self.label_error.setGeometry(QtCore.QRect(0, 0, 250, 41))
        self.label_error.setMaximumSize(QtCore.QSize(250, 41))
        self.label_error.setStyleSheet("QLabel{\n"
"image: url(:/logo/quadroT.png);\n"
"    background-color: rgb(226, 75, 0);\n"
"}")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")

        self.btn_x = QtWidgets.QPushButton(self.frame_erro)
        self.btn_x.setGeometry(QtCore.QRect(200, 10, 31, 20))
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/button/marca-x (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_x.setIcon(icon5)
        self.btn_x.setIconSize(QtCore.QSize(35, 35))
        self.btn_x.setObjectName("btn_x")
        self.horizontalLayout.addWidget(self.frame_lista)
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.frame_erro.hide()


        #acao do buttons
        self.btn_x.clicked.connect(lambda: self.frame_erro.hide())
        self.button_Mdataset.clicked.connect(lambda: Ui_MainWindow.toggleMenu(self,300,True))
        self.btn_ocorrencias.clicked.connect(self.ocorrencia)
        self.btn_campinas_2.clicked.connect(self.lista)
        self.btn_buscar_grafico.clicked.connect(self.opcao_selecionada)

        self.btn_taxa.clicked.connect(self.taxa_crime)
        self.btn_policia.clicked.connect(self.policia_prod)
        self.btn_comparar.clicked.connect(self.duas_cidades)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_Mdataset.setText(_translate("MainWindow", "MENU DATASET"))
        self.label_dataset.setText(_translate("MainWindow", "Dataset Criminalidade"))
        self.btn_taxa.setText(_translate("MainWindow", "Taxa de Criminalidade"))
        self.btn_ocorrencias.setText(_translate("MainWindow", " Ocorrencias "))
        self.btn_policia.setText(_translate("MainWindow", "Produtividade Policial"))
        self.btn_grande_sp_2.setText(_translate("MainWindow", "Grande Sao Paulo"))
        self.btn_sorocaba_2.setText(_translate("MainWindow", "Sorocaba"))
        self.btn_registro_2.setText(_translate("MainWindow", "Registro"))
        self.btn_taubate_2.setText(_translate("MainWindow", "Taubate"))
        self.btn_bauru_2.setText(_translate("MainWindow", "Bauru"))
        self.btn_ribeiraoPreto_2.setText(_translate("MainWindow", "Ribeirao Preto"))
        self.btn_aracatuba_2.setText(_translate("MainWindow", "Aracatuba"))
        self.btn_saoJoseBoaVista_2.setText(_translate("MainWindow", "Sao Joao da Boa vista"))
        self.btn_saojoseriopreto_2.setText(_translate("MainWindow", "Sao jose do rio Preto"))
        self.btn_campinas_2.setText(_translate("MainWindow", "Campinas"))
        self.btn_marilia_2.setText(_translate("MainWindow", "Marilia"))
        self.btn_Pprudente_2.setText(_translate("MainWindow", "Presidente Prudente"))
        self.btn_barretos_2.setText(_translate("MainWindow", "Barretos"))
        self.btn_franca_2.setText(_translate("MainWindow", "Franca"))
        self.btn_santista_2.setText(_translate("MainWindow", "Baixada Santista"))
        self.btn_piracicaba_2.setText(_translate("MainWindow", "Pracicaba"))
        self.btn_araraquara_2.setText(_translate("MainWindow", "Araraquara"))
        self.label_estado.setText(_translate("MainWindow", "ESTADO DE SAO PAULO"))
        self.label_Municipio.setText(_translate("MainWindow", "Municipio:"))
        self.label_comparacao.setText(_translate("MainWindow", "GRAFICOS PARA DUAS CIDADES"))
        self.label_cidade1.setText(_translate("MainWindow", "Primeira Cidade:"))
        self.label_cidade2.setText(_translate("MainWindow", "Segunda Cidade:"))
        self.label_busca.setText(_translate("MainWindow", "Tipo de Busca:"))
        self.label__populacao.setText(_translate("MainWindow", "POPULACAO:"))
        self.label_quantidade.setText(_translate("MainWindow", "Quantidade"))
        self.label_natureza2.setText(_translate("MainWindow", "Tipo de comparacao: "))
        self.btn_buscar_grafico.setText(_translate("MainWindow", "Buscar Grafico"))
        self.btn_comparar.setText(_translate("MainWindow", "Buscar por Compararcao"))
        self.label_error.setText(_translate("MainWindow", "ERRO ao selecionar!"))
import icon_sp2


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
