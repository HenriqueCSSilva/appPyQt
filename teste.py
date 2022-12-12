
import pandas as pd
import os
path = os.getcwd() + '\\base_de_dados' + '\\basePatrimonio.xlsx'
tabela = pd.read_excel(path)


filtro = 169
tabela= tabela.query(f"patrimonio == {filtro}")

print(tabela.empty)

if tabela.empty:
    print('E vazio')
    print(tabela)
else:
    print('Preenchido')
    print(tabela)