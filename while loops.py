"""---------/--------WHILE-LOOP--------/----------#
#--- EXECUTA UMA AÇÂO ATÉ DETERMINADA CONDIÇÃO ---#
#- ideal para situações onde não se sabe ---------#
#- a quantidade exata a ser repetida -------------#
#-----------/-------------/------------/--------"""

#1) executa uma repetição e adição até cert condição ser atingida
print("CASO 1 / (x <= 5)")
x = 0
while (x <= 5):
    print (x)
    x += 1

#saida: 0  1  2  3  4  5

#--------/--------/--------/--------/--------/--------/--------#

#2) executa uma saida que é interrompida se certa condição é atingida
print ("\nCASO 2 / (y <= 5)")

y = 0
while (y <= 5):
    print (y)
    if (y == 3): break
    
    y += 1

#saida: 0  1  2  3

#--------/--------/--------/--------/--------/--------/--------#

#3) executa uma mensagem após a condição se tornar falsa
print("\nCASO 3 / (z < 4)")
z = 1
while z < 4:
  print(z)
  z += 1
else:
  print("z deixou de ser menor que 4")

#saida: 0  1  2  3  z deixou de ser menor que 4

