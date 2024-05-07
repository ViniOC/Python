import math
# Funciona apenas com 2 numeros.

def mediaGeometrica (num1, num2):
  raiz = (num1*num2)
  result = math.sqrt(raiz)  
  return result

n1 = float(input("Infome um numero: "))
n2 = float(input("Infomre um segundo numero: "))

media = mediaGeometrica(n1, n2)

print (media)
