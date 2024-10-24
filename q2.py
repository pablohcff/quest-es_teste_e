numero = 15

a, b = 0, 1

faz_parte = False

while a <= numero:
    if a == numero:
        faz_parte = True
        break

    a, b = b, a + b  

if faz_parte:
    print(f"O número {numero} faz parte da sequência de Fibonacci.")

else:
    print(f"O número {numero} não faz parte da sequência de Fibonacci.")
