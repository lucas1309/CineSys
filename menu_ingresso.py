import ingresso
import filme
import sessao

def imprimir_ingresso(ingresso):
    print('Cod. Sessão: ',ingresso[0])
    print('Cod. Filme: ', ingresso[1][1])
    print('Cod sala: ',ingresso[1][2])
    print('Horário: ',ingresso[1][3])
    print('Capacidade: ',ingresso[1][4], "Ingressos Restantes :", ingresso[2])
    
    
def menu_criar():
    cod_sessao = int(input('Digite o código da sessão: '))
    capacidade = int(input('Digite a capacidade da sessão :'))
    a = ingresso.adicionar_ingresso(cod_sessao,capacidade)
    if a == True:
        print ("Ingressos da sessao criados com sucesso")
    else:
        print("Erro, a sessao nao foi encontrada")

def menu_buscar():
    cod_sessao= int(input('Buscar ingressos pelo código da sessão: '))
    o = ingresso.obter_ingresso(cod_sessao)
    if o==None:
        print('Sessão não encontrada! ')
    else:
        imprimir_ingresso(o)

def menu_listar():
    print(' Listar sessões \n')
    ingressos = ingresso.listar_ingressos()
    for s in ingressos:
        imprimir_ingresso(s)

def menu_excluir():
    print('\n Vender ingresso')
    cod_sessao = int(input('Cod. Sessao: '))
    qtd = int(input("Quantos deseja comprar?  "))
    s = ingresso.vender_ingresso(cod_sessao,qtd)
    if (s == False):
        print ("Sessao não encontrada ou quantidade de ingressos maior que a disponibilidade")
    else:
        print ("Ingressos vendidos!")

def menu_verificar():
    cod_sessao = int(input("Insira o codigo da sessao: "))
    qtd = ingresso.verificar_ingresso(cod_sessao)
    if (qtd == None):
        print("Sessão não encontrada")
    else:
        print("A sessão ",cod_sessao," possui ", qtd , " Ingressos disponiveis")
    
        
def menu_mostrar():
    run_sessao = True
    menu = ("\n----------------\n"+
             "(1) Criar ingressos da sessao \n" +
             "(2) Listar ingressos da sessão \n" +
             "(3) Buscar ingressos por Cód. sessão\n" +
             "(4) Vender ingresso \n" +
             "(5) Verificar disponibilidade da sessao \n" + 
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
        elif op ==5:
            menu_verificar()
        elif op == 0:
            run_sessao = False

if __name__ == "__main__":
    menu_mostrar()
    

