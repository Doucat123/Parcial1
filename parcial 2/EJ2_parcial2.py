#Dado un grafo no dirigido con los personajes de star wars implementar los algoritmos necesarios para resolver las siguientes tareas:
#a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos 
#ambos personajes que se relacionan;
#b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
#c) determinar cuál es el número máximo de episodio que comparten dos personajes,

from grafo import Grafo

star = Grafo(dirigido=False)

lista_personajes = ['luke','yoda','leia','axel','emperador']

for ambiente in lista_personajes:
    star.insert_vertice(ambiente)

#A)
star.insert_arist('luke', 'leia', 4)
star.insert_arist('yoda', 'axel', 6)
star.insert_arist('leia', 'yoda', 8)
star.insert_arist('axel', 'luke', 3)
star.insert_arist('emperador', 'luke', 6)
star.insert_arist('leia', 'axel', 5)
star.insert_arist('axel', 'emperador', 7)
star.insert_arist('yoda', 'emperador', 1)
star.insert_arist('leia', 'emperador', 1)

star.barrido()

#B)
print ('B)')
star_minima = star.kruskal()
print (star_minima)
print()
yoda_presente = False
for conexion in star_minima:
    joda = conexion
    if 'yoda' in (joda):
        yoda_presente = True
        break

if yoda_presente:
    print(f"Yoda está presente en el árbol de expansión mínima.")
else:
    print(f"Yoda no está presente en el árbol de expansión mínima.")
print()

#C)
print ('C)')
star.barrido_mayor()