from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
import sys
import os
import base

class Janela(QtWidgets.QMainWindow, base.Ui_MainWindow, ):
    def __init__(self, parent=None):
        super(Janela, self).__init__(parent)
        self.setupUi(self)
        self.Btn_botao1_2.clicked.connect(self.exibir) 
        self.Btn_botao1_3.clicked.connect(self.abrirPasta)
        
        
    def exibir (self): # função botão exibir
        nome = self.txt_nome.text()
        patrimonio = self.txt_patrimonio.text()
        email = self.txt_email.text()
        estado = self.txt_estado.text()
        
        if(email == '' or email == None):
            QMessageBox.about(self, "AVISO" , "Verifique o campo de e-mail" )
        else:
            print(nome,"\n",patrimonio,"\n",email,"\n",estado)
        #def  clickMethod (self) :
            #QMessageBox.about(self, "AVISO" , "O botão foi clicado" )
    
    def abrirPasta(self): # função botão ...
        path = os.getcwd() + '\base_de_dados'
        os.startfile(path)
        
        
def main():
    app = QApplication(sys.argv)
    form = Janela()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()