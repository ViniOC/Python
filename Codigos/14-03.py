dias_uteis = int(input("informe a qnt de dias uteis: "))

horas_trabalhadas = float(input("Horas trabalhadas: "))

salario_hora = float(input("Salario por hora: "))

jornada = dias_uteis * 8
valor_hora_extra = 0.0
salario = jornada*salario_hora

if horas_trabalhadas > jornada:
    #tenho horas para calcular
   hora_extra = horas_trabalhadas - jornada
   valor_hora_extra = hora_extra * salario_hora *1.5
   
   salario = horas_trabalhadas * salario_hora + valor_hora_extra
   
   print(f"horas-extras: R${valor_hora_extra}")

print(f"salario: R${salario}")
