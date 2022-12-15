
import pandas as pd
import os
path = os.getcwd() + '\\base_de_dados' + '\\basePatrimonio.xlsx'
tabela = pd.read_excel(path)

    # for linha range(self.tableWidget.columnRoum()):
    
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
filtro = 169
tabela= tabela.query(f"patrimonio == {filtro}")

print(tabela.empty)

if tabela.empty:
    print('E vazio')
    print(tabela)
else:
    print('Preenchido')
    print(tabela)