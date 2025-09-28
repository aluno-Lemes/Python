import datetime

#Declaração de variaveis
Saldo = 0
Limite = 500
Extrato = []
numSaques = 0
limiteSaque = 3
transacoes = len(Extrato)



menu = """
O que deseja fazer ?

    [1]   DEPOSITAR
    [2]   SACAR
    [3]   EXTRATO
    [4]   SAIR  \n
    """


#Função responsavel pela entrada de valores
def entrada(x):
    try:
        valor = float(input(f"Digite o valor a ser {x}: \n"))
        return valor
    except:
        return 0

    
#função responsavel pela estrutura do sistema
def Main():

    while True:

        opção = input(menu)

        if opção == "1":
           depositar(entrada("Depositado"))

        elif opção == "2":
            if numSaques < limiteSaque:
                sacar(entrada("Sacado"))
            else:
                print("Limite de saques diarios atingido!")

        elif opção == "3":
            extrato()

        elif opção == "4":
            print ("Encerrando Programa")
            break

        else:
            print ("OPÇÂO INVALIDA")



# Bloco responsavel pelo controle de tempo
def getTime():
    data_hora = datetime.datetime.now()
    return data_hora.strftime("%d/%m/%Y - %H:%M")



#Função responsavel pelo Deposito
def depositar(num):
    global Saldo

    if num <= 0:
        print("\nNão foi possivel realizar esta ação! ")

    else:
        Extrato.append(f"Deposito - R$:{num:.2f} -- Data:{getTime()} ")
        Saldo += num
        print("\nValor atualizado com sucesso ! ")
    
    

#Função responsavel pelo Saque
def sacar(num):
    global Saldo
    global numSaques

    if num > Saldo:
        print("Saldo insuficiente")
    
    elif num > Limite:
        print(f"Limite por saque é de {Limite:.2f} ")

    elif num <= 0:
        print("\nNão foi possivel realizar esta ação! ")

    else:
        Extrato.append(f"Saque - R$:{num:.2f} -- Data:{getTime()} ")
        Saldo -= num
        numSaques += 1
        print("\nValor atualizado com sucesso ! ")
            


#Função responsavel pelo Extrato
def extrato():
    print ("-----#-----#-----EXTRATO-----#-----#-----")
    print (f"# Saldo de R$:{Saldo:.2f} #")
    print (f"# Total de movimentações na conta: {len(Extrato)}\n")
    print ("-----#-----#----HISTÓRICO----#-----#-----")
    for elemento in Extrato: print(elemento)
    print ("-----#-----#-----#-----#-----#-----#-----")

    
print (" #-#-#-#-#-#-#-# SISTEMA BANCARIO #-#-#-#-#-#-#-# ")

Main()



