"""--------/---------FOR-LOOP---------/----------#
#-- EXECUTA UM NUMERO EXPECIFICO DE REPETIÇÔES --#
#-ideal para situações onde se sabe a quantidade-#
#-de vezes a ser repetida com antecedencia ------#
#----------/------------/-------------/--------"""

#1)executa um loop começando em 0 e adicionando 1
print("CASO 1:")
for i in range(4) : 
    print(i) 

# saida = 0  1  2  3

#2)executa um loop começando em 3 e adicionando 1
print("\nCASO 2:")
for i in range(3,6):
    print(i)

# saida = 3  4  5

#3)executa um loop começando em 0 e adicionando 10
print("\nCASO 3:")
for i in range(0,31,10) :
    print(i)

# saida 0  10  20  30