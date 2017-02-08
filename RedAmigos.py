#! python2

# Se esta utilizando un hash bang para que corra en python2
#Tareas de Mapeo
#1.Librerias
#Intertools: This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
#sys: This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

import itertools
import sys

#Maximo 10 personas recomendadas para el ejercicio
#Si se desea modificar cambie el numero de abajo
total_reco = 10


#Funcion para hacer diccionarios realcion
#Diccionario de Usuarios
#Ir agregando Usuario al diccionarios
#Conforme se va agregando se ira diciendo si es amigo
#en caso que no este sera False significara que no sera amigo de este ultimo (llave)
#EstadoRelacion es de tipo binario: 1 son amigos, 0 es que no lo sera
#Importante Recordemos <USER><TAB><FRIEND>
def Diccionario_Rela(User,k1,k2,Relacion):
    if Relacion==1:
        Relacion = True
    else:
        Relacion = False
    #se revisara el k2
    if k1 not in User:
        User[k1] = {}
        User[k1][k2] = [1,False]
    else:
        if k2 in User[k1]:
            User[k1][k2][0] += 1
        else:
            User[k1][k2] = [1,False]
    # se revisara el k2
    if Relacion==True:
        User[k1][k2][0] -= 1
        User[k1][k2][1] = True



# Input ingresara de la forma STDIN
# Ejemplo
#$ input | programa2 | programa3
#word Count
User = {}
# 5. Ejemplo de Split
# In[2]: x = "something \t like     \t this"
# In[4]: x.split('\t')
# Out[4]: ['something ', ' like     ', ' this']
# <User><TAB><Friends> = [User Friend1 Friend2 Friend3 ...]

# sys para input STDIN

for Usuario in sys.stdin:
    Usuario = Usuario.strip()
    Usuario = Usuario.split("\t")

    #llave sera la tupla 1

    key = tuple(map(int,Usuario[0].strip().split(",")))
    #relacion que tienen
    Relacion = int(Usuario[1])
    #k1 y k2 igual a la llave
    # Cumpliendo con la forma algoritmoo
    #Map(k1,v1) list(k2,v2)
    k1,k2 = key
    Diccionario_Rela(User,k1,k2,Relacion)
    Diccionario_Rela(User,k2,k1,Relacion)

#Lista de recomendaciones
#Agregara
for k1 in User.keys():
    #lista de recomendaciones
    #Ira agregando a la lista las recomendaciones solo cuando el tipo de relacion = a 0 de no se asi
    #no los agregara
    # esto hasta llegar a 10
    # el numero de recomendaciones puede cambiar arriba
    Recomendacion = []
    for k2 in User[k1].keys():
        #Son o no amigos
        n,Amistad = User[k1][k2]
        if Amistad==False:
            Recomendacion.append((k2,n))
    #Ordenadas de orden ascendentes
    #Puede alterar el orde cambiando el valor del reverse
    Recomendacion = sorted(Recomendacion,key=lambda x: x[0])
    Recomendacion = sorted(Recomendacion,key=lambda x: x[1],reverse=True)
    #en caso que sea mas de 0 se imprimira la recomendaciones
    #de no ser asi no se imprimira nada, por lo que pueden haber usuarios que no aparezcan
    #casos como el del usuario 49,999
    if len(Recomendacion)>0:
        Recomendacion = list(map(str,zip(*Recomendacion)[0]))
        print k1,"\t",','.join(Recomendacion[:total_reco])