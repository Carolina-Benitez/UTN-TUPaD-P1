#Crea un programa que imprima en pantalla todos los numeros enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un numero por linea.
for i in range(101):
    print(i)

#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
numero = int(input("Ingresa un número entero: "))

#usa valor absoluto para ignorar el signo negativo si lo hay, y contar solo los digitos
numero_abs = abs(numero)

#convierte a cadena y cuenta los dígitos
cantidad_digitos = len(str(numero_abs))

print(f"El número tiene {cantidad_digitos} dígito(s).")

#Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

#solicitar los dos valores al usuario
primer_valor = int(input("Ingrese el primer numero: "))
segundo_valor = int(input("Ingrese el segundo numero: "))

#asegurarse de que el primer valor sea el menor
menor = min(primer_valor, segundo_valor)
mayor = max(primer_valor, segundo_valor)

#sumar los numeros entre los dos valores (excluyendo ambos) 
suma = 0
for x in range(menor + 1, mayor):
    suma = suma + x 

print(f"La suma de los numeros entre {primer_valor} y {segundo_valor} es: {suma}")

#Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

numero = int(input("Ingresa un número entero (0 para terminar): "))
total = 0

while numero != 0:
    total = total + numero
    #mientras el numero no sea 0, lo suma y vuelve a pedir otro
    numero = int(input("Ingresa otro número (0 para terminar): "))

print(f"La suma total es: {total}")

#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

#generar el número secreto entre 0 y 9
numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

print("Adivina el número (entre 0 y 9):")

while adivinado == False:
    intento = int(input("Ingresa tu intento: "))
    intentos = intentos + 1

    if intento == numero_secreto:
        adivinado = True
    else:
        print("Incorrecto, intenta de nuevo.")

print(f"¡Correcto! El número era, {numero_secreto}. Número de intentos: {intentos}.")

#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
for i in range(100,-1, -1):
    if i % 2 == 0:
        print(i)

#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario
numero = int(input("Ingrese un numero positivo: "))

#verificar que el numero sea valido
if numero >= 0:
    suma = 0 #contador
    for i in range(numero + 1):  #incluye el número ingresado
        suma = suma + i
    print("La suma de los números desde 0 hasta", numero, "es:", suma)
else:
    print("Debes ingresar un número entero positivo.")

#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos.

#inicializar contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

print("Ingresa 100 números enteros: ")

for i in range(1, 101):
    numero = int(input(f"Número {i}: "))

    #contar pares e impares
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

    #contar positivos y negativos
    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1

print("Resultados:")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores

#inicializar la suma total
suma_total = 0

print("Ingresa 100 números enteros:")

for i in range(1, 101):
    numero = int(input(f"Número {i}: "))
    suma_total = suma_total + numero

#calcular el promedio
media = suma_total / 100

print("La media de los 100 números ingresados es: ", media)

#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.
numero = input("Ingresa un número entero: ")

#verificar si es negativo
if numero.startswith('-'):
    invertido = '-' + numero[:0:-1]  #ignora el signo al invertir
else:
    invertido = numero[::-1]  #invertir los digitos. 

print("Número invertido:", invertido)







