filmes = []

##Classe Filme
class classeFilme(object):
    def __init__(self,cod,nome,genero,elenco,duracao,classificacao,distribuidora):
        self.cod = cod
        self.nome = nome
        self.genero = genero
        self.elenco = elenco
        self.duracao = duracao
        self.classificacao = classificacao
        self.distribuidora = distribuidora
        
def criar_filme(cod_filme,nome,genero,elenco,duracao,classificacao,distribuidora):
    filme = classeFilme(cod_filme,nome,genero,elenco,duracao,classificacao,distribuidora)
    filmes.append(filme)
    
def obter_filme(cod_filme):
    for f in range (0,len(filmes)):
        if cod_filme == filmes[f].cod:
            return filmes[f]
    return None

def excluir_filme(cod_filme):
    for f in range (0,len(filmes)):
        if cod_filme == filmes[f].cod:
            aux = filmes[f]
            filmes.remove(aux)
            return True
    return False

def listar_filmes():
    return filmes

def alterar_filme(cod_filme,nome,genero,elenco,duracao,classificacao,distribuidora):
    for f in filmes:
        if f.cod == cod_filme:
            f.nome = nome
            f.genero = genero
            f.elenco = elenco
            f.duracao = duracao
            f.classificacao = classificacao
            f.distribuidora = distribuidora
            return True
        return False

def excluir_todos_filmes():
    global filmes
    filmes = []

