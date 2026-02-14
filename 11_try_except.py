# try/except: evita que el programa inturrumpa 

def dividir(a, b): return a/b 
# resultado = dividir(5,5) # 1.0
# resultado = dividir(0,5) # 0.0
# #resultado = dividir(5,0) #! ZeroDivisionError: division by zero
# print(resultado) #

def dividir_saneada(a, b):
    try:
        resultado  = a/b 
        print(f'El resultado es {resultado}')
    except ZeroDivisionError:
        print('❌ No puedes divi entre 0')

dividir_saneada(5,0) #controlado
#dividir_saneada(5,'g') #!TypeError: unsupported operand type(s) for /: 'int' and 'str'

try:
    edad  = int(input('Ingrese su edad: '))
    print(f'Tu edad es {edad}')
except ValueError as e:
    print(f'⚠️ No digito un numero {e}') 
except Exception as e:
    print(f'An exception occurred {e}')



try: #? operacion riesgosa que intento hacer
    archivo = 'datos_ventas.csv'
    print(f'Abriendo el archivo {archivo}')
except FileNotFoundError: #! se ejecuta si una operacion o instruccion del try lanza error
    print('📁 No existe')

else:  #*se ejecuta si el try fue exitoso
        print(f'El archivo {archivo} es leido con exito')
finally:
    print(f'limpiar recursos...')





print('La programacion continua')
print('La programacion continua')
print('La programacion continua')
print('La programacion continua')