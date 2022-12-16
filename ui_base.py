# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\GITHUB\Python\appPyQt\base.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 841, 501))
        self.tabWidget.setStyleSheet("background-color:rgb(167, 167, 167);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_geral = QtWidgets.QWidget()
        self.tab_geral.setObjectName("tab_geral")
        self.txt_patrimonio = QtWidgets.QLineEdit(self.tab_geral)
        self.txt_patrimonio.setGeometry(QtCore.QRect(10, 31, 31, 21))
        self.txt_patrimonio.setStyleSheet("background-color:rgb(254, 254, 254);")
        self.txt_patrimonio.setText("")
        self.txt_patrimonio.setObjectName("txt_patrimonio")
        self.label_patrimonio = QtWidgets.QLabel(self.tab_geral)
        self.label_patrimonio.setGeometry(QtCore.QRect(11, 10, 61, 21))
        self.label_patrimonio.setStyleSheet("font-family:\"MS Shell Dlg 2\";")
        self.label_patrimonio.setObjectName("label_patrimonio")
        self.txt_memoria = QtWidgets.QLineEdit(self.tab_geral)
        self.txt_memoria.setGeometry(QtCore.QRect(178, 150, 51, 21))
        self.txt_memoria.setStyleSheet("background-color:rgb(254, 254, 254);")
        self.txt_memoria.setText("")
        self.txt_memoria.setObjectName("txt_memoria")
        self.txt_modelo = QtWidgets.QLineEdit(self.tab_geral)
        self.txt_modelo.setGeometry(QtCore.QRect(10, 150, 81, 21))
        self.txt_modelo.setStyleSheet("background-color:rgb(254, 254, 254);")
        self.txt_modelo.setText("")
        self.txt_modelo.setObjectName("txt_modelo")
        self.txt_processador = QtWidgets.QLineEdit(self.tab_geral)
        self.txt_processador.setGeometry(QtCore.QRect(99, 150, 71, 21))
        self.txt_processador.setStyleSheet("background-color:rgb(254, 254, 254);")
        self.txt_processador.setText("")
        self.txt_processador.setObjectName("txt_processador")
        self.label_modelo = QtWidgets.QLabel(self.tab_geral)
        self.label_modelo.setGeometry(QtCore.QRect(12, 129, 41, 21))
        self.label_modelo.setStyleSheet("font-family:\"MS Shell Dlg 2\";")
        self.label_modelo.setObjectName("label_modelo")
        self.label_processador = QtWidgets.QLabel(self.tab_geral)
        self.label_processador.setGeometry(QtCore.QRect(100, 129, 61, 21))
        self.label_processador.setStyleSheet("font-family:\"MS Shell Dlg 2\";")
        self.label_processador.setObjectName("label_processador")
        self.label_memoria = QtWidgets.QLabel(self.tab_geral)
        self.label_memoria.setGeometry(QtCore.QRect(180, 129, 51, 21))
        self.label_memoria.setStyleSheet("font-family:\"MS Shell Dlg 2\";")
        self.label_memoria.setObjectName("label_memoria")
        self.btn_detalhes = QtWidgets.QPushButton(self.tab_geral)
        self.btn_detalhes.setGeometry(QtCore.QRect(52, 30, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.btn_detalhes.setFont(font)
        self.btn_detalhes.setStyleSheet("background-color:rgb(167, 167, 167);\n"
"\n"
"font-family:\"Small Fonts\";\n"
"\n"
"font-size:75 6pt \"MS Shell Dlg 2\";")
        self.btn_detalhes.setObjectName("btn_detalhes")
        self.btn_3pontos = QtWidgets.QPushButton(self.tab_geral)
        self.btn_3pontos.setGeometry(QtCore.QRect(71, 220, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3pontos.setFont(font)
        self.btn_3pontos.setStyleSheet("background-color:rgb(167, 167, 167);\n"
"\n"
"font-family:\"Small Fonts\";\n"
"font-size: 12pt\n"
"")
        self.btn_3pontos.setObjectName("btn_3pontos")
        self.txt_status = QtWidgets.QLineEdit(self.tab_geral)
        self.txt_status.setGeometry(QtCore.QRect(238, 151, 41, 21))
        self.txt_status.setStyleSheet("background-color:rgb(254, 254, 254);")
        self.txt_status.setText("")
        self.txt_status.setObjectName("txt_status")
        self.txt_setor = QtWidgets.QLineEdit(self.tab_geral)
        self.txt_setor.setGeometry(QtCore.QRect(270, 90, 131, 21))
        self.txt_setor.setStyleSheet("background-color:rgb(254, 254, 254);")
        self.txt_setor.setText("")
        self.txt_setor.setObjectName("txt_setor")
        self.txt_usuario = QtWidgets.QLineEdit(self.tab_geral)
        self.txt_usuario.setGeometry(QtCore.QRect(11, 90, 251, 21))
        self.txt_usuario.setStyleSheet("background-color:rgb(254, 254, 254);")
        self.txt_usuario.setText("")
        self.txt_usuario.setObjectName("txt_usuario")
        self.label_setor = QtWidgets.QLabel(self.tab_geral)
        self.label_setor.setGeometry(QtCore.QRect(270, 70, 31, 21))
        self.label_setor.setStyleSheet("font-family:\"MS Shell Dlg 2\";")
        self.label_setor.setObjectName("label_setor")
        self.label_usuario = QtWidgets.QLabel(self.tab_geral)
        self.label_usuario.setGeometry(QtCore.QRect(13, 70, 41, 21))
        self.label_usuario.setStyleSheet("font-family:\"MS Shell Dlg 2\";")
        self.label_usuario.setObjectName("label_usuario")
        self.label_status = QtWidgets.QLabel(self.tab_geral)
        self.label_status.setGeometry(QtCore.QRect(240, 130, 41, 21))
        self.label_status.setStyleSheet("font-family:\"MS Shell Dlg 2\";")
        self.label_status.setObjectName("label_status")
        self.btn_mostrar = QtWidgets.QPushButton(self.tab_geral)
        self.btn_mostrar.setGeometry(QtCore.QRect(12, 220, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(6)
        self.btn_mostrar.setFont(font)
        self.btn_mostrar.setStyleSheet("background-color:rgb(167, 167, 167);\n"
"font-family:\"Small Fonts\";\n"
"\n"
"font-size: 6pt")
        self.btn_mostrar.setObjectName("btn_mostrar")
        self.btn_limpar = QtWidgets.QPushButton(self.tab_geral)
        self.btn_limpar.setGeometry(QtCore.QRect(110, 30, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.btn_limpar.setFont(font)
        self.btn_limpar.setStyleSheet("background-color:rgb(167, 167, 167);\n"
"font-family:\"Small Fonts\";\n"
"\n"
"font-size: 6pt")
        self.btn_limpar.setObjectName("btn_limpar")
        self.line = QtWidgets.QFrame(self.tab_geral)
        self.line.setGeometry(QtCore.QRect(0, 200, 411, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget.addTab(self.tab_geral, "")
        self.tab_pesquisa = QtWidgets.QWidget()
        self.tab_pesquisa.setObjectName("tab_pesquisa")
        self.label_nome = QtWidgets.QLabel(self.tab_pesquisa)
        self.label_nome.setGeometry(QtCore.QRect(20, 8, 41, 21))
        self.label_nome.setStyleSheet("font-family:\"MS Shell Dlg 2\";")
        self.label_nome.setObjectName("label_nome")
        self.txt_nome_buscar = QtWidgets.QLineEdit(self.tab_pesquisa)
        self.txt_nome_buscar.setGeometry(QtCore.QRect(20, 28, 81, 21))
        self.txt_nome_buscar.setStyleSheet("background-color:rgb(254, 254, 254);")
        self.txt_nome_buscar.setText("")
        self.txt_nome_buscar.setObjectName("txt_nome_buscar")
        self.btn_buscar_nome = QtWidgets.QPushButton(self.tab_pesquisa)
        self.btn_buscar_nome.setGeometry(QtCore.QRect(109, 28, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.btn_buscar_nome.setFont(font)
        self.btn_buscar_nome.setStyleSheet("background-color:rgb(167, 167, 167);\n"
"\n"
"font-family:\"Small Fonts\";\n"
"\n"
"font-size:75 7pt \"MS Shell Dlg 2\";")
        self.btn_buscar_nome.setObjectName("btn_buscar_nome")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_pesquisa)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 731, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(11)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.btn_limpar_nome = QtWidgets.QPushButton(self.tab_pesquisa)
        self.btn_limpar_nome.setGeometry(QtCore.QRect(170, 28, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.btn_limpar_nome.setFont(font)
        self.btn_limpar_nome.setStyleSheet("background-color:rgb(167, 167, 167);\n"
"\n"
"font-family:\"Small Fonts\";\n"
"\n"
"font-size:75 7pt \"MS Shell Dlg 2\";")
        self.btn_limpar_nome.setObjectName("btn_limpar_nome")
        self.tabWidget.addTab(self.tab_pesquisa, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Controle TI"))
        self.label_patrimonio.setText(_translate("MainWindow", "Patrimonio:"))
        self.label_modelo.setText(_translate("MainWindow", "Modelo:"))
        self.label_processador.setText(_translate("MainWindow", "Processador:"))
        self.label_memoria.setText(_translate("MainWindow", "Memoria:"))
        self.btn_detalhes.setText(_translate("MainWindow", "BUSCAR"))
        self.btn_3pontos.setText(_translate("MainWindow", "..."))
        self.label_setor.setText(_translate("MainWindow", "Setor:"))
        self.label_usuario.setText(_translate("MainWindow", "Usuario:"))
        self.label_status.setText(_translate("MainWindow", "Status:"))
        self.btn_mostrar.setText(_translate("MainWindow", "MOSTRAR"))
        self.btn_limpar.setText(_translate("MainWindow", "LIMPAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_geral), _translate("MainWindow", "Geral"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.btn_buscar_nome.setText(_translate("MainWindow", "BUSCAR"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Patrimonio"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Modelo"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Processador"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Memoria"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Usuario"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Setor"))
        self.btn_limpar_nome.setText(_translate("MainWindow", "LIMPAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_pesquisa), _translate("MainWindow", "Pesquisa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab_"))
