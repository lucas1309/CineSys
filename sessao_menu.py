import sessao
import sala
import filme


def imprimir_sessao(sessoes):
    print(sessoes)
    print('Cod. Sessão: ',sessoes[0])
    print('Cod. Filme: ', sessoes[1])
    print('Cod sala: ',sessoes[2])
    print('Horário: ',sessoes[3])
    print('Capacidade: ',sessoes[4])
    
def menu_criar():
    cod_sessao = int(input('Digite o código da sessão: '))
    cod_filme = int(input('Digite o código do filme: '))
    cod_sala = int(input('Digite o código da sala: '))
    horario = int(input('Digite o horário: '))
    capacidade = int(input('Digite a capacidade da sessão :'))
    sessao.criar_sessao(cod_sessao,cod_filme,cod_sala,horario,capacidade)

def menu_buscar():
    cod_sessao= int(input('Buscar sessão pelo código da sessão: '))
    o = sessao.buscar_sessao(cod_sessao)
    if o==None:
        print('Sessão não encontrada! ')
    else:
        imprimir_sessao(o)

def menu_listar():
    print(' Listar sessões \n')
    sessoes = sessao.listar_sessao()
    for s in sessoes:
        imprimir_sessao(s)

def menu_excluir():
    print('\n Excluir sessão')
    cod_sessao = int(input('Cod. Sessao: '))
    s = sessao.excluir_sessao(cod_sessao)
    if (s == False):
        print ("Sessao não encontrada")
    else:
        print ("Sessão excluida")
    
def menu_alterar():
    print('\n Alterar sessão')
    cod_sessao = int(input('Cod. Sessão: '))
    s = sessao.listar_sessao()
    if (s == False):
        print ("Sessão não encontrada")
    else:
        cod_filme = int(input('Digite o novo código do filme: '))
        cod_sala = int(input('Digite o novo código da sala: '))
        horario = int(input('Digite o novo horário: '))
        capacidade = int(input('Digite a nova capacidade da sessão :'))
        s = sessao.buscar_sessao(cod_sessao)
        s[1] = cod_filme
        s[2] = cod_sala
        s[3] = horario
        s[4] = capacidade
        ss= s[1] and s[2] and s[3] and s[4]
        sessao.alterar_sessoes(cod_sessao, cod_filme, cod_sala, horario, capacidade)
        return ss

def menu_excluirTodas():
    sessao.remover_todas_as_sessoes()

def menu_verificar():
    cod_sessao = int(input('Digite o cód. sessão: '))
    print('Capacidade da sessão é de :',sessao.verificar_disponibilidade(cod_sessao), ' pessoas.')
        
def menu_mostrar():
    run_sessao = True
    menu = ("\n----------------\n"+
             "(1) Criar sessão \n" +
             "(2) Listar sessão \n" +
             "(3) Buscar sessão por Cód. sessão\n" +
             "(4) Excluir sessão \n" +
             "(5) Alterar sessão \n"+
             "(6) Remover TODAS as sessões \n"+
             "(7) Verificar disponibilidade da sessao \n" + 
             "(0) Voltar\n"+
            "----------------")
    
    while(run_sessao):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if op == 1:
            menu_criar()
        elif op == 2:
            menu_listar()
        elif op == 3:       
            menu_buscar()
        elif op == 4:
            menu_excluir()
        elif op == 5:
            menu_alterar()
        elif op == 6:
            menu_excluirTodas()
        elif op ==7:
            menu_verificar()
        elif op == 0:
            run_sessao = False

if __name__ == "__main__":
    menu_mostrar()
    

        
    

