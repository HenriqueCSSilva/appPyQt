from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
import sys
import os
import base
import pandas as pd

class Janela(QtWidgets.QMainWindow, base.Ui_MainWindow):
    def __init__(self, parent=None):

        super(Janela, self).__init__(parent)
        self.setupUi(self)
        
        self.btn_detalhes.clicked.connect(self.detalhes_usuario) 
        self.btn_3pontos.clicked.connect(self.abrirPasta)
        self.btn_mostrar.clicked.connect(self.mostrar)
        self.btn_limpar.clicked.connect(self.limpar)
        self.btn_buscar_nome.clicked.connect(self.buscar)
        self.btn_limpar_nome.clicked.connect(self.limparN)
        
        
    def detalhes_usuario(self): #botão exibir
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
    
    def abrirPasta(self): #botão ...
        path = os.getcwd() + '\\base_de_dados' 
        os.startfile(path)

    def mostrar(self): #botão mostrar (tabela) 
        path = os.getcwd() + '\\base_de_dados' + '\\basePatrimonio.xlsx'
        tabela = pd.read_excel(path)
        
        print(tabela)
    
    def limpar(self): #botão limpar (aba geral)
        campos = [self.txt_patrimonio,self.txt_modelo,self.txt_processador,self.txt_memoria,self.txt_status,self.txt_usuario,self.txt_setor]
        for item in campos:
            item.clear()

    def buscar(self): # botão buscar (aba pesquisa)
        path = os.getcwd() + '\\base_de_dados' + '\\basePatrimonio.xlsx'
        tabela = pd.read_excel(path)
        
        filtro = self.txt_nome_buscar.text()  
           
        if (filtro == '' or filtro == None):
            
            QMessageBox.about(self, "AVISO" , "Campo vazio! \n" "Por favor, preencha o campo de busca")  
            
        else:
            
            tabela =tabela[tabela["usuario"].str.contains(filtro, na=False)]
            linha = 0
            
            for linha_indice in (tabela.index):
                
                coluna = 0
                
                for item in tabela:
                    
                    print(linha_indice, linha , coluna, item)
                    self.x = tabela.iloc[linha,coluna] 
                    self.tableWidget.setItem( linha, coluna, QTableWidgetItem(str(self.x)))
                    coluna = coluna +1
                    
                linha = linha + 1
    
    def limparN(self): #botão limpar (aba pesquisa)
        self.txt_nome_buscar.clear()
        self.tableWidget.clear()
                              
def main():
    app = QApplication(sys.argv)
    form = Janela()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()