from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
import sys
import os
import base
import pandas as pd
from  IPython.display import display 

class Janela(QtWidgets.QMainWindow, base.Ui_MainWindow):
    def __init__(self, parent=None):

        super(Janela, self).__init__(parent)
        self.setupUi(self)
        self.btn_buscar.clicked.connect(self.buscar) 
        self.btn_3pontos.clicked.connect(self.abrirPasta)
        self.btn_mostrar.clicked.connect(self.mostrar)
        self.btn_limpar.clicked.connect(self.limpar)
        
        
    def buscar(self): # função botão exibir
        try:
            patrimonio_ver = self.txt_patrimonio.text()
             
            if patrimonio_ver == '' or patrimonio_ver == None:
                QMessageBox.about(self, "AVISO" , "Campo vazio! \n" "Por favor, preencha os campos")
                
            else:
                path = os.getcwd() + '\\base_de_dados' + '\\basePatrimonio.xlsx'
                tabela = pd.read_excel(path)
                
                filtro = int(self.txt_patrimonio.text())
                tabela = tabela.query(f"patrimonio == {filtro}")
               
                if tabela.empty == False:
                    
                    modelo = list(tabela['modelo'])[0]
                    processador = list(tabela['processador'])[0]
                    memoria = list(tabela['memoria'])[0]
                    status = list(tabela['status'])[0]
                    usuario = list(tabela['usuario'])[0]
                    setor = list(tabela['setor'])[0]
                    
                    self.txt_modelo.setText(modelo)
                    self.txt_processador.setText(processador)
                    self.txt_memoria.setText(memoria)
                    self.txt_status.setText(status)
                    self.txt_usuario.setText(usuario)
                    self.txt_setor.setText(setor)
                    
                else:
                    QMessageBox.about(self, "AVISO", "Patrimonio não encontrado")    
                   
        except Exception as error:
            print(error)       
    
    def abrirPasta(self): # função botão ...
        path = os.getcwd() + '\\base_de_dados' 
        os.startfile(path)

    def mostrar(self): # função botão mostar
        path = os.getcwd() + '\\base_de_dados' + '\\basePatrimonio.xlsx'
        tabela = pd.read_excel(path)
        
        print(tabela)
    
    def limpar(self): # função botão limpar
        # campos = [self.txt_patrimonio,self.txt_modelo,self.txt_processador,self.txt_memoria,self.txt_status,self.txt_usuario,self.txt_setor]
        # for item in campos:
        #     item.clear()
        
        self.txt_patrimonio.clear()
        self.txt_modelo.clear()
        self.txt_processador.clear()
        self.txt_memoria.clear()
        self.txt_status.clear()
        self.txt_usuario.clear()
        self.txt_setor.clear()
        
def main():
    app = QApplication(sys.argv)
    form = Janela()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()