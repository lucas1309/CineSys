atores = []


def adicionar_ator(cod_ator, nome, nacionalidade, idade):
    ator = [cod_ator, nome, nacionalidade, idade]
    atores.append(ator)
    
def listar_atores():
    return atores

def obter_ator(cod_ator):
    for a in atores:
        if (a[0] == cod_ator):
            return a
    return None

def excluir_ator(cod_ator):
    for a in atores:
        if (a[0] == cod_ator):
            atores.remove(a)
            return True
    return False

def remover_todos_atores():
    global atores
    atores =  [] 

def iniciar_atores():
    adicionar_ator(1, "Chris Hemsworth ", "Australiano", 33)
    adicionar_ator(2, "Jason Statham", "Ingles", 49)
    adicionar_ator(3, "Sylvester Stallone", "Americano", 70)
