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
carros = [
    "Chevrolet Tracker",
    "Chevrolet Onix",
    "Chevrolet Spin",
    "Hyundai HB20",
    "Hyundai Tucson",
    "Fiat Uno",
    "Fiat Mobi",
    "Fiat Pulse"
]
valores = [120, 90, 150, 85, 120, 60, 70, 130]
disponibilidade = [True] * len(carros)  # Lista para rastrear a disponibilidade

limpaTela()

while True:
    opcao = mostraTitulo()
    if opcao == 1:
        limpaTela()
        print("===============================")
        print("Nosso portfólio de carros!")
        print("===============================")
        for i in range(len(carros)):
            if disponibilidade[i]:
                print("[{}] {} - R$ {}/dia".format(codigoCarros[i], carros[i], valores[i]))
        print("===============================")
        input("Pressione ENTER para voltar ao menu principal.")
        limpaTela()
    elif opcao == 2:
        limpaTela()
        print("===============================")
        print("Escolha um carro para alugar:")
        print("===============================")
        for i in range(len(carros)):
            if disponibilidade[i]:
                print("[{}] {} - R$ {}/dia".format(codigoCarros[i], carros[i], valores[i]))
        print("===============================")
        escolhaCarro = int(input("Indique o código do carro: ")) - 1
        if escolhaCarro not in range(len(carros)) or not disponibilidade[escolhaCarro]:
            opcaoInvalida()
            continue
        print("Carro escolhido: {}".format(carros[escolhaCarro]))
        dias = int(input("Por quantos dias deseja alugar o carro? "))
        print("Valor total do aluguel: R$ {:.2f}".format(dias * valores[escolhaCarro]))
        confirma = int(input("Confirma o aluguel? 1 - SIM | 2 - NÃO "))
        if confirma == 1:
            print("Aluguel confirmado!")
            disponibilidade[escolhaCarro] = False
        else:
            print("Aluguel não confirmado!")
        input("Pressione ENTER para voltar ao menu principal.")
        limpaTela()
    elif opcao == 3:
        limpaTela()
        print("===============================")
        print("Escolha um carro para devolver:")
        print("===============================")
        for i in range(len(carros)):
            if not disponibilidade[i]:
                print("[{}] {}".format(codigoCarros[i], carros[i]))
        codigoDevolucao = int(input("Insira o código do carro: ")) - 1
        if codigoDevolucao in range(len(carros)) and not disponibilidade[codigoDevolucao]:
            disponibilidade[codigoDevolucao] = True
            print("O carro {} foi devolvido com sucesso.".format(carros[codigoDevolucao]))
            input("Pressione ENTER para voltar ao menu principal.")
            limpaTela()
        else:
            opcaoInvalida()
            continue
    elif opcao == 0:
        tchau()
        break
    else:
        opcaoInvalida()
