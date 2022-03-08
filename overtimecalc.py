# Overtime calculator

horas = float(input("Quantas horas trabalhadas? "))
valor = float(input("Qual valor da hora de trabalho? "))
valor_hora_extra = valor*1.5

while (horas < 0):
    horas = float(
        input("Horas trabalhadas negativas, favor informar horas correta! "))
while (valor < 0):
    valor = float(
        input("Valor da hora trabalhada negativo, favor informar valor correto! "))
if (horas >= 160):
    salario = 160*valor + (horas - 160)*valor_hora_extra
    print("Salário com hora extra = R$", salario)
else:
    salario = horas*valor
    print("Salário = R$", salario)
