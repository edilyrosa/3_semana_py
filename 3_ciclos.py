
#&=======================FOR
# for var_ele in mi_iterable:
        # programacion dentro del for, donde tienes acceso a la {var_ele}
        
lista = [1, 5, 2, 3, 4] # → lista, la conoces
for mi_ele in lista:
    print(f'mi ele = ', mi_ele)

for mi_ele in lista:
    print(f'elev {mi_ele}^2 = ', mi_ele**2)
    

lista_nueva = []
print(lista_nueva)
for e in lista:
    lista_nueva.append(e**2)
    print(f'nuevo elemento a la nueva lista {e**2}')
print(lista_nueva)



for e in lista: # [1, 5, 2, 3, 4]
    if(e %2 == 0):
        print(f'el elemento {e} es par')

# print(f'mi ele fuera del loop= ', lista[0])
# print(f'mi ele fuera del loop= ', lista[1])
# print(f'mi ele fuera del loop= ', lista[2])
lista.sort()
print(lista)
for e in lista: # [1, 2, 3, 4, 5]
    if(e == 4):
        break
    print('esto se imprimira 2 vcs')
    
print('soy flujo principal')

  
for e in lista: # [1, 2, 3, 4, 5]
    if(e == 3):
        continue
    print(f'Soy ele {e}')
    
print('soy flujo principal')  


for e in lista: # [1, 2, 3, 4, 5]
    pass

#&======================WHILE
i = 1 #⚠️ cuidado ! evita los looop int 
while i<=5:
    print(f'valor de {i}')
    i+=1 #💡 debes establecer la forma de incrementar o cambiar el valor del iterador para evitar un loop infinito
    
    
#TODO PENDIENTE MAP() Y FILTER()