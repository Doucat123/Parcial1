#Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la cual se almacenaban en una 
# pila en cada misión de caza que emprendió (con la siguiente información planeta visitado, a quien 
# capturado, costo de la recompensa), resolver las siguientes
#actividades:

#a. Mostrar los planetas visitados en el orden hizo las misiones.
#b. Determinar cuántos créditos galácticos recaudo en total.
#c. Determinar el número de la misión en que capturo a Han Solo y en que planeta fue, suponga que dicha 
# misión está cargada.
from clases import Pila

misiones= [{"planeta":"luna","capturado":"toro","recompensa":1234},
        {"planeta":"pluton","capturado":"Han Solo","recompensa":632},
        {"planeta":"saturno","capturado":"walter","recompensa":2345},
        {"planeta":"tierra","capturado":"rupia","recompensa":234},
        {"planeta":"marte","capturado":"cristal","recompensa":654}
        ]

pila = Pila()
for i in range(len(misiones)): #Agrego la información a la pila
    mis = misiones[i]
    pila.push(mis)


aux = Pila()
ac = 0
cont = 0
while pila.size() > 0:
    dat = pila.pop()
    ac += dat["recompensa"] #hago un acumulador para ir sumando los creditos (b)
    aux.push(dat)
while (aux.size() > 0):
    dat = aux.pop()
    cont +=1
    planeta = dat["planeta"]
    print (f"El planeta {planeta} fue visitado en la mision n°{cont}") #reordeno la pila y muestro el numero de mision(a)
    if dat["capturado"] == "Han Solo":
        mis = dat["planeta"]
        print(f"Han Solo fue capturado en el planeta {planeta} en la mision n°{cont}") #muestro en que mision fue capturado Han solo (c)
    pila.push(dat)
print (f"El dinero total recaudado es de {ac} creditos") #finalmente muestro lo creditos totales (b)
