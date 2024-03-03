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

codigoCarros = [1, 2, 3, 4, 5, 6, 7, 8]

carros = ["Chevrolet Tracker",
          "Chevrolet Onix",
          "Chevrolet Spin",
          "Hyundai HB20",
          "Hyundai Tucson",
          "Fiat Uno",
          "Fiat Mobi",
          "Fiat Pulse"
          ]

"""
carros = ["[1] Chevrolet Tracker - R$ 120/dia",
          "[2] Chevrolet Onix - R$ 90/dia",
          "[3] Chevrolet Spin - R$ 150/dia",
          "[4] Hyundai HB20 - R$ 85/dia",
          "[5] Hyundai Tucson - R$ 120/dia",
          "[6] Fiat Uno - R$ 60/dia",
          "[7] Fiat Mobi - R$ 70/dia",
          "[8] Fiat Pulse - R$ 130/dia"
          ]
"""

valores = [120, 90, 150, 85, 120, 60, 70, 130]

limpaTela()

while True:
    opcao = mostraTitulo()
    totalCarros = len(carros)
    if opcao == 1:
        if totalCarros == 0:
            print("Todos os carros estão alugados. Verifique novamente amanhã.")
            tchau()
            break
        limpaTela()
        print("===============================")
        print("Nosso portfólio de carros!")
        print("===============================")
        for i in range(0, totalCarros):
            print("[{}] {} - R$ {}/dia".format(codigoCarros[i], carros[i], valores[i]))
        print("===============================")
        print("O que você deseja fazer? 1 - MENU PRINCIPAL | 2 - FINALIZAR O PROGRAMA")
        decisao = int(input("Insira o número da opção desejada: "))
        if decisao == 1:
            limpaTela()
            mostraTitulo()
        elif decisao == 2:
            tchau()
            break
        else:
            opcaoInvalida()
            continue
    elif opcao == 2:
        if totalCarros == 0:
            print("Todos os carros estão alugados. Verifique novamente amanhã.")
            tchau()
            break
        limpaTela()
        print("===============================")
        print("Nosso portfólio de carros!")
        print("===============================")
        for i in range(0,totalCarros):
            print("[{}] {} - R$ {}/dia".format(codigoCarros[i], carros[i], valores[i]))
        print("===============================")
        escolhaCarro = int(input("Indique o código do carro: "))
        escolhaCarro -= 1
        if escolhaCarro not in range(0, totalCarros):
            opcaoInvalida()
            continue
        print("Carro escolhido: {}".format(carros[escolhaCarro]))
        dias = int(input("Indique por quantos dias você quer alugar o carro: "))
        if escolhaCarro == 0:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * valores[escolhaCarro])))
        elif escolhaCarro == 1:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * valores[escolhaCarro])))
        elif escolhaCarro == 2:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * valores[escolhaCarro])))
        elif escolhaCarro == 3:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * valores[escolhaCarro])))
        elif escolhaCarro == 4:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * valores[escolhaCarro])))
        elif escolhaCarro == 5:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * valores[escolhaCarro])))
        elif escolhaCarro == 6:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * valores[escolhaCarro])))
        else:
            print("Valor total do aluguel: R$ {:.2f}".format(float(dias * valores[escolhaCarro])))
        print("Confirma o aluguel? 1 - SIM | 2 - NÃO")
        confirma = int(input("Indique a opção: "))
        if confirma not in [1, 2]:
            opcaoInvalida()
            continue
        if confirma == 1:
            print("Aluguel confirmado!")
            codigoCarros.pop(escolhaCarro)
            carros.pop(escolhaCarro)
            valores.pop(escolhaCarro)
        else:
            print("Aluguel não confirmado!")
        print("===============================")
        print("O que você deseja fazer? 1 - MENU PRINCIPAL | 2 - FINALIZAR O PROGRAMA")
        decisao = int(input("Insira o número da opção desejada: "))
        if decisao == 1:
            limpaTela()
            mostraTitulo()
        elif decisao == 2:
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