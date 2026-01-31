
#* FUNCIONES EN PY.
# Las funciones son bloques de código reutilizables que realizan una tarea específica.
# Se definen usando la palabra clave def, seguida del nombre de la función y paréntesis ().
# Pueden aceptar parámetros (entradas) y devolver valores (salidas) usando la palabra clave return.


#?⭐ Definición de una función simple
def saludar(nombre):
    """Función que saluda a una persona por su nombre."""
    return f"Hola, {nombre}!"       


#?⭐ Llamada a la función
mensaje = saludar("Ana")
print(mensaje)  # Salida: Hola, Ana!


#?⭐ Función con múltiples parámetros
def sumar(a, b):
    """Función que suma dos números."""
    return a + b 
resultado = sumar(5, 3)

print(resultado)  # Salida: 8


#?⭐ Función sin parámetros
def obtener_pi():
    """Función que devuelve el valor de pi."""
    return 3.14159
pi_valor = obtener_pi()
print(pi_valor)  # Salida: 3.14159      


#?⭐ Función sin valor de retorno
def mostrar_mensaje():
    """Función que muestra un mensaje en pantalla."""
    print("Este es un mensaje desde una función.")      
mostrar_mensaje()  # Salida: Este es un mensaje desde una función.


#?⭐ Función con valor por defecto en parámetros    
def potencia(base, exponente=2):
    """Función que calcula la potencia de un número."""
    return base ** exponente
print(potencia(3))      # Salida: 9 (3 al cuadrado)
print(potencia(2, 3))   # Salida: 8 (2 al cubo)

