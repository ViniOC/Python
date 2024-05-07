
def verificaNumeroPrimo(numero):
    print(numero)
    for i in range (2, numero):
        if numero % i == 0 and numero != i:
            return False
        
    return True

numero = int (input( "Informe um numero: "))

primo = verificaNumeroPrimo(numero)

print(primo)
            
