n = int(input("Digite um número: "))

while n <= 0:
    n = int(input("Vlor Invalido, digite um número: "))

ant = 0
atual = 1
prox = 1
for i in range (n-2):
   ant = atual
   atual = prox
   prox = ant + atual
   
   position = i
print(f"posição {n} = {prox}")
   

       




# if n == 1 or n == 2:
#     print("fibonacci vale 1")
# else:
#     ant = 1
#     atual = 1
#     prox = ant + atual
#     position = 3
    
#     while position < n:
#         ant = atual
#         atual = prox
#         prox = ant + atual
#         position += 1
#         print(f"posição {position} = {prox}")
    
    


