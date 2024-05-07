sorteada = input("Digite a palavra secreta: ")
erros = 0
sorteada = sorteada.lower()
segredo = ""
for i in range(len(sorteada)):
    if sorteada[i] == " ":
        segredo += " "
    else:
        segredo += "_"
        

        
print(f"{segredo}\n erros: {erros}" )
while segredo != sorteada and erros < 6:
    letra = input("Digite uma letra: ").lower()
    if letra in sorteada:
        for i in range(len(sorteada)):
            if sorteada[i] == letra:
                segredo = segredo[:i] + letra + segredo[i+1:]
            
   
    else:
        erros += 1
        
    print(f"{segredo}\n erros: {erros}" )
