
# & condcionales anidados: es para determianr una gran coindcion antes de continhuar
# ejercicio: ncesitamos saber si la perosna puede condducir
# condcion a evaluar : licencia AND (mayor OR emancipado)

# licencia = input('tienes licencia (si/no): ').strip().lower()
# edad = int(input('Digita tu edad: '))
# MAYORIDAD = 18
# emancipado = input('estas emancipado (si/no): ').strip().lower()

# if licencia == 'si':
#     if edad >= MAYORIDAD or emancipado == 'si':
#         print('✅Puedes conducir')
# else: 
#     print('❌No puedes conducir sin licencia')
    
    
    
    
# &TERNARIO: es una forma resumida de establecer un condcional.
# is_auth = False
# # mensaje = 'si es true' if is_auth else "si es falso" → TERNADIO
# mensaje = '✅Puede entrar al sistema' if is_auth else "❌ no pued eentra al sistema"
# print(mensaje)


#& match - case

opcion = int(input('Digita un num 1-7: '))

match opcion:
    case 1: #valor exac
        print('Digito 1')
        
    case 2 | 3 | 4: # Pipe es = al OR, no puedes usar el "OR"
        print('Digito 2 o 3 o 4')
        
    case i if i > 4 and i <= 7: # rango con if y AND
        print(f'Digitaste {i} que esta dentro del conjunto de  5-7 ')
        
    case op if op >=8:
        print(f'Digito {op} esta fuera de rango')
        
    case _:
        print('Opcion invalida')

print('RESTO DE LA PROG DEL FLUJO PRINCI')