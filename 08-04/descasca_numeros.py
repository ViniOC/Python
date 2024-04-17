# dado um numero inteiro, imprima todos os digitos desse numero de maneira individualizada. Por exemplo, num = 27348329 deve imprimir
# 2
# 7
# 3
# ...
# 2
# 9
# #

num = int (input("Digite um número: "))

while num != 0:
    dig = num % 10
    num = num // 10
    print(dig)
