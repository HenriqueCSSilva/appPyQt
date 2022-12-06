from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
import sys
import os
import base
import pandas as pd


class Janela(QtWidgets.QMainWindow, base.Ui_MainWindow):
    def __init__(self, parent=None):

        super(Janela, self).__init__(parent)
        self.setupUi(self)
        self.Btn_botao_exibir.clicked.connect(self.exibir) 
        self.Btn_botao_3pontos.clicked.connect(self.abrirPasta)
        self.Btn_botao_mostrar.clicked.connect(self.mostrar)
        
        
    def exibir(self): # função botão exibir
        
        patrimonio = self.txt_patrimonio.text()
        modelo = self.txt_modelo.text()
        processador = self.txt_processador.text()
        memoria = self.txt_memoria.text()
        status = self.txt_status.text()
        usuario = self.txt_usuario.text()
        setor = self.txt_usuario.text()

        campos = [patrimonio, modelo, processador, memoria, status, usuario, setor]

        for item in campos:
            if(item == '' or item == None):
                QMessageBox.about(self, "AVISO" , "Campo vazio! \n" "por favor, preencha os campos")
                return
        else:
            print (patrimonio,"\n",modelo,"\n",processador,"\n",memoria,"\n",status,"\n",status,"\n",usuario,"\n",setor)
    
    def abrirPasta(self): # função botão ...
        path = os.getcwd() + '\\base_de_dados' 
        os.startfile(path)

    def mostrar(self): # função botão mostar
        path = os.getcwd() + '\\base_de_dados' + '\\basePatrimonio.xlsx'
        tabela = pd.read_excel(path)
        print(tabela)
        
def main():
    app = QApplication(sys.argv)
    form = Janela()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()