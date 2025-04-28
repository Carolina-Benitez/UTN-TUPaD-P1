#Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. 
lista_range = list(range(4,101,4)) #empieza en 4, primer multiplo de 4
print (lista_range)

#Crear una lista con cinco elementos y mostrar el penúltimo. 
lista_elementos = [1,2,3,4,5]
print (lista_elementos[-2])

#Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
lista_vacia = []
lista_vacia.append("Hola")
lista_vacia.append("soy")
lista_vacia.append("Carolina")
print(lista_vacia)

#Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla.
animales = ["perro", "gato", "conejo", "pez"]
animales[1]= "loro"
animales[3]= "oso"
print(animales)

#Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#este programa crea una lista de numeros enteros e elimina el mas grande, en este caso el 22

#Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
lista_range = list(range(10,31,5))
print(lista_range[0], lista_range[1])

#Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualquiera. 
autos = ["sedan", "polo", "suran", "gol"]
autos[1]= "renault"
autos[2]= "siena"
print(autos)

#Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#Dada la lista “compras”: 
#a)Agregar "jugo" a la lista del tercer cliente usando append. 
#b)Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
#c)Eliminar "pan" de la lista del primer cliente.  
#d)Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#agregar jugo al tercer cliente
compras[2].append("jugo")
#reemplazar fideos por tallarines al segundo cliente
indice_fideos = compras[1].index("fideos") #encontramos la posicion (indice) de "fideos"
compras[1][indice_fideos]= "tallarines" #lo reemplazamos
#eliminar pan del primer cliente
compras[0].remove("pan") 

print(compras)

#Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
# ● Posición lista_anidada[0]: 15 
# ● Posición lista_anidada[1]: True 
# ● Posición lista_anidada[2][0]: 25.5 
# ● Posición lista_anidada[2][1]: 57.9 
# ● Posición lista_anidada[2][2]: 30.6 
# ● Posición lista_anidada[3]: False 

lista_anidada = [15, "true", [25.5, 57.9, 30.6], ["false"]]
print(lista_anidada)