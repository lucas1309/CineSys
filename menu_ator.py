import ator

def imprimir_ator(ator):
    print ("Código do Ator: ",  ator[0])
    print ("Nome: ", ator[1])
    print ("Nacionalidade: ",  ator[2])
    print ("Idade: ",  ator[3])
    print ()

def adicionar_ator():
    print ("\nAdicionar Ator \n")
    cod = int(input("Código do ator: "))
    nome = str (input("Nome: "))
    nacionalidade = str(input("Nacionalidade: "))
    idade = int(input("Idade: "))
    ator.adicionar_ator(cod, nome, nacionalidade, idade)

def obter_ator():
    print ("\nBuscar Ator pelo código. \n")
    cod = int(input("Código do Ator: "))
    a = ator.obter_ator(cod)
    if (a == None):
        print ("Ator não encontrado")
    else:
        imprimir_ator(a)
  
def excluir_ator():
    print ("\nRemover Ator \n")
    cod = int(input("Código do Ator: "))
    a = ator.excluir_ator(cod)
    if (a == False):
        print ("Ator não encontrado")
    else:
        print ("Ator removido")
    

def mostrar_menu():
    run_ator = True
    menu = ("\n----------------\n"+
             "(1) Adicionar novo Ator \n" +
             "(2) Obter Ator \n" +
             "(3) Excluir Ator \n" +
             "(0) Voltar\n"+
            "----------------")
    
    while(run_ator):
        print (menu)
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            adicionar_ator()
        elif(op == 2):
            obter_ator()
        elif(op == 3):       
            excluir_ator()
        elif (op == 0):
            run_ator = False
    
if __name__ == "__main__":
    mostrar_menu()
