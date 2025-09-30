def converson_binario(n):
    if n == 0:
        resultado = 0
    pila = []
    #apila los residuos
    while n > 0:
        pila.append(str(n % 2))
        n = n // 2
    #desapila en orden inverso
    binario = ''
    while pila:
        binario += pila.pop()
    resultado = binario
    return resultado

#Uso
numero = int(input('numero decimal->'))
binario = converson_binario(numero)
print(f'El numero decimal ingresado{numero} en binario es {binario}')