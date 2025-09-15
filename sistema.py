menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    
    opcao = input(menu)

    if opcao == "1":
        num = float(input("Digite o valor que deseja Depositar: \n"))
        if num > 0 :
            saldo += num
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

            elif num1 <= saldo :
                saldo -= num1
                numero_saques += 1
                print("Saldo atualizado com sucesso !!!")

            else :
                print("Ação invalida")

        else:
            print("!!! LIMITE DE SAQUES DIARIOS ATINGIDOS !!!")

    elif opcao == "3":
        print ("Extrato")
        print (saldo)

    elif opcao == "0":
        print("Encerrando programa")
        break

    else:
        print("OPÇÃO INVALIDA")