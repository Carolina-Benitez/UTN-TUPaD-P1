#Ejercicio 1- Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!".
print("Hola Mundo!")

#Ejercicio 2- Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
nombre = input ("Por favor, ingrese su nombre: ")
print(f"¡Mucho gusto, {nombre}""!")

#Ejercicio 3- Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
nombre = input ("Por favor, ingrese su nombre y apellido: ")
edad = input ("¿Cuantos años tienes?: ")
residencia = input ("¿Cual es su lugar de residencia?: ")
print(f"soy {nombre}, tengo {edad} y vivo en {residencia}")

#Ejercicio 4- Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio = int(input("ingrese el radio: "))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio 
print("perimetro:", perimetro, "area:", area)

#Ejercicio 5- Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Por favor, ingrese una cantidad de segundos: "))
horas = segundos//3600
print(f"Los {segundos} segundos ingresados equivalen a {horas} horas ") 

#Ejercicio 6- Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero = int(input("Por favor, ingrese un numero: ")) 
for i in range(0,11):
    resultado = i * numero
    print(f"{numero} x {i} = {resultado}") 

#Ejercicio 7- Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = int(input("Por favor, ingrese un primer numero entero que no sea 0: "))
numero2 = int(input("ingrese un segundo numero entero que no sea 0: "))
suma = numero1+numero2
division = numero1//numero2
multiplicacion = numero1*numero2
resta = numero1-numero2
print(f"La suma de los numeros ingresados es: {suma}, la division es: {division}, la multiplicacion es: {multiplicacion}, y la resta es: {resta}")

#Ejercicio 8- Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
peso = float(input("Por favor, ingrese su peso en kg: "))
altura = float(input("Por favor, ingrese su altura en mts: "))
masa_corporal = peso/(altura)**2
print(f"su indice de masa corporal es: {masa_corporal}")

#Ejercicio 9- Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"la temperatura en grados fahrenheit es: {fahrenheit}")

#Ejercicio 10- Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
numero1 = float(input("Por favor, ingrese el primer numero: "))
numero2 = float(input("Por favor, ingrese el segundo numero: "))
numero3 = float(input("Por favor, ingrese el tercer numero: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"el promedio de los numeros ingresados es: {promedio}")

