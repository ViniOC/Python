valor = float (input ("inofrme o valor do produto "))
desconto = float (input ("informe a porcentagem de desconto "))

menos = float (valor * desconto/100)
final = float( valor - menos)
print ("o valor ficou de R$",final)
