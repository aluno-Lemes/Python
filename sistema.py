menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def callExtrato():
    for elemento in extrato:
        print(elemento)

while True:
    
    opcao = input(menu)

    if opcao == "1":
        num = float(input("Digite o valor que deseja Depositar: \n"))
        
        if num > 0 :
            saldo += num
            extrato.append(f"Deposito - R$:{num:.2f}")
            print("Saldo atualizado com sucesso !!!")

        else:
            print("Ação invalida")

    elif opcao == "2":
        if numero_saques < LIMITE_SAQUES:
            num1 = float(input("Digite o valor que deseja Sacar: \n"))

            if num1 > limite:
                print(f"Valor limite para Saques é de R$:{limite}")

            elif num1 > saldo:
                print("saldo insuficiente!")

            elif 0 < num1 <= saldo :
                saldo -= num1
                numero_saques += 1
                extrato.append(f"Saque - R$:{num1:.2f}")
                print("Saldo atualizado com sucesso !!!")

            else :
                print("Ação invalida")

        else:
            print("!!! LIMITE DE SAQUES DIARIOS ATINGIDOS !!!")

    elif opcao == "3":
        print ("-----/-----/-----EXTRATO-----\-----\-----")
        print (f"# Saldo de R$:{saldo:.2f} #")
        print (f"# Total de movimentações na conta: {len(extrato)}")
        print (f"# Numero de Saques realizados: {numero_saques}\n")
        print ("-----/-----/----HISTÓRICO----\-----\-----")
        print (callExtrato())
        print ("-----/-----/-----/-----\-----\-----\-----")
# 
#                


    elif opcao == "0":
        print("Encerrando programa")
        break

    else:
        print("OPÇÃO INVALIDA")
