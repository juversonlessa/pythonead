def countdown(n):
    if n == 0:
        print("Acabou")
    else:
        print(n)
        countdown(n-1)


num = int(input("Coloque um número: "))
countdown(num)
