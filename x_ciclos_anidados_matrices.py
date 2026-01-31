
#? ⭐ Bucles anidados (loops dentro de loops): para recorrer matrices y acceder a cada elemento.
# Una matriz es una lista de listas
# Cada ele de la lista principal es una FILA de la matriz (una lista). = 'i'
# Cada ele dentro de una fila es un valor en una COLUMNA. = 'j'
# matriz = [
#     [0, 1, 1],  # fila 0
#     [1, 0, 1],  # fila 1
#     [1, 1, 0]   # fila 2
# ]

# El bucle externo itera sobre las filas (i es el índice de fila).
# El bucle interno itera sobre las columnas (j es el índice de columna), elemento por elemento.

#& 🤸🏻 Ejemplo para imprimir cada elemento con su posición:

matriz = [
    [1, 2, 3],  # fila 0
    [4, 5, 6],  # fila 1
    [7, 8, 9]   # fila 2
]

print('cuantos elementos o filas tiene la matriz ',len(matriz)) # 3
for i in range(len(matriz)):        # Por cada fila
    for j in range(len(matriz[i])): #uso range pq no se cuantos ele hay en esa fila, podria ser irregular
        valor = matriz[i][j]
        print(f'ele en fila {i} colum {j} es {valor}')


#? EXPLICACION DE RANGE → range(start, stop, step)
# range recive por parametro un escalar y retorna una serie de iterables, para ser recorridos.
# Su llamado NO crea una variable que guarda esa serie.
# Argumentos:
# start (opcional): entero donde comienza la secuencia. Por defecto = 0.
# stop (requerido si solo pasas un argumento): entero que marca el tope exclusivo (no se incluye).
# step (opcional): entero que indica el salto entre valores. 
# Por defecto = 1. Puede ser negativo para contar hacia atrás. No puede ser 0 (lanza ValueError).
#& Ejemplos prácticos 🔢
range(5)            # → 0, 1, 2, 3, 4
range(1, 5)         # → 1, 2, 3, 4
range(1, 10, 2)     # → 1, 3, 5, 7, 9
range(5, 0, -1)     # → 5, 4, 3, 2, 1
list(range(3))      # → [0, 1, 2]

mi_lista = [10, 20, 30, 40]
for i in range(len(mi_lista)):
    print(mi_lista[i])

#& 🤸🏻EJERCICIO: con el uso de la libreria time, vamos a imprimir los elementos de un range cada segundo
import time 
for i in range(5):
    print(i, end=' ', flush=True) # espera 1s para imprimir el siguente.
    time.sleep(1)
# flush=True → obliga a que lo que se ha impreso se escriba en la terminal en ese momento.
# es útil para ver salidas en tiempo real (barras de progreso, logs, o antes de sleep())


#TODO: ⛹🏽⛹🏽 ALUMNOS REALICEN EL SIGUIENTE EJERCICIO
# Imprime La diagonal principal de una matriz cuadrada.
# La diagonal principal son los elementos donde el índice de fila es 
# igual al índice de columna, es decir, donde i == j, 
# recuerda que la sabes usar condicionales.
matriz = [
    [0, 1, 1], # fila 0
    [1, 0, 1], # fila 1
    [1, 1, 0]  # fila 2
]

#* 💡SOLUCION EL EJERCICIO
print('\nIMPRIMIENDO LA DIAGONAL PRINCIPAL DE LA MATRIZ')
for i in range(len(matriz)):        # recorre 0, 1, 2 - indices de filas
    for j in range(len(matriz[i])): # recorre 0, 1, 2 - indices de columnas en fila i
        if i == j:
            print(f"Diagonal[{i}][{j}] = {matriz[i][j]}")


# TODO: Ahora que sabemos recorer iterables podemos podemos aprender mas sobre ellos
#? Explicacion ir a: 5_iterables_avanzados.py
