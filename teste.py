
import pandas as pd
import os
path = os.getcwd() + '\\base_de_dados' + '\\basePatrimonio.xlsx'
tabela = pd.read_excel(path)

# linha = 0
# coluna = 0
# tabela = []

# for linha in tabela:
#     while tablewidget.rowCount() <= tabela.rowCount():
#         for coluna in tabela:
#             while tableWidget.columnCount()<= tabela.columnCount():
            
#                 self.x = tabela.iloc[linha,coluna]
#                 self.tableWidget.setItem(linha,coluna, QTableWidgetItem(str(self.x)))
                
#         coluna+=1
        
# linha+=1



    # for linha range(self.tableWidget.rowCount()):
    
        # for coluna in range(self.tableWidget.columnCount()): 
            
            # if linha == 2:
            #     return
        
            # x = tabela.iloc[linha,coluna] 
            # self.tableWidget.setItem(linha, coluna, QTableWidgetItem(x))
    
    # print(tabela)
                
            # patrimonio = tabela["patrimonio"][0]
            # modelo = tabela["modelo"][0]
            # processador= tabela["processador"][0]
            
            # for item in range(self.tableWidget.columnCount()):
            #     print('oi')
            
            #     self.tableWidget.setItem(0, 0, QTableWidgetItem(str(patrimonio)))
            #     self.tableWidget.setItem(0, 1, QTableWidgetItem(modelo)) 
            #     self.tableWidget.setItem(0, 2, QTableWidgetItem(processador)) 

        # def limpar(self):
            # self.txt_patrimonio.clear()
            # self.txt_modelo.clear()
            # self.txt_processador.clear()
            # self.txt_memoria.clear()
            # self.txt_status.clear()
            # self.txt_usuario.clear()
            # self.txt_setor.clear()
