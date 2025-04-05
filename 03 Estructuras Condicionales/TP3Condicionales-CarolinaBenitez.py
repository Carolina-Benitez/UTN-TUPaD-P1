#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad= int(input("Escriba su edad: "))
if edad > 18:
    print("Es mayor de edad.")

#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota= float(input("Escriba su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
numero= float(input("Ingrese un numero: "))

#verificar si el numero es par
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
edad= int(input("Ingrese su edad: "))
if edad < 13:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
contraseña= input("Ingrese una contraseña: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random
import statistics

#definir la lista numeros_aleatorios
numeros_aleatorios = {random.randint(1, 100) for i in range(50)}

#calcular la media, mediana y moda
media= statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)

#intentamos obtener moda, puede haber un error si no existe una moda clara
try:
    moda = statistics.mode(numeros_aleatorios)
except statistics.StatisticsError:
    moda = "No hay una moda unica"

#imprimimos los resultados
print("Lista de numeros aleatorios:" , numeros_aleatorios)
print("Media:", media)
print("mediana:", mediana)
print("Moda:", moda)

#determinamos si hay sesgo
if isinstance(moda, int): #solo comparamos si hay una moda
    if media > mediana and media > moda:
        sesgo = "Sesgo positivo"
    elif media < mediana and media < moda: 
        sesgo = "Sesgo negativo"
    else:
        sesgo = "No hay sesgo"
else:
    sesgo = "No se puede determinar sesgo debido a que no hay una moda unica."

print("Sesgo:", sesgo)

#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

#solicitar una frase o palabra al usuario
palabra = input("Ingresa una frase o palabra: ")

#comprobar si la ultima letra es una vocal
if palabra[-1].lower() in "aeiouáéíóú":
    #si termina con una vocal, agregar un signo de exclamacion 
    palabra += "!"

#imprimir el resultado
print("Resultado:", palabra)

#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: Si quiere su nombre en mayúsculas, minúsculas o con la primera letra mayúscula. El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 

#solicitar el nombre al usuario
nombre = input("Ingrese su nombre: ")

#mostrar opciones para la transformación
print("¿De qué manera te gustaría ver tu nombre?")
print("1. En mayúsculas.")
print("2. En minúsculas.")
print("3. Con la primera letra en mayúscula.")

#solicitar la opción que desea el usuario
opcion = input("Selecciona una opción (1, 2, 3): ")

# transformar el nombre según la opción seleccionada
if opcion == '1':
    resultado = nombre.upper()  # Convierte todo el nombre a mayúsculas
elif opcion == '2':
    resultado = nombre.lower()  # Convierte todo el nombre a minúsculas
elif opcion == '3':
    resultado = nombre.capitalize()  # Convierte la primera letra a mayúscula
else:
    resultado = "Opción no válida."

#imprimir el resultado
print("Resultado:", resultado)

#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
magnitud = float(input("Ingrese la magnitud de un terremoto: "))
if magnitud < 3:
    categoria = "Muy leve"
elif magnitud >= 3 and magnitud < 4:
    categoria = "Leve"
elif magnitud >= 4 and magnitud < 5:
    categoria = "Moderado"
elif magnitud >= 5 and magnitud < 6:
    categoria = "Fuerte"
elif magnitud >= 6 and magnitud < 7:
    categoria = "Muy fuerte"
else:
    categoria = "Extremo"

#imprimir el resultado
print("La categoria del terremoto es:", categoria)

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

#solicitar al usuario la información
hemisferio = input("¿En qué hemisferio te encuentras? (N para norte, S para sur): ")
mes = int(input("¿Qué mes es? (1 a 12): "))
dia = int(input("¿Qué día del mes es? (1 a 31): "))

#validar que los valores ingresados sean correctos
if hemisferio not in ['N', 'S']:
    print("Hemisferio no válido. Ingresa 'N' para el hemisferio norte o 'S' para el hemisferio sur.")
elif mes < 1 or mes > 12:
    print("Mes no válido. Ingresa un número entre 1 y 12.")
elif dia < 1 or dia > 31:
    print("Día no válido. Ingresa un número entre 1 y 31.")
else:
    #determinar la estación según el hemisferio y la fecha
    if hemisferio == 'N':  #hemisferio norte
        if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
            estacion = "Verano"
        else:
            estacion = "Otoño"
    else:  #hemisferio sur
        if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
            estacion = "Invierno"
        else:
            estacion = "Primavera"

    #imprimir el resultado
    print(f"En el hemisferio {'norte' if hemisferio == 'N' else 'sur'}, el día {dia} del mes {mes} corresponde a la estación {estacion}.")
