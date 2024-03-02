import os
import time

def limpaTela():
    os.system("cls" if os.name == "nt" else "clear")

def mostraTitulo():
    print("===============================")
    print("Bem-vindo à locadora de carros!")
    print("===============================")
    print("O que deseja fazer?")
    print("1 - Mostrar portfólio | 2 - Alugar um carro | 3 - Devolver um carro | 0 - Sair do sistema")
    opcao = int(input("Insira o número da opção desejada: "))
    return opcao

def tchau():
    print("Obrigado por utilizar os nossos serviços. Volte sempre!")
    time.sleep(3)
    limpaTela()

def opcaoInvalida():
    print("Opção inválida. Voltando para o menu principal...")
    time.sleep(3)
    limpaTela()

carros = ["[1] Chevrolet Tracker - R$ 120/dia",
          "[2] Chevrolet Onix - R$ 90/dia",
          "[3] Chevrolet Spin - R$ 150/dia",
          "[4] Hyundai HB20 - R$ 85/dia",
          "[5] Hyundai Tucson - R$ 120/dia",
          "[6] Fiat Uno - R$ 60/dia",
          "[7] Fiat Mobi - R$ 70/dia",
          "[8] Fiat Pulse - R$ 130/dia"
          ]

while True:
    limpaTela()
    opcao = mostraTitulo()
    limpaTela()
    if opcao == 1:
        print("===============================")
        print("Nosso portfólio de carros!")
        print("===============================")
        for carro in carros:
            print(carro)
        print("===============================")
        print("O que você deseja fazer? 0 - MENU PRINCIPAL | 1 - FINALIZAR O PROGRAMA")
        decisao = int(input("Insira o número da opção desejada: "))
        if decisao == 0:
            limpaTela()
            mostraTitulo()
        elif decisao == 1:
            tchau()
            break
        else:
            opcaoInvalida()
            continue
    elif opcao == 2:
        print("===============================")
        print("Nosso portfólio de carros!")
        print("===============================")
        for carro in carros:
            print(carro)
        print("===============================")
        escolha = int(input("Indique o código do carro: "))
        if escolha not in range(1, 9):
            opcaoInvalida()
            continue
        print("Carro escolhido: {}".format(carros[escolha - 1]))
        dias = int(input("Indique por quantos dias você quer alugar o carro: "))
        if escolha not in range(1, 9):
            opcaoInvalida()
            continue
        if escolha - 1 == 0:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * 120)))
        elif escolha - 1 == 1:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * 90)))
        elif escolha - 1 == 2:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * 150)))
        elif escolha - 1 == 3:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * 85)))
        elif escolha - 1 == 4:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * 120)))
        elif escolha - 1 == 5:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * 60)))
        elif escolha - 1 == 6:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * 70)))
        else:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * 130)))
        print("Confirma o aluguel? 1 - SIM | 2 - NÃO")
        confirma = int(input("Indique a opção: "))
        if confirma not in [1, 2]:
            opcaoInvalida()
            continue
        if confirma == 1:
            print("Aluguel confirmado!")
            carros = carros.pop(escolha - 1)
        else:
            print("Aluguel não confirmado!")
        print("===============================")
        print("O que você deseja fazer? 0 - MENU PRINCIPAL | 1 - FINALIZAR O PROGRAMA")
        decisao = int(input("Insira o número da opção desejada: "))
        if decisao == 0:
            limpaTela()
            mostraTitulo()
        elif decisao == 1:
            tchau()
            break
        else:
            opcaoInvalida()
            continue
    elif opcao == 3:
        print("Opção 3")
        break
    elif opcao == 0:
        tchau()
        break
    else:
        opcaoInvalida()
        continue