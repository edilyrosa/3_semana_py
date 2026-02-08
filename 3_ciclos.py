
# #&=======================FOR
# # for var_ele in mi_iterable:
#         # programacion dentro del for, donde tienes acceso a la {var_ele}
        
# lista = [1, 5, 2, 3, 4] # → lista, la conoces
# for mi_ele in lista:
#     print(f'mi ele = ', mi_ele)

# for mi_ele in lista:
#     print(f'elev {mi_ele}^2 = ', mi_ele**2)
    

# lista_nueva = []
# print(lista_nueva)
# for e in lista:
#     lista_nueva.append(e**2)
#     print(f'nuevo elemento a la nueva lista {e**2}')
# print(lista_nueva)



# for e in lista: # [1, 5, 2, 3, 4]
#     if(e %2 == 0):
#         print(f'el elemento {e} es par')

# # print(f'mi ele fuera del loop= ', lista[0])
# # print(f'mi ele fuera del loop= ', lista[1])
# # print(f'mi ele fuera del loop= ', lista[2])
# lista.sort()
# print(lista)
# for e in lista: # [1, 2, 3, 4, 5]
#     if(e == 4):
#         break
#     print('esto se imprimira 2 vcs')
    
# print('soy flujo principal')

  
# for e in lista: # [1, 2, 3, 4, 5]
#     if(e == 3):
#         continue
#     print(f'Soy ele {e}')
    
# print('soy flujo principal')  


# for e in lista: # [1, 2, 3, 4, 5]
#     pass

# #&======================WHILE
# i = 1 #*ITERADOR FUERA DEL WHILE ⚠️ cuidado ! evita los looop int 
# while i<=5:
#     print(f'valor de {i}')
#     i+=1 #*INCREMENTO O DECREMENTO DEL ITERADOR DENTRO DEL WHILE 💡 debes establecer la forma de incrementar o cambiar el valor del iterador para evitar un loop infinito

# tupla = 1,2,3,'cuatro', 2, 4, 5
# tupla[0]
# # tupla = (1,2,3,'cuatro')
# indice = 5 
# while indice < len(tupla):
#     print(tupla[indice])
#     indice +=1 #*INCREMENTO O DECREMENTO

    
VERDE ="\033[32m"
AZUL ="\033[34m"
CYAN ="\033[36m"
ROJO ="\033[31m"
RESET ="\033[0m"

while True:
    print(f'\n{AZUL}---------- MENU DE OPCIONES ----------{RESET}')
    print('1. Ver perfil')
    print('2. Ver Cargar archivo')
    print('3. Visualizar')
    print('4. Salir')
    
    opcion = input(f'{CYAN}Digite su opcion: {RESET}')
    match opcion:
        case "a" | 'b' | 'c':
            print(f'{ROJO} Opn invalida ❌😡 {RESET}')
        case '1':
            print(f'{VERDE} Viendo perfil {RESET}')
        case '2':
            print(f'{VERDE} cargando {RESET}')
        case '3':
            print(f'{VERDE} viendo {RESET}')
        case '4':
            print(f'{VERDE} saliendo del sistema {RESET}')
            break
        case _:
            print(f'{ROJO} opc invalida {RESET}')
            