 # Escreva um programa que recebe uma String e imprime uma outra String com
#  os caracteres invertidos. Obrigatoriamente, nesse exerc´ ıcio, use um comando de
#  repeti¸c˜ ao (while ou for)

palavra = input("Digite uma palavra/Frase: ")

palavraInvertida = ""
# O primeiro -1 faz com que comecemos a lista do ultimo espaco
# o segundo faz com que paremos de subtrair a lista antes de -1(ou seja 0)
# o terceiro é para identificarmos como andaremos nesta lista(-1 casa)

for c in range (len(palavra) -1, -1, -1):
    
    palavraInvertida += palavra[c]
        
print(palavraInvertida)
    
    