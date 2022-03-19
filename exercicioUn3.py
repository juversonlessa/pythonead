a = float(0)
b = float(0)

while(a >= b):
    a = input('Digite um valor para A:')
    b = input('Digite um valor para B:')

    if(a == b):
        print('Valores de A e B iguais!', 'A = ', a, ', B = ', b)
    if(a > b):
        print('Valor de A é maior que B!', 'A = ', a, ', B = ', b)

if b > a:
    print('Valor de B é maior que valor de A.')
    print('A = ', a, 'B = ', b)
    print('Fim do algoritmo')
