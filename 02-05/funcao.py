def transforma_caixa_alta (nome):
    nome = nome.upper()
    return nome

def adiciona(conjunto, valor):
    conjunto.append(valor)
    
    
valor = "Ontem foi feriado"
valor = transforma_caixa_alta(valor)
print(valor)

array = []

adiciona(array, valor)

print (array)