#Dada una lista con nombres de personajes de la saga de Avengers ordenados por nombre del superhéroes,
# de los cuales se conoce:
#nombre del superhéroe, nombre del personaje (puede ser vacio), grupo al que (puede ser vacio),
# año de aparición, por ejemplo (Star Lord – Peter Quill – Guardianes de la galaxia - 1976).
#Resolver las siguientes tareas:
#a. Determinar si “Capitana Marvel” está en la lista y mostrar su nombre de personaje;
#b. Almacenar los superhéroes que pertenezcan al grupo “Guardianes de la galaxia” en una cola e 
# indicar cuantos son.
#c. Mostrar de manera descendente los superhéroes que pertenecen al grupo “Los cuatro fantásticos” y 
# “Guardianes de la galaxia”.
#d. Listar los superhéroes que tengan nombre de personajes cuyo año de aparición sea posterior a 1960.
#e. Hemos detectado que la superhéroe “Black Widow” está mal cargada por un error de tipeo, figura como
# “Vlanck Widow”, modifique dicho superhéroe para solucionar este problema.
#f. Dada una lista auxiliar con los siguientes personajes 
# (‘Black Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la información), 
# agregarlos a la lista principal en el caso de no estar cargados.
#g. Mostrar todos los personajes que comienzan con C, P o S.
#h. Cargue al menos 20 superheroes a la lista.
from clases import Lista
from clases import Cola

class Personaje:
    def __init__(self, nombreSH, nombrePER, grupo, año):
        self.nombreSH = nombreSH
        self.nombrePER = nombrePER
        self.grupo = grupo
        self.año = año
    
    def __str__(self):
        return f'{self.nombreSH} - {self.nombrePER} - {self.grupo} - {self.año}'

P1 = Personaje("Capitana Marvel","Carol Danvers",None,1968)
P2 = Personaje("Thor",None,"Vengadores",1962)
P3 = Personaje("Hulk","Bruce Banner","Vengadores",1962)
P4 = Personaje("Loki", None, None, 1962)
P5 = Personaje("Sr. Fantástico","Reed Richards","Los cuatro Fantasticos", 1961)
P6 = Personaje("Gamora", None,"Guardianes de la galaxia", 1975)
P7 = Personaje("Antorcha Humana","Jonathan Storm","Los cuatro Fantasticos", 1961)
P8 = Personaje("Vlanck Widow","Natalia Alianovna Romanova","Vengadores", 1964)
P9 = Personaje("Mole","Benjamin Grimm","Los cuatro Fantasticos", 1961)
P10 = Personaje("Ant-Man ","Henry Pym", None, 1962)
P11 = Personaje("Black Panther","T'Challa","Vengadores", 1966)
P12 = Personaje("Iron Man","Anthony Stark","Vengadores", 1963)
P13 = Personaje("Star Lord","Peter Quill","Guardianes de la galaxia", 1976)
P14 = Personaje("Namor",None,None, 1939)
P15 = Personaje("Ángel","Warren Kenneth","X-Men", 1963)
P16 = Personaje("Cíclope","Mace Windu","X-Men", 1963)
P17= Personaje("Iceman","Robert Louis","X-Men", 1963)
P18 = Personaje("Bestia","Hank McCoy'","X-Men", 1963)
P19 = Personaje("Spider-Man","Peter Parker",None, 1962)
P20 = Personaje("The Punisher","Frank Castle",None, 1974)
print()
lista = Lista()

lista.insert(P1, "nombreSH")
lista.insert(P2, "nombreSH")
lista.insert(P3, "nombreSH")
lista.insert(P4, "nombreSH")
lista.insert(P5, "nombreSH")
lista.insert(P6, "nombreSH")
lista.insert(P7, "nombreSH")
lista.insert(P8, "nombreSH")
lista.insert(P9, "nombreSH")
lista.insert(P10, "nombreSH")
lista.insert(P11, "nombreSH")
lista.insert(P12, "nombreSH")
lista.insert(P13, "nombreSH")
lista.insert(P14, "nombreSH")
lista.insert(P15, "nombreSH")
lista.insert(P16, "nombreSH")
lista.insert(P17, "nombreSH")
lista.insert(P18, "nombreSH")
lista.insert(P19, "nombreSH")
lista.insert(P20, "nombreSH")

lista.barrido()
print()

#a)
print("a)")
capitana = lista.search("Capitana Marvel", "nombreSH")
if capitana != None:
    print ("El nombre del personaje de capitana marvel es: ", lista.get_element_by_index(capitana).nombrePER)
print()

#b)
print ("b)")
cola_guar = Cola()
for i in range(lista.size()):
    if lista.get_element_by_index(i).grupo == "Guardianes de la galaxia":
        guardian = lista.get_element_by_index(i).nombreSH
        cola_guar.arrive(guardian)
numG = cola_guar.size()
print (f"El numero de personajes de Los Guardianes de la galaxia es {numG}")
print()

#c)
print ("c)")
list_GD = Lista()
list_CD = Lista()
for i in range(lista.size()):
    if lista.get_element_by_index(i).grupo == "Guardianes de la galaxia":
        personajeGG = lista.get_element_by_index(i)
        list_GD.insert(personajeGG,"nombreSH")
    if lista.get_element_by_index(i).grupo == "Los cuatro Fantasticos":
        personajeL4 = lista.get_element_by_index(i)
        list_CD.insert(personajeL4,"nombreSH")
list_GD.order_by("nombreSH",reverse=True)
list_CD.order_by("nombreSH",reverse=True)
print("Guardianes de la galaxia de forma descendente:")
list_GD.barrido()
print()

print("Los 4 fantasticos de forma descendente:")
list_CD.barrido()
print()

#d)
print ("d)")
list_pos1960 = Lista()
for i in range(lista.size()):
    if lista.get_element_by_index(i).año > 1960 and lista.get_element_by_index(i).nombrePER != None:
        post1960= lista.get_element_by_index(i)
        list_pos1960.insert(post1960,"nombreSH")
print("Lista de superheroes con nombre de personaje y posteriores a 1960:")
list_pos1960.barrido()
print()

#e)
print ("e)")
black = lista.search("Vlanck Widow", "nombreSH")
if lista.get_element_by_index(black).nombreSH != "Black Widow":
    lista.get_element_by_index(black).nombreSH = "Black Widow"
print("Lista con el nombre Black Widow arreglado:")
lista.barrido()
print()

#f)
print ("f)")
PA = Personaje("Loki", None, None, 1962)
PB= Personaje("Black Cat", "Felicia Hardy", "Héroes de Alquiler",1979)
PC = Personaje("Rocket Racoonn", None, None, 1982)
PD = Personaje("Hulk", "Bruce Banner", "Vengadores",1962)

lista_aux = Lista()

lista_aux.insert(PA, 'nombreSH')
lista_aux.insert(PB, 'nombreSH')
lista_aux.insert(PC, 'nombreSH')
lista_aux.insert(PD, 'nombreSH')
lista_aux.barrido()
print()

for i in range(lista_aux.size()):
    name = str(lista_aux.get_element_by_index(i).nombreSH)
    index = lista.search(lista_aux.get_element_by_index(i).nombreSH,'nombreSH')
    if index == None:
        element = lista_aux.get_element_by_index(i)
        lista.insert(element,'nombreSH')
print("Lista con los nuevos superheroes agregados, sin repetir a Hulk y Loki:")
lista.barrido()
print()

#g)
print("g)")
for i in range(lista.size()):
    if lista.get_element_by_index(i).nombreSH.startswith("C"):
        startc = lista.get_element_by_index(i)
        print ("Este Superheroe empieza con C:")
        print (startc)
        print()
    if lista.get_element_by_index(i).nombreSH.startswith("P"):
        startP = lista.get_element_by_index(i)
        print ("Este Superheroe empieza con P:")
        print (startP)
        print()
    if lista.get_element_by_index(i).nombreSH.startswith("S"):
        startS = lista.get_element_by_index(i)
        print ("Este Superheroe empieza con S:")
        print (startS)
        print()

