from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem,QComboBox
import sys
import os
import base
import pandas as pd
import pymysql
import funcoes as f
from openpyxl import Workbook, load_workbook

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
        
        self.btn_buscar_detalhes_2.clicked.connect(self.detalhes_equipamentos)
        self.btn_limpar_detalhes_2.clicked.connect(self.limpar2)
        self.btn_cadastrar_2.clicked.connect(self.cadastrar_equipamentos)
        self.btn_alterar_2.clicked.connect(self.alterar_equipamentos)
        self.btn_apagar_2.clicked.connect(self.apagar_equipamentos)
    
        
    #PAGE GERAL    
    def detalhes_usuario(self): 
        conn = pymysql.connect(host='satelpjceara.com',port=3306, user='satelp03_marcosh'  ,password='12345678', db='satelp03_bd_github')
        cur = conn.cursor()
    
        try:
            patrimonio_ver = self.txt_patrimonio.text()
            
            if patrimonio_ver == '' or patrimonio_ver == None:
                
                msg = QMessageBox()
                msg.setWindowTitle('AVISO')
                msg.setText('Campo vazio!')
                msg.setInformativeText('Por favor, preencha o campo de busca')
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                
            else:
                filtro = int( self.txt_patrimonio.text() )
                
                query = f"select * from tb_base_patrimonio where patrimonio = { filtro }"
                tabela = pd.read_sql(query, conn)
            
                if tabela.empty == False:
            
                    tipo_item = list( tabela[ 'tipo_item' ] )[0]
                    posto_trabalho = list( tabela[ 'posto_trabalho' ] )[0]
                    descricao = list( tabela[ 'descricao' ] )[0]
                    
                    uf = list( tabela[ 'uf' ] )[0]
                    if list( tabela[ 'uf' ] )[0] == 'RJ':
                        indexUf = 0
                    if list( tabela[ 'uf' ] )[0] == 'RJ - NITEROI':
                        indexUf = 1
                    if list( tabela[ 'uf' ] )[0] == 'SP':
                        indexUf = 2    
                    if list( tabela[ 'uf' ] )[0] == 'GO':
                        indexUf = 3
                    if list( tabela[ 'uf' ] )[0] == 'AC':
                        indexUf = 4
                    if list( tabela[ 'uf' ] )[0] == 'RO':
                        indexUf = 5
                    if list( tabela[ 'uf' ] )[0] == 'MG':
                        indexUf = 6
                    if list( tabela[ 'uf' ] )[0] == 'CE':
                        indexUf = 7
                    if list( tabela[ 'uf' ] )[0] == 'PE':
                        indexUf = 8
                           
                    id_usuario = list( tabela[ 'id_usuario' ] )[0]
                
                    setor = list( tabela['setor'] )[0]
                    if list( tabela[ 'setor' ] )[0] == 'Analise de Projetos':
                        indexSetor =  0 
                    if list( tabela[ 'setor' ] )[0] == 'Projetos AT':
                        indexSetor =  1 
                    if list( tabela[ 'setor' ] )[0] == 'Projetos MT - BT':
                        indexSetor =  2 
                    if list( tabela[ 'setor' ] )[0] == 'Fiscalização':
                        indexSetor =  3 
                    if list( tabela[ 'setor' ] )[0] == 'Financeiro':
                        indexSetor =  4 
                    if list( tabela[ 'setor' ] )[0] == 'Recursos Humanos':
                        indexSetor =  5 
                    if list( tabela[ 'setor' ] )[0] == 'COM':
                        indexSetor =  6 
                    if list( tabela[ 'setor' ] )[0] == 'Segurança do Trabalho':
                        indexSetor =  7 
                    if list( tabela[ 'setor' ] )[0] == 'Administrativo':
                        indexSetor =  8 
                    if list( tabela[ 'setor' ] )[0] == 'T.I':
                        indexSetor =  9 
                    
                    modelo = list( tabela [ 'modelo' ] )[0]
                    marca = list( tabela [ 'marca' ] )[0]
                    n_modelo = list( tabela [ 'n_modelo' ] )[0]
                    processador = list( tabela [ 'processador' ] )[0]
                    n_serie = list( tabela [ 'n_serie' ] )[0]
                    email = list( tabela [ 'email' ] )[0]
                    memoria = list( tabela [ 'memoria' ] )[0]
                    
                    status = list( tabela [ 'status' ] )[0]
                    if list( tabela [ 'status' ] )[0] == 'Ativo':
                        indexStatus = 0
                    if list( tabela [ 'status' ] )[0] == 'Inativo':
                        indexStatus = 1
                        
                    condicoes = list( tabela [ 'condicoes' ] )[0]
                    
                    alugado = list( tabela [ 'alugado' ] )[0]
                    if list( tabela [ 'alugado' ] )[0] == 'Sim':
                        indexAlugado = 0
                    if list( tabela [ 'alugado' ] )[0] == 'Não':
                        indexAlugado = 1
                        
                    ssd_hdd = list( tabela[ 'ssd_hdd' ] )[0]
                    if list( tabela[ 'ssd_hdd' ] )[0] == 'SSD':
                        indexSSD = 0
                    if list( tabela[ 'ssd_hdd' ] )[0] == 'HDD':
                        indexSSD = 1
                    if list( tabela[ 'ssd_hdd' ] )[0] == 'Ambos':
                        indexSSD = 2
                    
                    windows = list( tabela[ 'windows' ] )[0]
                    anydesk = list( tabela[ 'anydesk' ] )[0]
                    
                    officie = list( tabela[ 'officie' ] )[0]
                    if list( tabela[ 'officie' ] )[0] == 'Sim':
                        indexOfficie = 0
                    if list( tabela[ 'officie' ] )[0] == 'Não':
                        indexOfficie = 1
                        
                    tipo_officie = list( tabela[ 'tipo_officie' ] )[0]
                    if list( tabela[ 'tipo_officie' ] )[0] == '365':
                        indexTipoOfficie = 0
                    if list( tabela[ 'tipo_officie' ] )[0] == 'Home & Business':
                        indexTipoOfficie = 1
                    if list( tabela[ 'tipo_officie' ] )[0] == 'Standard':
                        indexTipoOfficie = 2
                    
                    conta = list( tabela[ 'conta' ] )[0]        
                    chave = list( tabela[ 'chave' ] )[0]
                    licenca = list( tabela[ 'licenca' ] )[0] 
                    
                    self.txt_tipo_item.setText( tipo_item )
                    self.txt_posto_trabalho.setText( posto_trabalho )
                    self.txt_descricao.setText( descricao )
                    self.ddl_uf.setCurrentIndex( indexUf )
                    self.txt_id_usuario.setText( id_usuario )
                    self.ddl_setor.setCurrentIndex( indexSetor )
                    self.txt_modelo.setText( modelo )
                    self.txt_marca.setText( marca )
                    self.txt_n_modelo.setText( n_modelo )
                    self.txt_processador.setText( processador )
                    self.txt_n_serie.setText( n_serie )
                    self.txt_email.setText( email )
                    self.txt_memoria.setText( memoria )
                    self.ddl_status.setCurrentIndex( indexStatus )                  
                    self.txt_condicoes.setText( condicoes )
                    self.ddl_alugado.setCurrentIndex( indexAlugado )
                    self.ddl_ssd_hdd.setCurrentIndex( indexSSD )
                    self.txt_windows.setText( windows )
                    self.txt_anydesk.setText( anydesk )
                    self.ddl_officie.setCurrentIndex( indexOfficie )
                    self.ddl_tipo_officie.setCurrentIndex( indexTipoOfficie )
                    self.txt_conta.setText( conta )
                    self.txt_chave.setText( chave )
                    self.txt_licenca.setText( licenca )
                    
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("AVISO")
                    msg.setText("Patrimonio não encontrado!")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                
        except Exception as error:
            print(error)
    
    #PAGE GERAL    
    def cadastrar(self):        
        campos = { 'patrimonio': self.txt_patrimonio.text(), 'tipo_item':self.txt_tipo_item.text(), 'posto_trabalho':self.txt_posto_trabalho.text(), 'descricao':self.txt_descricao.text(), 
                 'uf':self.ddl_uf.currentText(),'id_usuario':self.txt_id_usuario.text(), 'setor':self.ddl_setor.currentText(), 'modelo':self.txt_modelo.text(), 'marca':self.txt_marca.text(), 
                 'n_modelo':self.txt_n_modelo.text(), 'processador':self.txt_processador.text(), 'n_serie':self.txt_n_serie.text(), 'email':self.txt_email.text(), 
                 'memoria':self.txt_memoria.text(), 'status':self.ddl_status.currentText(), 'condicoes':self.txt_condicoes.text(), 'alugado':self.ddl_alugado.currentText(), 
                 'ssd_hdd':self.ddl_ssd_hdd.currentText(), 'windows':self.txt_windows.text(), 'anydesk':self.txt_anydesk.text(), 'officie':self.ddl_officie.currentText(),
                 'tipo_officie':self.ddl_tipo_officie.currentText(), 'conta':self.txt_conta.text(), 'chave':self.txt_chave.text(), 'licenca':self.txt_licenca.text() }

        conn = pymysql.connect(host='satelpjceara.com',port=3306, user='satelp03_marcosh' ,password='12345678', db='satelp03_bd_github')
        cur = conn.cursor()
        
        if f.se_vazio( campos ) == False: 
            try:
                query_insert = f"""INSERT INTO satelp03_bd_github.tb_base_patrimonio( patrimonio, tipo_item, posto_trabalho, descricao, uf, id_usuario, setor, modelo, marca, n_modelo, 
                                processador, n_serie, email, memoria, status, condicoes, alugado, ssd_hdd, windows, anydesk, officie, tipo_officie, conta, chave, licenca ) 
                                VALUES ( { campos['patrimonio'] }, '{ campos['tipo_item'] }', '{ campos['posto_trabalho']}', '{ campos['descricao'] }', '{ campos['uf'] }', '{ campos['id_usuario'] }', 
                                '{ campos[ 'setor' ] }', '{ campos['modelo'] }', '{ campos['marca'] }', '{ campos['n_modelo'] }', '{ campos['processador'] }', '{ campos['n_serie'] }', 
                                '{ campos['email'] }', '{ campos['memoria'] }', '{ campos['status'] }', '{ campos['condicoes'] }', '{ campos['alugado'] }', '{ campos['ssd_hdd'] }', 
                                '{ campos['windows'] }', '{ campos['anydesk'] }','{ campos['officie'] }', '{ campos['tipo_officie'] }', '{ campos['conta'] }', '{ campos['chave'] }', 
                                '{ campos['licenca'] }' ) """
                
                cur.execute(query_insert) #executa (raiozinho)
                conn.commit() #salvar
                conn.close()
                
                msg = QMessageBox()   
                msg.setWindowTitle("AVISO")
                msg.setText("Usuário cadastrado com sucesso!")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                
            except Exception as erro:
                print(erro)
                
        else:
            msg = QMessageBox()
            msg.setWindowTitle("FALHA")
            msg.setText("Usuário não cadastrado!")
            msg.setInformativeText("Nnehum campo pode estar vazio")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

    #PAGE GERAL
    def alterar(self):
        campos = { 'patrimonio':self.txt_patrimonio.text(), 'tipo_item':self.txt_tipo_item.text(), 'posto_trabalho':self.txt_posto_trabalho.text(), 'descricao':self.txt_descricao.text(), 
                  'uf':self.ddl_uf.currentText(), 'id_usuario':self.txt_id_usuario.text(), 'setor':self.ddl_setor.currentText(), 'modelo':self.txt_modelo.text(), 'marca':self.txt_marca.text(), 
                  'n_modelo':self.txt_n_modelo.text(), 'processador':self.txt_processador.text(), 'n_serie':self.txt_n_serie.text(), 'email':self.txt_email.text(), 
                  'memoria':self.txt_memoria.text(), 'status':self.ddl_status.currentText(), 'condicoes':self.txt_condicoes.text(), 'alugado':self.ddl_alugado.currentText(), 
                  'ssd_hdd':self.ddl_ssd_hdd.currentText(), 'windows':self.txt_windows.text(), 'anydesk':self.txt_anydesk.text(), 'officie':self.ddl_officie.currentText(),
                  'tipo_officie':self.ddl_tipo_officie.currentText(), 'conta':self.txt_conta.text(), 'chave':self.txt_chave.text(), 'licenca':self.txt_licenca.text() }
        
        conn = pymysql.connect(host='satelpjceara.com',port=3306, user='satelp03_marcosh' ,password='12345678', db='satelp03_bd_github')
        cur = conn.cursor()
        
        msg = QMessageBox()
        msg.setWindowTitle("AVISO")
        msg.setText("DESEJA SALVAR AS ALTERAÇÕES?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)

        executar = msg.exec_()
        
        if f.se_vazio( campos ) == False:
            try:
                if executar == msg.Yes:
                    query_update = f"""UPDATE satelp03_bd_github.tb_base_patrimonio SET tipo_item = '{ campos['tipo_item'] }', posto_trabalho = '{ campos['posto_trabalho'] }', 
                                    descricao = '{ campos['descricao'] }', uf = '{ campos['uf'] }', id_usuario = '{ campos['id_usuario'] }', setor = '{campos['setor']}', 
                                    modelo = '{ campos['modelo'] }', marca = '{ campos['marca'] }', n_modelo = '{ campos['n_modelo'] }', processador = '{ campos['processador'] }', 
                                    n_serie = '{ campos['n_serie'] }', email = '{ campos['email'] }', memoria = '{ campos['memoria'] }', status = '{ campos['status'] }', 
                                    condicoes = '{ campos['condicoes'] }', alugado = '{ campos['alugado'] }', ssd_hdd = '{ campos['ssd_hdd'] }', windows = '{ campos['windows'] }',
                                    anydesk = '{ campos['anydesk'] }', officie = '{ campos['officie'] }', tipo_officie = '{ campos['tipo_officie'] }', conta = '{ campos['conta'] }',
                                    chave = '{ campos['chave'] }', licenca = '{ campos['licenca'] }' WHERE patrimonio = { campos['patrimonio'] } """
                
                    cur.execute(query_update) #executa (raiozinho)
                    conn.commit() #salvar
                    conn.close()
                    
                    msg = QMessageBox()
                    msg.setWindowTitle("AVISO")
                    msg.setText("Alterações feitas com sucesso!")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                
            except Exception as erro:
                print(erro) 
                
        else:
            msg = QMessageBox()
            msg.setWindowTitle("FALHA")
            msg.setText("Não foi possivel fazer as alterações!")
            msg.setInformativeText("Nenhum campo pode estar vazio")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
         
    def apagar(self):
        campos = { 'patrimonio':self.txt_patrimonio.text(),'tipo_item':self.txt_tipo_item.text(), 'posto_trabalho':self.txt_posto_trabalho.text(), 'descricao':self.txt_descricao.text(),
                  'uf':self.ddl_uf.currentText(), 'id_usuario':self.txt_id_usuario.text(), 'setor':self.ddl_setor.currentText(), 'modelo':self.txt_modelo.text(), 'marca':self.txt_marca.text(), 
                  'n_modelo':self.txt_n_modelo.text(), 'processador':self.txt_processador.text(), 'n_serie':self.txt_n_serie.text(), 'email':self.txt_email.text(), 'memoria':self.txt_memoria.text(), 
                  'status':self.ddl_status.currentText(), 'condicoes':self.txt_condicoes.text(), 'alugado':self.ddl_alugado.currentText(), 'ssd_hdd':self.ddl_ssd_hdd.currentText(),
                  'windows':self.txt_windows.text(), 'anydesk':self.txt_anydesk.text(), 'officie':self.ddl_officie.currentText(),'tipo_officie':self.ddl_tipo_officie.currentText(), 
                  'conta':self.txt_conta.text(), 'chave':self.txt_chave.text(), 'licenca':self.txt_licenca.text() }
        
        conn = pymysql.connect(host='satelpjceara.com',port=3306, user='satelp03_marcosh' ,password='12345678', db='satelp03_bd_github')
        cur = conn.cursor()
      
        query_delete = f"""DELETE FROM satelp03_bd_github.tb_base_patrimonio WHERE patrimonio = { campos['patrimonio'] } """
                          
        msg = QMessageBox()
        msg.setWindowTitle("AVISO")
        msg.setText("ESTÁ AÇÃO É DEFINITIVA")
        msg.setInformativeText("Deseja continuar?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        executar = msg.exec_()
                
        if f.se_vazio( campos ) == False:
            try:   
                if executar == msg.Yes:
                    cur.execute(query_delete) #executa (raiozinho)
                    conn.commit() #salvar
                    conn.close()
                    
                    msg = QMessageBox()
                    msg.setWindowTitle("AVISO")
                    msg.setText("Dados apagados com sucesso")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                
            except Exception as erro:
                print(erro)
                
        else:
            msg = QMessageBox()
            msg.setWindowTitle("FALHA")
            msg.setText("Impossivel apagar os dados")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
    
    def limpar(self): #botão limpar (ABA GERAL)
        campos = [ self.txt_patrimonio, self.txt_tipo_item, self.txt_posto_trabalho ,self.txt_descricao, self.txt_id_usuario ,self.txt_modelo, self.txt_marca, self.txt_n_modelo, 
                  self.txt_processador, self.txt_n_serie, self.txt_email, self.txt_memoria, self.txt_condicoes, self.txt_windows, self.txt_anydesk, self.txt_conta, self.txt_chave, 
                  self.txt_licenca, self.txt_windows, self.txt_anydesk, self.txt_conta, self.txt_chave, self.txt_licenca ]
        
        for item in campos:
            item.clear()

#####################################################################################################################################################################################################

    #PAGE PESQUISA
    def buscarN(self): # botão buscar (ABA PESQUISA)
        filtro = self.txt_nome_buscar.text()
          
        if ( filtro == '' or filtro == None ):
            msg = QMessageBox()
            msg.setWindowTitle("AVISO")
            msg.setText("Campo vazio!")
            msg.setInformativeText("Por favor, preencha o campo de busca")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()  
            
        else:
            conn = pymysql.connect(host='satelpjceara.com',port=3306, user='satelp03_marcosh'  ,password='12345678', db='satelp03_bd_github')
            query = f"""select patrimonio, tipo_item, posto_trabalho, descricao, uf, id_usuario, modelo, marca, n_modelo, processador, n_serie, email, memoria, status, condicoes, alugado, 
                    sdd_hdd from tb_base_patrimonio where usuario like ' %{ filtro }% ' """
                    
            tabela = pd.read_sql(query, conn)
            print(tabela)
        
            tabela = tabela[ tabela[ "usuario" ].str.contains( filtro, na=False ) ]
            linha = 0
            
            for linha_indice in ( tabela.index ):
                coluna = 0
                
                for item in tabela:  
                    print( linha_indice, linha , coluna, item )
                    self.x = tabela.iloc[ linha,coluna ] 
                    self.tableWidget.setItem( linha, coluna, QTableWidgetItem( str( self.x ) ) )
                    coluna = coluna +1
                    
                linha = linha + 1
    
    #PAGE PESQUISA            
    def limparN(self):
        self.txt_nome_buscar.clear()
        self.tableWidget.clear() 
    
#############################################################################################################################################################################################

#PAGE EQUIPAMENTOS
    def detalhes_equipamentos(self):
        conn = pymysql.connect(host='satelpjceara.com',port=3306, user='satelp03_marcosh'  ,password='12345678', db='satelp03_bd_github')
        cur = conn.cursor()
    
        try:
            patrimonio_ver = self.txt_patrimonio_e.text()
            
            if patrimonio_ver == '' or patrimonio_ver == None:
                msg = QMessageBox()
                msg.setWindowTitle('AVISO')
                msg.setText('Campo vazio!')
                msg.setInformativeText('Por favor, preencha o campo de busca')
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                
            else:
                filtro = int( self.txt_patrimonio_e.text() )
                
                query = f"select * from tb_base_equipamentos where patrimonio = { filtro }"
                tabela = pd.read_sql(query, conn)
            
                if tabela.empty == False:
                    
                    if list( tabela[ 'uf' ] )[0] == 'RJ':
                        indexUf = 0
                    if list( tabela[ 'uf' ] )[0] == 'RJ - NITEROI':
                        indexUf = 1
                    if list( tabela[ 'uf' ] )[0] == 'SP':
                        indexUf = 2    
                    if list( tabela[ 'uf' ] )[0] == 'GO':
                        indexUf = 3
                    if list( tabela[ 'uf' ] )[0] == 'AC':
                        indexUf = 4
                    if list( tabela[ 'uf' ] )[0] == 'RO':
                        indexUf = 5
                    if list( tabela[ 'uf' ] )[0] == 'MG':
                        indexUf = 6
                    if list( tabela[ 'uf' ] )[0] == 'CE':
                        indexUf = 7
                    if list( tabela[ 'uf' ] )[0] == 'PE':
                        indexUf = 8
                        
                    descricao = list( tabela[ 'descricao' ] )[0]
                    posto_trabalho = list( tabela[ 'posto_trabalho' ] )[0]
                    modelo = list( tabela[ 'modelo' ] )[0]
                    marca = list( tabela[ 'marca' ] )[0]
                    n_modelo = list( tabela[ 'n_modelo' ] )[0]
                    n_serie = list( tabela[ 'n_serie' ] )[0]
                    
                    if list( tabela[ 'status' ] )[0] == 'Ativo':
                        indexStatus = 0
                    if list( tabela[ 'status' ] )[0] == 'Inativo':
                        indexStatus = 1
                    
                    self.ddl_uf_e.setCurrentIndex( indexUf )
                    self.txt_tipo.setText( descricao )
                    self.txt_posto_trabalho_e.setText( posto_trabalho )
                    self.txt_modelo_e.setText( modelo )
                    self.txt_marca_e.setText( marca )
                    self.txt_n_modelo_e.setText( n_modelo )
                    self.txt_n_serie_e.setText( n_serie )
                    self.ddl_status_e.setCurrentIndex( indexStatus )
                
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("AVISO")
                    msg.setText("Patrimonio não encontrado!")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                    
        except Exception as error:
            print(error)
            
    def cadastrar_equipamentos (self):
        campos = { 'patrimonio':self.txt_patrimonio_e.text(),'uf':self.ddl_uf_e.currentText(), 'descricao':self.txt_tipo.text(), 'posto_trabalho':self.txt_posto_trabalho_e.text(), 
                  'modelo':self.txt_modelo_e.text(), 'marca':self.txt_marca_e.text(), 'n_modelo':self.txt_n_modelo_e.text(), 'n_serie':self.txt_n_serie_e.text(), 
                  'status':self.ddl_status_e.currentText() }
        
        conn = pymysql.connect(host='satelpjceara.com',port=3306, user='satelp03_marcosh' ,password='12345678', db='satelp03_bd_github')
        cur = conn.cursor()
        
        if f.se_vazio( campos ) == False:
            try:
                query_insert = f""" INSERT INTO satelp03_bd_github.tb_base_equipamentos (patrimonio, uf, descricao, posto_trabalho, modelo, marca, n_modelo, n_serie, status) VALUES 
                              ( { campos[ 'patrimonio' ] }, '{ campos[ 'uf' ] }', '{ campos[ 'descricao' ] }', '{ campos[ 'posto_trabalho' ] }', '{ campos[ 'modelo' ] }', 
                              '{ campos[ 'marca' ] }', '{ campos[ 'n_modelo' ] }', '{ campos[ 'n_serie'] }', '{ campos[ 'status' ] }' )"""      
                
                cur.execute(query_insert)
                conn.commit()
                conn.close()
                
                msg = QMessageBox()
                msg.setWindowTitle("AVISO")
                msg.setText("Equipamento cadastrado com sucesso!")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                
            except Exception as erro:
                print(erro)
                
        else:
            msg = QMessageBox()
            msg.setWindowTitle("FALHA")
            msg.setText("Equipamento não cadastrado!")
            msg.setInformativeText("Nenhum campo pode estar vazio")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            
    def alterar_equipamentos (self):
        campos = { 'patrimonio':self.txt_patrimonio_e.text(), 'uf':self.ddl_uf_e.currentText(), 'descricao':self.txt_tipo.text(), 'posto_trabalho':self.txt_posto_trabalho_e.text(), 
                  'modelo':self.txt_modelo_e.text(), 'marca':self.txt_marca_e.text(), 'n_modelo':self.txt_n_modelo_e.text(), 'n_serie':self.txt_n_serie_e.text(),
                  'status':self.ddl_status_e.currentText() }
        
        conn = pymysql.connect(host='satelpjceara.com',port=3306, user='satelp03_marcosh' ,password='12345678', db='satelp03_bd_github')
        cur = conn.cursor()
        
        msg = QMessageBox()
        msg.setWindowTitle("WARNING")
        msg.setText("DESEJA SALVAR AS ALTERAÇÕES?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        executar = msg.exec_()
        
        if f.se_vazio( campos ) == False:
            try:
                if executar == msg.Yes:
                    query_update = f""" UPDATE satelp03_bd_github.tb_base_equipamentos SET uf = '{ campos[ 'uf' ] }', descricao = '{ campos[ 'descricao' ] }', 
                    posto_trabalho = '{ campos[ 'posto_trabalho' ] }', modelo = '{ campos[ 'modelo' ] }', marca = '{ campos[ 'marca' ] }', n_modelo = '{ campos[ 'n_modelo' ] }', 
                    n_serie = '{ campos[ 'n_serie'] }', status = '{ campos[ 'status' ] }' WHERE patrimonio = { campos['patrimonio'] }"""
                    
                    cur.execute( query_update )
                    conn.commit()
                    conn.close()
                    
                    msg = QMessageBox()
                    msg.setWindowTitle("AVISO")
                    msg.setText("Alterações feitas com sucesso!")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                
            except Exception as erro:
                print(erro)
        
        else:
            msg = QMessageBox()
            msg.setWindowTitle("FALHA")
            msg.setText("Não foi possivel fazer as alterações!")
            msg.setInformativeText("Nenhum campo pode estar vazio")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            
    def apagar_equipamentos (self):
        campos = { 'patrimonio':self.txt_patrimonio_e.text(),'uf':self.ddl_uf_e.currentText(), 'descricao':self.txt_tipo.text(), 'posto_trabalho':self.txt_posto_trabalho_e.text(), 
            'modelo':self.txt_modelo_e.text(), 'marca':self.txt_marca_e.text(), 'n_modelo':self.txt_n_modelo_e.text(), 'n_serie':self.txt_n_serie_e.text(), 
            'status':self.ddl_status_e.currentText() }
        
        conn = pymysql.connect(host='satelpjceara.com',port=3306, user='satelp03_marcosh' ,password='12345678', db='satelp03_bd_github')
        cur = conn.cursor()
        
        query_delete = f"""DELETE FROM satelp03_bd_github.tb_base_equipamentos WHERE patrimonio = { campos['patrimonio'] }"""
        
        msg = QMessageBox()
        msg.setWindowTitle("WARNING")
        msg.setText("ESTÁ AÇÃO É DEFINITIVA")
        msg.setInformativeText("Deseja continuar?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Cancel)
        executar = msg.exec_()
        
        if f.se_vazio( campos ) == False:
            try:
                if executar == msg.Yes:
                    cur.execute( query_delete )
                    conn.commit()
                    conn.close()

                    msg = QMessageBox()
                    msg.setWindowTitle("AVISO")
                    msg.setText("Dados apagados com sucesso!")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                
            except Exception as erro:
                print(erro)
        
        else:
            msg = QMessageBox()
            msg.setWindowTitle("FALHA")
            msg.setText("Impossivel apagar os dados!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
        
    def limpar2 (self):
        campos = [ self.txt_patrimonio_e, self.txt_tipo, self.txt_posto_trabalho_e, self.txt_modelo_e, self.txt_marca_e, self.txt_n_modelo_e, self.txt_n_serie_e ]
        
        for item in campos:
            item.clear()
               
def main():
    app = QApplication(sys.argv)
    form = Janela()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()