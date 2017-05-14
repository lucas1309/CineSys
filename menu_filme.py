import filme
import menu_ator
import ator

def imprimir_filme(filme):
    print('Cod. filme: ',filme.cod)
    print('Nome: ', filme.nome)
    print("Genero: ", filme.genero)
    print('Elenco: ', filme.elenco)
    print('Duração: ', filme.duracao , "  Minutos")
    print('Classificação: ', filme.classificacao , " Anos")
    print('Diostribuidora: ', filme.distribuidora)
    
    
def menu_criar():
    cod_filme = int(input('Digite o código do filme: '))
    nome = str(input('Digite o nome do filme :'))
    genero = str(input('Digite o genero do filme :'))
    menuElenco = 0
    listaElenco = []
    while menuElenco == 0:
        print ("\n----------------\n"+
             "(1) Criar Ator \n" +
             "(2) Listar Atores \n" +
             "(3) Adicionar Ator ao Elenco \n" +
             "(4) Ver Elenco \n" +
             "(0) Terminar Elenco \n" +
             "----------------")
        opt = int(input("Escolha a opção: "))
        if opt == 1:
            menu_ator.adicionar_ator()
        if opt == 2:
            menu_ator.listar_ator()
        if opt == 3:
            cod_ator = int(input("Insira o codigo do ator: "))
            atorElenco = ator.obter_ator(cod_ator)
            if atorElenco == None:
                print ("Ator não encontrado")
            else:
                print ("Deseja adicionar: ", atorElenco[1]," ao  elenco? (S/N)")
                rodando = 0
                while rodando == 0:
                    resp = str(input(": "))
                    if resp == "S" or resp == "s":
                        nomeAtor = atorElenco[1]
                        listaElenco.append(nomeAtor)
                        print ("Ator ADICIONADO")
                        rodando = 1
                    elif resp == "N" or resp == "n":
                        print ("Ator NAO adicionado")
                        rodando = 1
                    else:
                        print ("Insira uma resposta valida")
        if opt == 4:
            print(listaElenco)
        if opt == 0:
            menuElenco = 1
    dura = int(input('Digite a duracao do filme :'))
    clasi = str(input('Digite a classificacao do filme :'))
    distr = str(input('Digite a distribuidora do filme :'))
    filme.criar_filme(cod_filme,nome,genero,listaElenco,dura,clasi,distr)

def menu_obter():
    cod_filme= int(input('Obter filme por código: '))
    o = filme.obter_filme(cod_filme)
    if o==None:
        print('filme não encontrado! ')
    else:
        imprimir_filme(o)

def menu_listar():
    print(' Listar filmes \n')
    filmes = filme.listar_filmes()
    for f in filmes:
        imprimir_filme(f)

def menu_excluir():
    print('\n Excluir filme')
    cod_filme = int(input('Cod. filme: '))
    f = filme.excluir_filme(cod_filme)
    if (f == False):
        print ("filme não encontrado")
    else:
        print ("filme excluido")
    
def menu_alterar():
    print('\n Alterar filme')
    cod_filme = int(input('Cod. filme: '))
    f = filme.obter_filme()
    if (f == None):
        print ("Filme não encontrado")
    else:
        nome = str(input('Digite o nome do filme :'))
        genero = str(input('Digite o genero do filme :'))
        menuElenco = 0
        listaElenco = []
        while menuElenco == 0:
            print ("\n----------------\n"+
                 "(1) Criar Ator \n" +
                 "(2) Listar Atores \n" +
                 "(3) Adicionar Ator ao Elenco \n" +
                 "(4) Ver Elenco \n" +
                 "(0) Terminar Elenco \n" +
                 "----------------")
            opt = int(input("Escolha a opção: "))
            if opt == 1:
                menu_ator.adicionar_ator()
            if opt == 2:
                menu_ator.listar_ator()
            if opt == 3:
                cod_ator = int(input("Insira o codigo do ator: "))
                atorElenco = ator.obter_ator(cod_ator)
                if atorElenco == None:
                    print ("Ator não encontrado")
                else:
                    print ("Deseja adicionar: ", atorElenco[1]," ao  elenco? (S/N)")
                    rodando = 0
                    while rodando == 0:
                        resp = str(input(": "))
                        if resp == "S" or resp == "s":
                            nomeAtor = atorElenco[1]
                            listaElenco.append(nomeAtor)
                            print ("Ator ADICIONADO")
                            rodando = 1
                        elif resp == "N" or resp == "n":
                            print ("Ator NAO adicionado")
                            rodando = 1
                        else:
                            print ("Insira uma resposta valida")
            if opt == 4:
                print(listaElenco)
            if opt == 0:
                menuElenco = 1
        dura = int(input('Digite a duracao do filme :'))
        clasi = str(input('Digite a classificacao do filme :'))
        distr = str(input('Digite a distribuidora do filme :'))
        filme.alterar_filme(cod_filme,nome,genero,listaElenco,dura,clasi,distr)

def menu_excluirTodas():
    filme.excluir_todos_filmes()
    
        
def menu_mostrar():
    run_sala = True
    menu = ("\n----------------\n"+
             "(1) Criar Filme \n" +
             "(2) Listar Filmes \n" +
             "(3) Obter Filme por Cód. \n" +
             "(4) Excluir Filme \n" +
             "(5) Alterar Filme \n"+
             "(6) Remover TODOS os Filmes \n"+
             "(0) Voltar\n"+
            "----------------")
    
    while(run_sala):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if op == 1:
            menu_criar()
        elif op == 2:
            menu_listar()
        elif op == 3:       
            menu_obter()
        elif op == 4:
            menu_excluir()
        elif op == 5:
            menu_alterar()
        elif op == 6:
            menu_excluirTodas()
        elif op == 0:
            run_sala = False

if __name__ == "__main__":
    menu_mostrar()
    

        
    
