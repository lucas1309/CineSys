
import filme
import menu_filme

import ingresso
import menu_ingresso

import sessao
import sessao_menu

import ator
import menu_ator

import sala
import sala_menu


def iniciar_compra():
    #interface.iniciar_interfaces()
    #filme.iniciar_filmes()
    #ingresso.iniciar_ingressos()
    #sessao.iniciar_sessoes()
    #ator.iniciar_atores()
    #sala.iniciar_salas()
    print("em breve")

def mostrar_menu():
    run_menu = True

    iniciar_compra()


    menu = ("\n----------------\n"+
             "(1) Menu de Filmes \n" +
             "(2) Menu de Ingressos \n" +
             "(3) Menu da Sessões \n" +
             "(4) Menu de Atores \n" +
             "(5) Menu da Salas \n" +
             "(0) Sair\n"+
            "----------------")

    while (run_menu):
        print(menu)

        op = int(input("Selecione a opção: "))

        if(op == 1):
            menu_filme.menu_mostrar()
        elif(op == 2):
            menu_ingresso.menu_mostrar()            
        elif(op == 3):
            sessao_menu.menu_mostrar()
        elif(op == 4):
            menu_ator.mostrar_menu()
        elif(op == 5):
            sala_menu.menu_mostrar()
        elif (op == 0):
            print ("Saindo do programa...")
            run_menu = False
        else:
            print ("Valor invalido")

mostrar_menu()
