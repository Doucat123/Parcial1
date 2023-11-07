#Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada de los cuales se conoce su nombre, número, 
#tipo/tipos para el cual debemos construir tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
#a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
#b) mostrar todos los datos de un Pokémon a partir de su número y nombre para este último, la búsqueda debe ser por proximidad, es decir si busco 
# “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
#c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
#d) realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
#e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
#f) Determina cuantos Pokémons hay de tipo eléctrico y acero.
from BinaryTree import BinaryTree

Pokemon_name_tree = BinaryTree()
Pokemon_num_tree = BinaryTree()
Pokemon_type_tree = BinaryTree()


lista_pokemon = [
    {'pokemon': 'Ceto', 'numero': 444, 'tipo': 'fuego'},
    {'pokemon': 'Tifón', 'numero': 43, 'tipo': 'agua'},
    {'pokemon': 'Equidna', 'numero': 5, 'tipo': 'agua'},
    {'pokemon': 'Dino', 'numero': 345, 'tipo': 'planta'},
    {'pokemon': 'Pefredo', 'numero': 123, 'tipo': 'planta'},
    {'pokemon': 'Enio', 'numero': 146, 'tipo': 'fuego'},
    {'pokemon': 'Jolteon', 'numero': 356, 'tipo': 'acero'},
    {'pokemon': 'Caribdis', 'numero': 33, 'tipo': 'electrico'},
    {'pokemon': 'Euríale', 'numero': 98, 'tipo': 'electrico'},
    {'pokemon': 'Esteno', 'numero': 67, 'tipo': 'agua'},
    {'pokemon': 'Medusa', 'numero': 12, 'tipo': 'electrico'},
    {'pokemon': 'Ladón', 'numero': 21, 'tipo': 'electrico'},
    {'pokemon': 'Lycanroc', 'numero':66, 'tipo': 'electrico'},
    {'pokemon': 'Quimera', 'numero': 56, 'tipo': 'fuego'},
    {'pokemon': 'Hidra de Lerna', 'numero': 789, 'tipo': 'fuego'},
    {'pokemon': 'León de Nemea', 'numero': 543, 'tipo': 'acero'},
    {'pokemon': 'Esfinge', 'numero': 45, 'tipo': 'fuego'},
    {'pokemon': 'Dragón de la Cólquida', 'numero': 678, 'tipo': 'agua'},
    {'pokemon': 'Cerbero', 'numero': 567, 'tipo': 'agua'},
    {'pokemon': 'Tyrantrum', 'numero': 934, 'tipo': 'acero'},
    {'pokemon': 'Ortro', 'numero': 245, 'tipo': 'planta'},
]

for pokemon in lista_pokemon:
    Pokemon_name_tree.insert_node(pokemon['pokemon'], pokemon)
    Pokemon_num_tree.insert_node(pokemon['numero'], pokemon)
    Pokemon_type_tree.insert_node(pokemon['tipo'], pokemon)

#A
print('A)')
print('Por nombre:')
Pokemon_name_tree.inorden()
print()
print('Por numero:')
Pokemon_num_tree.inorden()
print()
print('Por tipo:')
Pokemon_type_tree.inorden()
print()

#B
print('B)')
Pokemon_num_tree.inorden()
num = input('Que numero desea buscar:')
n = int(num)
pos = Pokemon_num_tree.search(n)
if pos is not None:
    print (f'La informacion del numero {n} es: {pos.other_values}')
print()
con = input('Ingrese nombre, o parte del nombre del pokemon que desea buscar:')
print (f'Resultados de ({con})')
Pokemon_name_tree.search_by_coincidence_pokemon(con)
print()

#C
print('C)')
tipo = input("Ingrese el tipo de pokemon: ")
Pokemon_type_tree.inorden_pokemon(tipo)
print()

#D
print('D)')
print('Listado ordenado de manera ascendente por numero:')
Pokemon_num_tree.inorden_pokemon2()
print()
print('Listado ordenado de manera ascendente por nombre:')
Pokemon_name_tree.inorden_pokemon2()
print()
print('Listado ordenado de manera ascendente por nivel por nombre:')
Pokemon_name_tree.by_level()
print()

#E
print('E)')
Jolteon = Pokemon_name_tree.search('Jolteon')
Lycanroc = Pokemon_name_tree.search('Lycanroc')
Tyrantrum = Pokemon_name_tree.search('Tyrantrum')

if Jolteon is not None:
    print (f'Los datos de Jolteon son:{Jolteon.other_values}')

if Lycanroc is not None:
    print (f'Los datos de Lycanroc son:{Lycanroc.other_values}')

if Tyrantrum is not None:
    print (f'Los datos de Tyrantrum son:{Tyrantrum.other_values}')
print()

#F
print('F)')
num1 = Pokemon_type_tree.contar('electrico')
num2 = Pokemon_type_tree.contar('acero')
print (f'Hay un total de {num1} pokemones electricos y {num2} pokemones de tipo acero')