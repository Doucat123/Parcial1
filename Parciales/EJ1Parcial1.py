#Desarrollar una función recursiva que permita contar cuantas veces aparece una determinada palabra, 
#en un vector de palabras.

palabras = ["hola", "como","hola","estas","hola"]

cont = 0
def contpalabras(vec,pala):
    if len(vec) == 0:  #Si el vector esta vacio retorna cero
        return 0
    elif vec[0] == pala:   #si encuentra una simulitud suma uno y sigue recorriendo
        return 1 + contpalabras(vec[1:], pala) 
    else:
        return contpalabras(vec[1:], pala) #si no encuentra similitud recorre sin sumar

num = contpalabras(palabras,"hola")
print (f"La palabra se encontro {num} veces") #finalmente muestro el numero de veces que se encontro la palabra