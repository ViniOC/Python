st = input("Digite uma palavra: ")
letra = input("Escolha uma letra para censurar: ")

for i in range (len(st)):
    if st[i] == letra:
        st = st[:i] + "*" + st[i+1:]

print(st)