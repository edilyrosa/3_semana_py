
# #& 1. IF
# #Se ejecuta un bloque si la condición es verdadera.
# # Sintaxis: 
# # if condición lógica a evaluar :
# #   indentación →  código py a ejecutar
# #?Sentencia else
# #Se usa para definir qué sucede si la condición del if es falsa. 
# # Por eso NO LE SIGUE NINGUNA condición lógica a evaluar.  
# # Se Ejecuta si ninguna condición previa es verdadera.
# # #? Ejercicio: Determine si un número es par o impar, 💡solo existen esas 2 posibilidades.

# print('Veamos si un número es par o impar')
# num = int(input('Ingrese un número: '))
# if num % 2 == 0:
#     print(f'{num} es par')
# else:
#     print(f'{num} es impar')
    
    
# #& 2. ELIF
# # Es la forma de agregar múltiples condiciones a una sentencia if-else. 
# #? Ejercicio: catalogue a un estudiante según su calificación, 
# # con rangos de {
# # +90,  -> # Excelente 🥳
# # +80,  -> # Muy bien 👏
# # +70,  -> # Bien 👍
# # +60,  -> # Suficiente 👌
# # else -> # Insuficiente 😞
# # }
# print('\nDeterminando calificacion de estudiante')
# calificacion = int(input('Ingrese la calificacion del estudiante: '))

# if calificacion < 1 or calificacion > 100:
#     print("Calificación no válida")
# elif calificacion >= 90:
#     print("Excelente 🥳")
# elif calificacion >= 80:
#     print(" Muy bien 👏")
# elif calificacion >= 70:
#     print("bien 👏")
# elif calificacion >= 60:
#     print("Suficiente 👌")
# else:
#     print("Insuficiente 😞")
    
# print('Fin del elif de calificaciones')








#***************************CLASE DE CONDIONALES.

#& IF - ANIDADOS
# Determine si usuario puede Conducir?
# condicion: debe tener licencia (True/False) y ( (ser mayor de edad (>=18)  o estar emancipado (si/no) )
print('\nDeterminando si usuario puede Conducir?')
licencia = input('Tienes licencia? (si/no): ').strip().lower()
edad = int(input('Ingrese su edad: '))
emancipado = input('Eres emancipado? (si/no): ').strip().lower()

if licencia == 'si':
    if edad >= 18 or emancipado == 'si':
        print('✅Tienes licencia y Eres mayor o eres emancipado, Puede Conducir')
    else: print('❌ No eres mayor ni eres emancipado, NO Puede Conducir')
else: print('❌ Legalmente NO Puede Conducir sin licencia')

#& TERNARIO
# Es una forma corta de escribir una sentencia if-else en una sola línea.
# Sintaxis: valor_si_verdadero if condición else valor_si_falso
print('\nAsignamos a una variable bandera de usuario autenticado o no')

autenticado = bool(int(input('Usuario autenticado? (0/1):')))
mensaje = '✅Usuario autenticado' if autenticado else '❌Usuario no autenticado'
print(mensaje)

#& match-case (match-case)
# Es una estructura de control que permite ejecutar diferentes bloques de código
# según el valor de una variable o expresión.
opcion = int(input("Selecciona una opción (1-7): "))

match opcion:
    case 1: # Coincidencia exacta (Literal)
        print("Elegiste 1.")
    # case 2 | 3: # El símbolo | significa "OR" (O una u otra)
    case 2 | 3 | 4 : # El símbolo | significa "OR" (O una u otra) En un match-case, no se usa la palabra or, sino el símbolo de tubería o pipe (|) para representar la unión de patrones.
        print("Elegiste 2, 3 o 4.")
        
    case n if n > 4 and n <= 7: # Uso de Guardia (IF) para rangos,  # Aquí el 'and' se escribe normal porque está dentro de un 'if'
        print("Elegiste 5, 6 o 7")
        
    case n if n >= 8: # Uso de Guardia (IF) para rangos
        print(f"La opción {n} está fuera de rango.")
        
    case _: # Comodín
        print("Opción no válida.") #! < 0 son opciones no válidas
        
# el case _ siempre debe ir al final de la estructura match-case. 
# Si intentas poner otro case después de este, Python arrojará un error 
# porque ese código sería inalcanzable.    

# TODO PROXIMO_TEMA:
    # TIPOS DE DATOS ESTRUCTURALES: LISTAS, TUPLAS, STR
    # #? ir a: 2_TDD_Estructurales.py

