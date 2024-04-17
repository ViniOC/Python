# funcionalidades do sistema:
# alugar veiculo
# devolver veiculo
# cadastrar cliente
# consiltar veiculo disponivel

opcao = 0

while opcao != 5:

    print("Bem vindo a locadora de veiculos!!\n Selecione uma opção:\n ---1 - Alugar veiculo--------------\n ---2 - Devolver veiculo------------\n ---3 - Cadastrar cliente-----------\n ---4 - Consultar veiculo disponivel\n ---5 - -------Sair-----------------\n")

    opcao = int(input("Digite a opção desejada: "))   

    
    match opcao:
        case 1:
            print("Alugar veiculo")
        case 2:
            print("Devolver veiculo")
            
        case 3:
            print("Cadastrar cliente")
            
            cpf = int (input("Digite o CPF do cliente: "))
            nome = input("Digite o nome do cliente: ")
            idade = int(input("Digite a idade do cliente: "))
            print(f"Cliente cadastrado com sucesso! CPF: {cpf} Nome: {nome} Idade: {idade}")
            
        case 4:
            print("Consultar veiculo disponivel")
        case 5:
            print("Saindo...")
        case _:
            print("Opção invalida")