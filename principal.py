from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
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
                df= tabela
                print( tabela['modelo'][0])
                
                if tabela.empty == False:
                    print(tabela)
                    
                    modelo = str( tabela['modelo'][0])
                    print( modelo  )
                    
                    processador = tabela['processador'][0]
                    memoria = tabela['memoria'][0]
                    status = tabela['status'][0]
                    usuario = tabela['usuario'][0]
                    setor = tabela['setor'][0]
                    
                    print('Entrou aqui')
                    # self.txt_modelo.setText(modelo)
                    # self.txt_processador.setText(processador)
                    # self.txt_memoria.setText(memoria)
                    # self.txt_status.setText(status)
                    # self.txt_usuario.setText(usuario)
                    # self.txt_setor.setText(setor)
                   
                else:
                    print('Entrou no Else')
                    QMessageBox.about(self, "AVISO" , "Campo vazio! \n" "Patrimonio não encontrado")
                    
                    
                   
        except Exception as error:
            print(error)       
         
        # for item in campos:
        #     if(item == '' or item == None):
        #         QMessageBox.about(self, "AVISO" , "Campo vazio! \n" "Por favor, preencha os campos")
        #         return
        # else:
        #     print (patrimonio,"\n",modelo,"\n",processador,"\n",memoria,"\n",status,"\n",status,"\n",usuario,"\n",setor)
    
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