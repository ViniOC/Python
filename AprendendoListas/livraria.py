def menu():
    print("1 - Insere livros")
    print("2 - Lista livros")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))
    return opcao

def insereLivro(lista):
    print("\n Inserindo livro...")
    titulo = input("Titulo: \n")
    autor = input ("Autor: \n")
    ano = int (input("Ano lançamento: \n"))
    preco = float(input("Preço\n"))
    lista.append(titulo)
    lista.append(autor)
    lista.append(ano)
    lista.append(preco)
    
    
def listaLivros (lista):
    i = 0
    while i < len(lista):
        print(f"{i}-> Titulo:{lista[i]} - Autor: {lista [i+1]}")
        
        i = i+4
        
    opcao = int(input("Posição do livro ou -1 para nenhum: "))
    return opcao
        
def subMenu():
    print("1 - altera\n 2 - exclui")
    return int(input("Selecione: "))

def altera_exclui (lista, posicao, opcao):
    if opcao == 2: #exclui
        for i in range (4):
            lista.pop(posicao)
    elif opcao == 1: #altera
        titulo = input(f"Titulo ({lista[posicao]}): ")
        if len (titulo)>0:
            lista[posicao] = titulo
            
        autor = input(f"Autor ({lista[posicao +1]}): ")
        if len (autor)>0:
            lista[posicao + 1] = autor
            
        ano = input(f"Ano ({lista[posicao +2]}): ")
        if len (ano)>0:
            lista[posicao + 2] = int (ano)
            
            
        preco = input(f"Preço ({lista[posicao +3]}): ")
        if len (preco)>0:
            lista[posicao + 3] = float(preco)
    
    
    
    

op = menu()
livros = ["Harry potter e a pedra filosofal", "jk rolling", 1997, 50.50, "menino do engenho", "jose", 1932, 35]
while op != 3:
    if op == 1:
        insereLivro(livros)
        print(livros)
    elif op == 2 :
        op2 = listaLivros(livros)
        print(f"Seleciona livro: {livros[op2]}")
        acao = subMenu()
        altera_exclui(livros, op2, acao  )
    else:
        print("Invalido")
        
    op = menu()
    
print("Saindo...")