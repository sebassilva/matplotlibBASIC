def insertionSort(n_lista):
    for index in range(1,len(n_lista)):
        actual = n_lista[index]
        posicion = index
        print("valor a ordenar = {}".format(actual))
        while posicion>0 and n_lista[posicion-1]>actual:
            n_lista[posicion]=n_lista[posicion-1]
            posicion = posicion-1           
        n_lista[posicion]=actual
        print(n_lista)
        print() 
    return n_lista

#Datos de 
"""
lista = [21, 10, 0, 11, 9, 24, 20, 14, 1]
print("lista desordenada {}".format(lista))
insertionSort(lista)
print("lista ordenada {}".format(lista))
"""
print("SEGUNDO METODO")
print("SEGUNDO METODO")
print("SEGUNDO METODO")
print("SEGUNDO METODO")

def quicksort(lista):
    quicksort_aux(lista,0,len(lista)-1)

def quicksort_aux(lista,inicio, fin):
    if inicio < fin:

        pivote = particion(lista,inicio,fin)

        quicksort_aux(lista, inicio, pivote-1)
        quicksort_aux(lista, pivote+1, fin)

def particion(lista, inicio, fin):
    #Se asigna como pivote en número de la primera localidad
    pivote = lista[inicio]
    print("Valor del pivote {}".format(pivote))
    #Se crean dos marcadores 
    izquierda = inicio+1
    derecha = fin
    print("Índice izquierdo {}".format(izquierda))
    print("Índice derecho {}".format(derecha))

    
    bandera = False
    while not bandera:
        while izquierda <= derecha and lista[izquierda] <= pivote:
            izquierda = izquierda + 1
        while lista[derecha] >= pivote and derecha >=izquierda:
            derecha = derecha -1
        if derecha < izquierda:
            bandera= True
        else:
            temp=lista[izquierda]
            lista[izquierda]=lista[derecha]
            lista[derecha]=temp
            
    print(lista)


    temp=lista[inicio]
    lista[inicio]=lista[derecha]
    lista[derecha]=temp
    return derecha


"""
lista = [21, 10, 0, 11, 9, 24, 20, 14, 1]
print("lista desordenada {}".format(lista))
quicksort(lista)
#Importando librerías
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
#print("lista a graficar  perrrro {}".format(lista))
"""
#Cargando módulos
import random
from time import time





#Tamaños de la lista de números aleatorios a generar
datos = [ii*5 for ii in range(1,5)] 

tiempo_is = []  #Lista para guardar el tiempo de ejecución de insert sort
tiempo_qs = []  #Lista para guardar el tiempo de ejecución de quick sort

for ii in datos:
    lista_is = random.sample(range(0, 444), ii)
    #Se hace una copia de la lista para que se ejecute el algoritmo con los mismo números
    lista_qs = lista_is.copy() 
    
    t0 = time()  #Se guarda el tiempo inicial
    insertionSort(lista_is)
    tiempo_is.append(round(time()-t0, 6))   #Se le resta al tiempo actual, el tiempo inicial
    
    t0 = time()    
    quicksort(lista_qs)
    tiempo_qs.append(round(time()-t0, 6))

#Imprimiendo tiempos parciales de ejecución
print("Tiempos parciales de ejecución en INSERT SORT {} \n".format(tiempo_is))
print("Tiempos parciales de ejecución en QUICK SORT {}".format(tiempo_qs))

#Imprimiendo tiempos totales de ejecución
#Para calcular el tiempo total se aplica la función sum() a las listas de tiempo
print("Tiempo total de ejecución en insert sort {}".format(sum(tiempo_is)))
print("Tiempo total de ejecución en quick sort {}".format(sum(tiempo_qs)))

#Generando la gráfica
"""
fig, ax = subplots()
ax.plot(datos, tiempo_is, label="insert sort", marker="*",color="r")
ax.plot(datos, tiempo_qs, label="quick sort", marker="o",color="b")
ax.set_xlabel('Datos') 
ax.set_ylabel('Tiempo') 
ax.grid(True)
ax.legend(loc=2); 
plt.title('Tiempo de ejecución (insert vs. quick)')
plt.show()
"""

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = datos
y = tiempo_is

x2 = datos
y2 = tiempo_qs

# can plot specifically, after just showing the defaults:
plt.plot(x,y,linewidth=5)
plt.plot(x2,y2,linewidth=5)

plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
