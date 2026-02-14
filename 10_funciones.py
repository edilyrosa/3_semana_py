


#* FUNCIONES EN PY.
# Las funciones son bloques de código reutilizables que realizan una tarea específica.
# Se definen usando la palabra clave def, seguida del nombre de la función y paréntesis ().
# Pueden aceptar parámetros (entradas) y devolver valores (salidas) usando la palabra clave return.
#! Si una función está definida para recibir un número específico de argumentos 
#! y le pasas más (o menos), lanza: TypeError.


#?⭐ Definición de una función simple
def saludar(nombre):
    return f'Hola {nombre}'

#?⭐ Llamada a la función
saludo = saludar('Edily')
print(saludo)       # Hola Edily
#print(saludo+5) #! can only concatenate str (not "int") to str        # Hola Edily
print(saludar('Rosa')) # Hola Rosa

#?⭐ Función con múltiples parámetros
def sumar(a, b):
    return a + b

resultado  = sumar(5, 5)
#resultado2  = sumar(5)
print(resultado+5) #15
#print(resultado2) #!ypeError: sumar() missing 1 required positional argument: 'b'

#?⭐ Función sin parámetros
def obtener_pi():
    return 3.14159

pi_valor  =  obtener_pi()
print(pi_valor) #3.14159

#?⭐ Función sin valor de retorno
def muestra_mensaje():
    print('Este es un mensaje desde una funcion')

muestra_mensaje() #Este es un mensaje desde una funcion

#?⭐ Función con valor por defecto en parámetros  
def potencia(base, exponente=2):
    return base ** exponente


print(potencia(2, 3))   #8
print(potencia(2))      #4

# # TODO: TRY- EXCEPT
#? ir a 11_try_except.py