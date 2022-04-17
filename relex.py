nomes = []
salarios = []
despesasIntegrantes = []
despesaTotal = 0
opcao = "sim"
pessoaIndex = 0

while (opcao == "sim"):
    nomes.append(input("Insira um integrante: "))
    salarios.append(
        float(input('Insira o salario de %s: ' % nomes[pessoaIndex])))
    pessoaIndex += 1

    if (len(nomes) >= 2):
        opcao = input("Você que adicionar mais um integrante?")

despesaTotal = float(input('Insira a despesa total: '))


for salario in salarios:
    despesasIntegrantes.append(float(
        despesaTotal * (salario/sum(salarios))))

for i in range(len(nomes)):
    print('A despesa de {} é R${:.2f}'.format(
        nomes[i], despesasIntegrantes[i]).replace('.', ','))
