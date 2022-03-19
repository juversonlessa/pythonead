def salarioVendedor(vendas):
    if (vendas < 5000):
        return float(1000 + (vendas*0.01))
    elif (5000 < vendas < 10000):
        return float(1000 + (vendas*0.015))
    elif (vendas > 10000):
        return float(1000 + (vendas*0.02))


vendasEmily = float(input('Quanto Emily vendeu? '))
vendasLarissa = float(input('Quanto Larissa vendeu? '))
vendasRafael = float(input('Quanto Rafael vendeu? '))
vendasMilena = float(input('Quanto Milena vendeu? '))

salarioEmily = salarioVendedor(vendasEmily)
salarioLarissa = salarioVendedor(vendasLarissa)
salarioRafael = salarioVendedor(vendasRafael)
salarioMilena = salarioVendedor(vendasMilena)

faturamentoTotal = (vendasEmily + vendasLarissa + vendasMilena + vendasRafael)
salarioJessica = (2000 + (faturamentoTotal*0.005))
totalSalarios = (salarioEmily + salarioLarissa +
                 salarioRafael + salarioMilena + salarioJessica)

print('Faturamento total = {:.2f}'.format(faturamentoTotal).replace('.', ','))
print('Salário da Emily = {:.2f}'.format(salarioEmily).replace('.', ','))
print('Salário da Larissa = {:.2f}'.format(salarioLarissa).replace('.', ','))
print('Salário do Rafael = {:.2f}'.format(salarioRafael).replace('.', ','))
print('Salário da Milena = {:.2f}'.format(salarioMilena).replace('.', ','))
print('Salário da Jéssica = {:.2f}'.format(salarioJessica).replace('.', ','))
print('Total dos salários = {:.2f}'.format(totalSalarios).replace('.', ','))
