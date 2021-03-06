import os
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
        #funcao para exibir a tabela com dados do csv
    def opcao_selecionada(self):
        tabela = self.comboBox_tabela.currentText()
        natureza = self.comboBox_natureza.currentText()
        cidade = self.comboBox_cidade.currentText() 
        #verifica se os itens no combobox foram selecionados
        if (tabela == "selecione") or (natureza == "selecione") or (cidade == "selecione"):
            self.frame_erro.show()
            self.label_erro.show()
                      
        else:   
            self.frame_erro.hide() 
            #busca o dados da tabela csv             
            dataset = pd.read_csv("projeto_dataset/csv/" + tabela, encoding="latin-1")
            #busca os dados da tabela apartir do tipo de natureza em qual cidade e pelo periodo dos anos contidos na tabela    
            dados = dataset[(dataset.Natureza == natureza) & (dataset.Cidade == cidade)].sort_values("Ano")
            #exibe a tabela no terminal
            print("TABELA\n", dados.head(20))
            #envia os dados para a construcao do grafico com matplotlib    
            plt.figure(figsize = (10,5))
            sns.barplot(x = "Ano", y="Total",data = dados, color="blue")
            plt.xticks(rotation=90)
            plt.title(natureza +" "+ cidade,fontsize = 14)
            plt.xlabel("Ano", fontsize = 10)
            plt.ylabel("numeros de:"+ natureza, fontsize = 10);
            #apresenta o grafico
            plt.show()

    #funcoa que inicia a construcao da tela     
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1100, 800))
        icon = QtGui.QIcon()
        #adiciona um icon no canto superior esquerdo da janela principal
        icon.addPixmap(QtGui.QPixmap(":/login/images/datasets.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.centralwidget.setObjectName("centralwidget")

        self.framefundo = QtWidgets.QFrame(self.centralwidget)
        self.framefundo.setGeometry(QtCore.QRect(-1, -1, 1100, 700))
        self.framefundo.setMinimumSize(QtCore.QSize(1000, 600))
        self.framefundo.setMaximumSize(QtCore.QSize(1100, 700))
        self.framefundo.setStyleSheet("\n"
"\n"
"QFrame{\n"
"background-color: rgb(0, 118, 173);\n"
"\n"
"}")
        self.framefundo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.framefundo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framefundo.setObjectName("framefundo")

        self.frame_inferior2 = QtWidgets.QFrame(self.framefundo)
        self.frame_inferior2.setGeometry(QtCore.QRect(50, 550, 1000, 80))
        self.frame_inferior2.setAutoFillBackground(False)
        self.frame_inferior2.setStyleSheet("QFrame{\n"
"border-radius:50px;\n"
"    background-color: rgb(28, 138, 219);\n"
"\n"
"}\n"
"QFrame:hover{\n"
"border:2px solid;\n"
"border-right-color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.frame_inferior2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_inferior2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inferior2.setObjectName("frame_inferior2")

        self.comboBox_tabela = QtWidgets.QComboBox(self.frame_inferior2)
        self.comboBox_tabela.setGeometry(QtCore.QRect(30, 40, 230, 20))
        self.comboBox_tabela.setStyleSheet("QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"    background-color: rgb(232, 232, 232);\n"
"}")
        self.comboBox_tabela.setObjectName("comboBox_tabela")
        self.comboBox_tabela.addItems(["selecione","ocorrencias_mensais_crimes_sp.csv"])


        self.comboBox_natureza = QtWidgets.QComboBox(self.frame_inferior2)
        self.comboBox_natureza.setGeometry(QtCore.QRect(290, 40, 230, 20))
        self.comboBox_natureza.setStyleSheet("QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"    background-color: rgb(232, 232, 232);\n"
"}")
        self.comboBox_natureza.setObjectName("comboBox_natureza")
        self.comboBox_natureza.addItems(["selecione",
                                  "HOMIC??DIO DOLOSO",
                                  "N?? DE V??TIMAS EM HOMIC??DIO DOLOSO",
                                  "HOMIC??DIO DOLOSO POR ACIDENTE DE TR??NSITO",
                                  "N?? DE V??TIMAS EM HOMIC??DIO DOLOSO POR ACIDENTE DE TR??NSITO",
                                  "HOMIC??DIO CULPOSO POR ACIDENTE DE TR??NSITO",
                                  "HOMIC??DIO CULPOSO OUTROS",
                                  "TENTATIVA DE HOMIC??DIO",
                                  "LES??O CORPORAL SEGUIDA DE MORTE",
                                  "LES??O CORPORAL DOLOSA",
                                  "LES??O CORPORAL CULPOSA POR ACIDENTE DE TR??NSITO",
                                  "LES??O CORPORAL CULPOSA - OUTRAS",
                                  "LATROC??NIO",
                                  "N?? DE V??TIMAS EM LATROC??NIO",
                                  "TOTAL DE ESTUPRO",
                                  "ESTUPRO",
                                  "ESTUPRO DE VULNER??VEL",
                                  "TOTAL DE ROUBO - OUTROS",
                                  "ROUBO - OUTROS",
                                  "ROUBO DE VE??CULO",
                                  "ROUBO A BANCO",
                                  "ROUBO DE CARGA",
                                  "FURTO - OUTROS",
                                  "FURTO DE VE??CULO"])

        self.comboBox_cidade = QtWidgets.QComboBox(self.frame_inferior2)
        self.comboBox_cidade.setGeometry(QtCore.QRect(550, 40, 230, 20))
        self.comboBox_cidade.setStyleSheet("QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"    background-color: rgb(232, 232, 232);\n"
"}")
        self.comboBox_cidade.setObjectName("comboBox_cidade")
        self.comboBox_cidade.addItems(["selecione",
                                  "S??o Paulo",
                                  "Franco da Rocha",
                                  "S??o Louren??o da Serra",
                                  "Suzano",
                                  "Tabo??o da Serra",
                                  "Vargem Grande Paulista",
                                  "Aparecida",
                                  "Areias",
                                  "Bragan??a Paulista",
                                  "Santo Andr??",
                                  "Campinas"
                                  "Diadema",
                                  "Itanha??m",
                                  "Itapecerica da Serra",
                                  "Itapevi",
                                  "Cotia",
                                  "Ilhabela"])

        self.pushButton_consulta = QtWidgets.QPushButton(self.frame_inferior2)
        self.pushButton_consulta.setGeometry(QtCore.QRect(840, 30, 101, 35))
        self.pushButton_consulta.setStyleSheet("QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"    background-color: rgb(16, 80, 127);\n"
"border: 2px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 85, 127);\n"
"border-color: rgb(255, 255, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 100), stop:1 rgba(255, 255, 150, 100));\n"
"}\n"
"QPushButton:pressed{\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-width:3px;\n"
"border-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"")
        self.pushButton_consulta.setObjectName("pushButton_consulta")

        self.frame_inferior_2 = QtWidgets.QFrame(self.framefundo)
        self.frame_inferior_2.setGeometry(QtCore.QRect(52, 547, 996, 31))
        self.frame_inferior_2.setStyleSheet("background-color: rgb(28, 138, 219);")
        self.frame_inferior_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_inferior_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inferior_2.setObjectName("frame_inferior_2")

        self.label_tabela = QtWidgets.QLabel(self.frame_inferior_2)
        self.label_tabela.setGeometry(QtCore.QRect(30, 10, 200, 20))
        self.label_tabela.setStyleSheet("font: 75 12pt \"Microsoft New Tai Lue\";\n""")
        self.label_tabela.setObjectName("label_tabela")

        self.label_natureza = QtWidgets.QLabel(self.frame_inferior_2)
        self.label_natureza.setGeometry(QtCore.QRect(290, 10, 200, 20))
        self.label_natureza.setStyleSheet("font: 75 12pt \"Microsoft New Tai Lue\";\n""")
        self.label_natureza.setObjectName("label_natureza")

        self.label_cidade = QtWidgets.QLabel(self.frame_inferior_2)
        self.label_cidade.setGeometry(QtCore.QRect(550, 10, 200, 20))
        self.label_cidade.setStyleSheet("font: 75 12pt \"Microsoft New Tai Lue\";\n""")
        self.label_cidade.setObjectName("label_cidade")

        self.frame_superior = QtWidgets.QFrame(self.framefundo)
        self.frame_superior.setGeometry(QtCore.QRect(-1, 0, 1100, 80))
        self.frame_superior.setMaximumSize(QtCore.QSize(1100, 80))
        self.frame_superior.setStyleSheet("background-color: rgb(16, 80, 127);")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")

        self.label_titulo = QtWidgets.QLabel(self.frame_superior)
        self.label_titulo.setGeometry(QtCore.QRect(277, 30, 545, 30))
        self.label_titulo.setStyleSheet("font: 75 22pt \"MS Sans Serif\";\n""color: rgb(255, 255, 255);")
        self.label_titulo.setObjectName("label_titulo")

        self.frame_erro = QtWidgets.QFrame(self.frame_superior)
        self.frame_erro.setGeometry(QtCore.QRect(350, 0, 401, 31))
        self.frame_erro.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"border-radius:5px;")
        self.frame_erro.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_erro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_erro.setObjectName("frame_erro")
        #inicia o frame de forma escondida
        self.frame_erro.hide()

        self.label_erro = QtWidgets.QLabel(self.frame_erro)
        self.label_erro.setGeometry(QtCore.QRect(0, 0, 371, 29))
        self.label_erro.setStyleSheet("color: rgb(48, 48, 48);")
        self.label_erro.setAlignment(QtCore.Qt.AlignCenter)
        self.label_erro.setObjectName("label_erro")
        #inicia o label de forma escondida
        self.label_erro.hide()

        self.button_close = QtWidgets.QPushButton(self.frame_erro)
        self.button_close.setGeometry(QtCore.QRect(360, 0, 30, 30))
        self.button_close.setMaximumSize(QtCore.QSize(30, 30))
        self.button_close.setAutoFillBackground(False)
        self.button_close.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"    background-image: url(:/Close_Image/images/marca-x (1).png);\n"
"background-repeat: no-repeat;\n"
"background-position:center;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 0, 0);\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"border-color: rgb(0, 0, 0);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"}\n"
"\n"
"")
        self.button_close.setText("")
        self.button_close.setIconSize(QtCore.QSize(20, 20))
        self.button_close.setAutoRepeat(False)
        self.button_close.setObjectName("button_close")

        self.frame_logo = QtWidgets.QFrame(self.framefundo)
        self.frame_logo.setGeometry(QtCore.QRect(315, 100, 470, 340))
        self.frame_logo.setStyleSheet("QFrame{\n"
"image: url(:/dataset/images/logo_datasets.png);\n"
"border-radius: 100px\n"
"\n"
"\n"
"}")
        self.frame_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #recebe o chamado do botao 
        self.pushButton_consulta.clicked.connect(self.opcao_selecionada)
        self.button_close.clicked.connect(lambda: self.frame_erro.hide())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DATASET"))
        self.pushButton_consulta.setText(_translate("MainWindow", "CONSULTAR"))
        self.label_tabela.setText(_translate("MainWindow", "Selecionar Tabela de Dados"))
        self.label_natureza.setText(_translate("MainWindow", "Selecionar Natureza"))
        self.label_cidade.setText(_translate("MainWindow", "Selecionar Cidade"))
        self.label_titulo.setText(_translate("MainWindow", "Consulta do Dataset Crime em Sao Paulo"))
        self.label_erro.setText(_translate("MainWindow", "ERROR OS DADOS NAO FORAM SELECIONADOS"))
import files_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
