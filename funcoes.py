def se_vazio(dicionario):
    verifc  = False #se for = false é != de vazio
    
    for item in dicionario:
        indice = dicionario[ item ]
        
        if ( indice == '' or indice == None ):
            verifc = True #se for = true é == de vazio
        
    return verifc

def caracter_9(valor):
    if len(valor) == 9:
        return True
    else:
        return False