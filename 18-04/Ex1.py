# 1. Dada uma sequência de números inteiros onde o último elemento é o 0, escreva um algoritmo
# que calcula a soma dos números pares da sequência.
n1 = input("informe um sequencia de numeros: ")
tam = len(n1)

for i in range (len(n1)):
 print(n1[i])

 if n1[i]%2 == 0:
    sum = int(n1[i])

 print (sum)   
  
 i = i+i

