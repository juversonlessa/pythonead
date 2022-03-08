# Power of number
def f(x):
    x_aux = x * x
    return x_aux


num = float(input("Coloque o número: "))
num_quadrado = f(num)
num = round(num, 2)
num_quadrado = round(num_quadrado, 2)
print(num, " ao quadrado é ", num_quadrado)
