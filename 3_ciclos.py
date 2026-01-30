

#& *****************************************PRIEMRO: Que es un iterable??
# Estructura de datos que agrupa elemento que puedes ser iterados o recorridos
# uno a uno dentro de un bucle, para por ejemplo, manipularlos, filtrarlos, mapearlos. 
# Como: las listas, tuplas, cadenas de texto, diccionarios.


#& ***************************************** FOR
# Ciclo que recorre una iterable.
# Sintaxis: 
# for variable_elemento in el_iterable:
     # bloque de código usando variable_elemento


#? 1.⭐ Recorrer una lista con for
lista = [1, 2, 3, 4, 5] # → ✅ Ya las conoces
for elemento in lista:
    print('Ele - ', elemento) #Ele -  1...
    
for ele in lista:
    print('Eleva', ele**2)    #Eleva 4...

lista_new = []
for e in lista:
    lista_new.append(e**2)
print('lista_new', lista_new) #lista_new [1, 4, 9, 16, 25]

#? 2.⭐ Puedes establecer un condicional dentro de un bucle.
for ele in lista:
    if(ele %2 == 0):
        print(f'los pares dentro de la lista son: {ele}') # los pares son 2, 4

#? 3.⭐ Sentencias de control dentro de bucles:
# Interrumpe y sale completamente del bucle, sin importar la condición del ciclo.
# y continua ejecutando la programacion principal
#? √ break 
for i in lista:
    if(i == 3):
        break
    print(f'Imprimimos hasta 2, ele = {i}') 
print('👋🏻Hemos salido del bucle con break')

# Salta el resto del código y pasa a la siguiente iteración.
#? √ continue 
for i in lista:
    if(i == 3):
        continue
    print(f'Imprimimos, ele = {i}') 
print('👋🏻Hemos salido del bucle con continue')

# No hace nada, es un marcador de posición 
#? √ pass
# útil para mantener la sintaxis cuando quieres dejar código pendiente.
for i in lista:
    pass

#& *******************WHILE
# Repite un bloque de código mientras una condición lógica sea verdadera.
# Sintaxis:
# Definicion inicial del iterador  🚩
# while condición:
#     # bloque de código a repetir
#     # actualizacion del iterador 🚩

#! 🚩🚩🚩👀🤯❌ Si no modificas una variable DENTRO del while que termina la condición,
#! puede generar un bucle infinito.

i = 1
while i <= 5:
    i+=1
    print(f'valor de i: {i}') # → f' {var}' Sintaxis de formato de interpolacion.


#& *******************EXISTEN OTROS METODOS CICLICOS PARA MANIPULAR ITERABLES
#?⭐ Metodo map()
# Es una función que presenta 2 parametros 
# 1er parametro: la función que se aplica a cada elemento
# 2do parametro: iterable (lista, tupla...) de los elementos a procesar
# Rertorna: otro iterable con los elementos resultados o procesados.

#? 🤸🏻Ejercicio: Elevar al cuadrado cada elemento
nums = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, nums)) # x es cada elemento de la lista nums
print(cuadrados)  # [1, 4, 9, 16]

#? 💡EXPLICACION DEL ANTERIOR CODIGO:
# TODO: 🔥mas adelante veremos a detalle las funciones y sus tipos, parametros y return. Pero:
# lambda es una función anónima para operaciones simples y rápidas. se define en 1 linea. Su sintaxis es:
# lambda argumentos: expresión

suma = lambda x, y: x + y
print(suma(3, 4))  # Salida: 7
#? 💡Lo mismo que lo anterior, pero con uso directo sin asignar a variable
print((lambda x, y: x + y)(3, 4))  # Salida: 7


#? ⭐ metodo filter()
# 1er parametro: función critero para filtrar elementos, mediante condicion logica a evaluar
# 2do parametro: iterable (lista, tupla...) de los elementos a filtrar
# Rertorna: otro iterable con los elementos filtrados.
# 💡Utilidad: filtrar los items de productos excentos del pago de impuesto.

#? 🤸🏻Ejercicio: crear una lista con solo números pares de otra lista.
pares = list(filter(lambda x: x % 2 == 0, nums))
print(pares)  # [2, 4]


# TODO: Cliclos Anidados - Matrices.
#? Explicacion ir a: 4_ciclos_anidados_matrices.py


