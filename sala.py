salas = []
def criar_sala(cod_sala,capacidade):
    sala = [cod_sala,capacidade]
    salas.append(sala)
def obter_sala(cod_sala):
    for s in salas:
        if s[0] ==cod_sala:
            return s
    return None
def excluir_sala(cod_sala):
    for s in salas:
        if s[0] == cod_sala:
            salas.remove(s)
            return True
    return False
def alterar_sala(cod_sala,capacidade):
    for s in salas:
        if cod_sala==s[0]:
            
            capacidade = s[1]
           
            return True
    return False
def remover_todas_as_salas():
    global salas
    salas=[]

def listar_salas():
    return salas
        
    
    
