import sessao

ingressos = []

def adicionar_ingresso(cod_sessao, qtd):
    ses = sessao.buscar_sessao(cod_sessao)
    if (ses != None):
        ingresso = [cod_sessao,ses, qtd]
        ingressos.append(ingresso)
        return True
    return False
    
def listar_ingressos():
    return ingressos

def obter_ingresso(cod_sessao):
    for i in ingressos:
        if (i[0] == cod_sessao):
            return i
    return None

def vender_ingresso(cod_sessao,qtd):
    for i in ingressos:
        if (i[0] == cod_sessao):
            i[1] -= qtd
            return True
        
    return False

def verificar_ingresso(cod_sessao):
    for i in ingressos:
        if (i[0] == cod_sessao):
            aux = i[1]
            return aux
    return None

def iniciar_ingressos():
    adicionar_ingresso(1,20)
    adicionar_ingresso(2,30)
    adicionar_ingresso(3,40)
    adicionar_ingresso(4,10)
    
