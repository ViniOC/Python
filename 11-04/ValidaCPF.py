cpf = int (input("Informe seu CPF apenas com numeros: "))

final_cpf = cpf % 100
cpf_1 = cpf // 100

final_cpf_1 = cpf_1 % 1000
cpf_2 = cpf_1 // 1000

final_cpf_2 = cpf_2 % 1000
cpf_3 = cpf_2 // 1000

final_cpf_3 = cpf_3 % 1000

print(f"cpf: {final_cpf_3}.{final_cpf_2}.{final_cpf_1}-{final_cpf}")

