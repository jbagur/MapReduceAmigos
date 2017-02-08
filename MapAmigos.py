#! python2
# Se esta utilizando un hash bang para que corra en python2

# Tareas de Mapeo
# 1.Librerias
# Intertools: This module implements a number of iterator building blocks inspired by constructs from APL, Haskell, and SML. Each has been recast in a form suitable for Python.
# sys: This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

import itertools
import sys

# Input ingresara de la forma STDIN
# $ input | programa2 | programa3
# word Count

for Usuario in sys.stdin:

    # 2.Quitar los espacios en blanco,separar por filas
    # 3.Spriping/Spliting
    # 4.La funcion "strip()" retorna una copia de una cadena con ciertos caracteres eliminados de su principio y final.

    Usuario = Usuario.strip()
    Usuario = Usuario.split("\t")

    # 5. Ejemplo de Split
    # In[2]: x = "something \t like     \t this"
    # In[4]: x.split('\t')
    # Out[4]: ['something ', ' like     ', ' this']
    # <User><TAB><Amigo> = [User Friend1 Friend2 Friend3 ...]
    # Mapping
    # LLave sera el User

    llave = int(Usuario[0])

    # Aplicara cuando el usuario tenga almenos un amigo.
    # Map(k1,v1) -> list(k2,v2)
    # listas y tuplas

    if len(Usuario) > 1:
        Amigo = Usuario[1]
        if Amigo != '':
            Amigo = Usuario[1].split(",")
            Amigo = sorted(map(int, Amigo))

            # Crear Tuplas

            for friend in Amigo:
                tupla_amigos = tuple(sorted([llave, friend]))
                tupla_amigos = ','.join(map(str, tupla_amigos))
                print tupla_amigos, "\t", 1
            for tupla_amigos in itertools.combinations(Amigo, 2):
                tupla_amigos = ','.join(map(str, tupla_amigos))
                print tupla_amigos, "\t", 0
