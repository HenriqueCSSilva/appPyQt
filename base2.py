# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SegundaJanela(object):
    def setupUi(self, SegundaJanela):
        SegundaJanela.setObjectName("SegundaJanela")
        SegundaJanela.resize(1363, 670)
        self.centralwidget = QtWidgets.QWidget(SegundaJanela)
        self.centralwidget.setObjectName("centralwidget")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setGeometry(QtCore.QRect(23, 10, 41, 21))
        self.label_nome.setStyleSheet("font-family:\"MS Shell Dlg 2\";")
        self.label_nome.setObjectName("label_nome")
        self.tabela_pc = QtWidgets.QTableWidget(self.centralwidget)
        self.tabela_pc.setGeometry(QtCore.QRect(11, 72, 1341, 581))
        self.tabela_pc.setObjectName("tabela_pc")
        self.tabela_pc.setColumnCount(16)
        self.tabela_pc.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela_pc.setHorizontalHeaderItem(15, item)
        self.txt_nome_buscar = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nome_buscar.setGeometry(QtCore.QRect(21, 30, 81, 21))
        self.txt_nome_buscar.setStyleSheet("background-color:rgb(254, 254, 254);")
        self.txt_nome_buscar.setText("")
        self.txt_nome_buscar.setObjectName("txt_nome_buscar")
        self.btn_limpar_nome = QtWidgets.QPushButton(self.centralwidget)
        self.btn_limpar_nome.setGeometry(QtCore.QRect(182, 30, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.btn_limpar_nome.setFont(font)
        self.btn_limpar_nome.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"\n"
"font-family:\"Small Fonts\";\n"
"\n"
"font-size:75 7pt \"MS Shell Dlg 2\";\n"
"font: 63 7pt \"Sitka Text Semibold\";")
        self.btn_limpar_nome.setObjectName("btn_limpar_nome")
        self.btn_buscar_nome = QtWidgets.QPushButton(self.centralwidget)
        self.btn_buscar_nome.setGeometry(QtCore.QRect(120, 30, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Sitka Text Semibold")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.btn_buscar_nome.setFont(font)
        self.btn_buscar_nome.setStyleSheet("background-color: rgb(185, 185, 185);\n"
"\n"
"font-family:\"Small Fonts\";\n"
"\n"
"font-size:75 7pt \"MS Shell Dlg 2\";\n"
"font: 63 7pt \"Sitka Text Semibold\";")
        self.btn_buscar_nome.setObjectName("btn_buscar_nome")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(37, 86, 1291, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        SegundaJanela.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SegundaJanela)
        self.statusbar.setObjectName("statusbar")
        SegundaJanela.setStatusBar(self.statusbar)

        self.retranslateUi(SegundaJanela)
        QtCore.QMetaObject.connectSlotsByName(SegundaJanela)

    def retranslateUi(self, SegundaJanela):
        _translate = QtCore.QCoreApplication.translate
        SegundaJanela.setWindowTitle(_translate("SegundaJanela", "Busca PC "))
        self.label_nome.setText(_translate("SegundaJanela", "Nome:"))
        item = self.tabela_pc.verticalHeaderItem(0)
        item.setText(_translate("SegundaJanela", "1"))
        item = self.tabela_pc.verticalHeaderItem(1)
        item.setText(_translate("SegundaJanela", "2"))
        item = self.tabela_pc.verticalHeaderItem(2)
        item.setText(_translate("SegundaJanela", "3"))
        item = self.tabela_pc.verticalHeaderItem(3)
        item.setText(_translate("SegundaJanela", "4"))
        item = self.tabela_pc.verticalHeaderItem(4)
        item.setText(_translate("SegundaJanela", "5"))
        item = self.tabela_pc.verticalHeaderItem(5)
        item.setText(_translate("SegundaJanela", "6"))
        item = self.tabela_pc.verticalHeaderItem(6)
        item.setText(_translate("SegundaJanela", "7"))
        item = self.tabela_pc.verticalHeaderItem(7)
        item.setText(_translate("SegundaJanela", "8"))
        item = self.tabela_pc.verticalHeaderItem(8)
        item.setText(_translate("SegundaJanela", "9"))
        item = self.tabela_pc.verticalHeaderItem(9)
        item.setText(_translate("SegundaJanela", "10"))
        item = self.tabela_pc.verticalHeaderItem(10)
        item.setText(_translate("SegundaJanela", "11"))
        item = self.tabela_pc.verticalHeaderItem(11)
        item.setText(_translate("SegundaJanela", "12"))
        item = self.tabela_pc.verticalHeaderItem(12)
        item.setText(_translate("SegundaJanela", "13"))
        item = self.tabela_pc.verticalHeaderItem(13)
        item.setText(_translate("SegundaJanela", "14"))
        item = self.tabela_pc.verticalHeaderItem(14)
        item.setText(_translate("SegundaJanela", "15"))
        item = self.tabela_pc.verticalHeaderItem(15)
        item.setText(_translate("SegundaJanela", "16"))
        item = self.tabela_pc.verticalHeaderItem(16)
        item.setText(_translate("SegundaJanela", "17"))
        item = self.tabela_pc.verticalHeaderItem(17)
        item.setText(_translate("SegundaJanela", "18"))
        item = self.tabela_pc.verticalHeaderItem(18)
        item.setText(_translate("SegundaJanela", "19"))
        item = self.tabela_pc.verticalHeaderItem(19)
        item.setText(_translate("SegundaJanela", "20"))
        item = self.tabela_pc.horizontalHeaderItem(0)
        item.setText(_translate("SegundaJanela", "Nome"))
        item = self.tabela_pc.horizontalHeaderItem(1)
        item.setText(_translate("SegundaJanela", "Patrimonio"))
        item = self.tabela_pc.horizontalHeaderItem(2)
        item.setText(_translate("SegundaJanela", "Tipo"))
        item = self.tabela_pc.horizontalHeaderItem(3)
        item.setText(_translate("SegundaJanela", "Estação"))
        item = self.tabela_pc.horizontalHeaderItem(4)
        item.setText(_translate("SegundaJanela", "Descrição"))
        item = self.tabela_pc.horizontalHeaderItem(5)
        item.setText(_translate("SegundaJanela", "UF"))
        item = self.tabela_pc.horizontalHeaderItem(6)
        item.setText(_translate("SegundaJanela", "Modelo"))
        item = self.tabela_pc.horizontalHeaderItem(7)
        item.setText(_translate("SegundaJanela", "Marca"))
        item = self.tabela_pc.horizontalHeaderItem(8)
        item.setText(_translate("SegundaJanela", "N° Modelo"))
        item = self.tabela_pc.horizontalHeaderItem(9)
        item.setText(_translate("SegundaJanela", "Processador"))
        item = self.tabela_pc.horizontalHeaderItem(10)
        item.setText(_translate("SegundaJanela", "N° Série"))
        item = self.tabela_pc.horizontalHeaderItem(11)
        item.setText(_translate("SegundaJanela", "Email"))
        item = self.tabela_pc.horizontalHeaderItem(12)
        item.setText(_translate("SegundaJanela", "Memória"))
        item = self.tabela_pc.horizontalHeaderItem(13)
        item.setText(_translate("SegundaJanela", "Status"))
        item = self.tabela_pc.horizontalHeaderItem(14)
        item.setText(_translate("SegundaJanela", "Condições"))
        item = self.tabela_pc.horizontalHeaderItem(15)
        item.setText(_translate("SegundaJanela", "SSD/HDD"))
        self.btn_limpar_nome.setText(_translate("SegundaJanela", "LIMPAR"))
        self.btn_buscar_nome.setText(_translate("SegundaJanela", "BUSCAR"))
