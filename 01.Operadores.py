"""### Exercicios Operadores ###
1- Crie um programa que imprima o valor do maior número entre duas variáveis.


"""

a = 82
b = 65
c = 33

print ("Crie um programa que imprima o valor do maior número entre duas variáveis.")
if a > b :
    print (f"entre {a} e {b}, {a} é maior que {b}")
else :
    print  (f"entre {a} e {b}, {b} é maior que {a}")

print("\nCrie um programa que imprima o maior e o menor valor entre três variáveis.")
if a > b:
    if a > c:
        print (f"{a} é o maior numero entre {a}, {b} e {c}")
    elif c > b:
        print (f"{c} é o maior numero entre {a}, {b} e {c}")
elif b > c:
    print (f"{b} é o maior numero entre {a}, {b} e {c}")

print("\nCrie um programa que imprima 'HAHAHA' caso o número da variável seja par.")
par = a%2
if par == 0:
    print ("HAHAHA")

print("\nCrie um programa para dizer se o número é par ou ímpar.")
def reteste(x):
    sobra = x%2
    if sobra == 0:
        print (f"{x} é PAR")
    else:
        print (f"{x} é IMPAR")
 
reteste(a)
reteste(b)
reteste(c)