#  //1. Nome e idade?
#  //2. J´a fez algum curso superior (mesmo que n˜ ao tenha
#  conclu´ ıdo)? Qual?
#  3. Por quˆ e escolheu Tecnologia da Informa¸ c˜ ao (TI)?
#  4. Dentro de TI, j´ a sabe no que vocˆe gostaria de trabalhar?
#  5. Quais s˜ ao seus hobbies?
nome = input ("qual o seu nome?")
idade = input ("qual a sua idade ?")
curso = input ("já fez algum curso superior?qual?")
escolha = input ("por que escolheu TI?")
trabalho = input ("em qual area gostaria de trabalhar ?")
hobbies = input ("quais são os seus hobbies?")

arq = open("dados.txt", "w")
arq.write(f"{nome}|{idade}|{curso}|{escolha}|{trabalho}|{hobbies}")
arq.close()