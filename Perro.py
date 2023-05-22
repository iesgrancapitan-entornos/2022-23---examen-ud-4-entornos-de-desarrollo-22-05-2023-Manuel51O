"""
Clase Perro.

Autor: Jaime Rabasco Ronda.
"""
class Perro:

    def __init__(self):
        self.__ladra = 'Guau'

    def ladrar(self):
        print('Guau');

p = Perro();
p.ladrar();
