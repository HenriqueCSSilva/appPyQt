from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem,QComboBox
import sys
import os
import base
import pandas as pd
import pymysql
import funcoes as f

class Janela(QtWidgets.QMainWindow, base.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Janela, self).__init__(parent)
        self.setupUi(self)
        
        #BOTÕES
        self.btn_buscar_detalhes.clicked.connect(self.detalhes_usuario)
        self.btn_limpar_detalhes.clicked.connect(self.limpar)
        self.btn_apagar.clicked.connect(self.apagar)
        
        self.btn_alterar.clicked.connect(self.alterar)
        self.btn_cadastrar.clicked.connect(self.cadastrar)
        
        self.btn_buscar_nome.clicked.connect(self.buscarN)
        self.btn_limpar_nome.clicked.connect(self.limparN)
        
        
    def detalhes_usuario(self): #botão buscar
        conn = pymysql.connect(host='satelpjceara.com',port=3306, user='satelp03_marcosh'  ,password='12345678', db='satelp03_bd_github')
        cur = conn.cursor()
    
        try:
            patrimonio_ver = self.txt_patrimonio.text()
            
            if patrimonio_ver == '' or patrimonio_ver == None:
                QMessageBox.about(self, "AVISO" , "Campo vazio! \n" "Por favor, preencha o campo de busca")
                
            else:
                filtro = int(self.txt_patrimonio.text())
                
                query = f"select * from tb_base_patrimonio where patrimonio = {filtro}"
                tabela = pd.read_sql(query, conn)
            
                if tabela.empty == False:
                    
                    modelo = list(tabela['modelo'])[0]
                    processador = list(tabela['processador'])[0]
                    memoria = list(tabela['memoria'])[0]
                    status = list(tabela['status'])[0]
                    usuario = list(tabela['usuario'])[0]
                    setor = list(tabela['setor'])[0]
                    n_modelo = list(tabela['n_modelo'])[0]
                    n_serie = list(tabela['n_serie'])[0]
                    tipo_contrato = list(tabela['tipo_contrato'])[0]
                    
                    self.txt_modelo.setText(modelo)
                    self.txt_processador.setText(processador)
                    self.txt_memoria.setText(memoria)
                    self.txt_status.setText(status)
                    self.txt_usuario.setText(usuario)
                    self.txt_setor.setText(setor)
                    self.txt_n_modelo.setText(n_modelo)
                    self.txt_n_serie.setText(n_serie)
                    self.txt_tipo_contrato.setText(tipo_contrato)
                    
                else:
                    QMessageBox.about(self, "FALHA", "Patrimonio não encontrado!")    
                
        except Exception as error:
            print(error)
            
    
    def cadastrar(self): #botão cadastrar        
        campos = {'patrimonio': self.txt_patrimonio.text(),'modelo':self.txt_modelo.text(),'processador':self.txt_processador.text(),'memoria':self.txt_memoria.text(),
                'status':self.txt_status.text(),'usuario':self.txt_usuario.text(),'setor':self.txt_setor.text(),'n_modelo':self.txt_n_modelo.text(),'n_serie':self.txt_n_serie.text(), 
                'tipo_contrato':self.txt_tipo_contrato.text()}

        conn = pymysql.connect(host='satelpjceara.com',port=3306, user='satelp03_marcosh' ,password='12345678', db='satelp03_bd_github')
        cur = conn.cursor()
        
        if f.se_vazio(campos) == False: 
            try:
                query_insert = f"""INSERT INTO tb_base_patrimonio (patrimonio, usuario, setor, modelo, processador, memoria, status, n_modelo, n_serie, tipo_contrato) 
                                    VALUES ({campos['patrimonio']}, '{campos['usuario']}', '{campos['setor']}', '{campos['modelo']}', '{campos['processador']}', 
                                    '{campos['memoria']}', '{campos['status']}', '{campos['n_modelo']}', '{campos['n_serie']}', '{campos['tipo_contrato']}')"""
                
                cur.execute(query_insert) #executa (raiozinho)
                conn.commit() #salvar
                conn.close()
                
                QMessageBox.about(self, "AVISO", "Usuário cadastrado com sucesso!")
                
            except Exception as erro:
                print(erro)
                
        else:
            QMessageBox.about(self, "FALHA", "Usuário não cadastrado!\n Nenhum campo pode estar vazio")

    def alterar(self): #botão alterar
        campos = {'patrimonio': self.txt_patrimonio.text(),'modelo':self.txt_modelo.text(),'processador':self.txt_processador.text(),'memoria':self.txt_memoria.text(),
                'status':self.txt_status.text(),'usuario':self.txt_usuario.text(),'setor':self.txt_setor.text(),'n_modelo':self.txt_n_modelo.text(),'n_serie':self.txt_n_serie.text(), 
                'tipo_contrato':self.txt_tipo_contrato.text()}
        
        conn = pymysql.connect(host='satelpjceara.com',port=3306, user='satelp03_marcosh' ,password='12345678', db='satelp03_bd_github')
        cur = conn.cursor()
        
        if f.se_vazio(campos) == False:
            try:
                query_update = f"""UPDATE tb_base_patrimonio SET usuario ='{campos['usuario']}', setor = '{campos['setor']}', modelo = '{campos['modelo']}', 
                                    processador = '{campos['processador']}', memoria = '{campos['memoria']}', status = '{campos['status']}', n_modelo = '{campos['n_modelo']}', 
                                    n_serie = '{campos['n_serie']}', tipo_contrato = '{campos['tipo_contrato']}'
                                    WHERE patrimonio = {campos['patrimonio']}"""

                print(query_update)
                
                cur.execute(query_update) #executa (raiozinho)
                conn.commit() #salvar
                conn.close()
                
                QMessageBox.about(self, "AVISO", "Dados alterados com sucesso!")
                
            except Exception as erro:
                print(erro) 
                
        else:
            QMessageBox.about(self, "FALHA", "Não foi possível fazer alterações!\n Nenhum campo pode estar vazio")
            
    def apagar(self):
        campos = {'patrimonio': self.txt_patrimonio.text(),'modelo':self.txt_modelo.text(),'processador':self.txt_processador.text(),'memoria':self.txt_memoria.text(),
        'status':self.txt_status.text(),'usuario':self.txt_usuario.text(),'setor':self.txt_setor.text(),'n_modelo':self.txt_n_modelo.text(),'n_serie':self.txt_n_serie.text(), 
        'tipo_contrato':self.txt_tipo_contrato.text()}
        
        conn = pymysql.connect(host='satelpjceara.com',port=3306, user='satelp03_marcosh' ,password='12345678', db='satelp03_bd_github')
        cur = conn.cursor()
      
        query_delete = f"""DELETE FROM satelp03_bd_github.tb_base_patrimonio WHERE patrimonio = {campos['patrimonio']};"""                    

        if f.se_vazio(campos) == False:
            try:
                print(query_delete)
                cur.execute(query_delete) #executa (raiozinho)
                conn.commit() #salvar
                conn.close()
                
                QMessageBox.about(self, "AVISO", "Dados apagados com sucesso!")
                
            except Exception as erro:
                print(erro)
                
        else:
            QMessageBox.about(self, "AVISO", "FALHA!\n Impossivel apagar os dados")

        
    def limpar(self): #botão limpar (ABA GERAL)
        campos = [self.txt_patrimonio,self.txt_modelo,self.txt_processador,self.txt_memoria,self.txt_status,self.txt_usuario,self.txt_setor,
        self.txt_n_modelo,self.txt_n_serie, self.txt_tipo_contrato]
        
        for item in campos:
            item.clear()


    #ABA PESQUISA
    def buscarN(self): # botão buscar (ABA PESQUISA)
        filtro = self.txt_nome_buscar.text()  
        
        conn = pymysql.connect(host='satelpjceara.com',port=3306, user='satelp03_marcosh'  ,password='12345678', db='satelp03_bd_github')
        query = f'select patrimonio,modelo,processador,memoria,status, usuario, setor from tb_base_patrimonio where usuario like "%{filtro}%"'
        tabela = pd.read_sql(query, conn)
       
        print(tabela)
    
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
                
    
    def limparN(self): #botão limpar (ABA PESQUISA)
        self.txt_nome_buscar.clear()
        self.tableWidget.clear()
        
        
def main():
    app = QApplication(sys.argv)
    form = Janela()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()