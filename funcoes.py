
campos = {'patrimonio': 123,'modelo':'','processador':'AMD Ryzen 5','memoria':'12GB',
                'status':'Ativo','usuario':'Giulia Nunes','setor':'TI','n_modelo':'AB100051','n_serie':'17-8522626', 
                'tipo_contrato':'Estagio'}


campos_vazio = {'patrimonio': 123,'modelo':'VivoBook','processador':'AMD Ryzen 5','memoria':'12GB',
                'status':'Ativo','usuario':'Giulia Nunes','setor':'TI','n_modelo':'','n_serie':'17-8522626', 
                'tipo_contrato':''}


def se_vazio(dicionario):
    verifc  = False #se for = false é != de vazio
    
    for item in dicionario:
        indice = dicionario[ item ]
        
        if ( indice == '' or indice == None ):
            verifc = True #se for = true é == de vazio
        
    return verifc