"""
Clase Perro.

Autor: Manuel Gómez Ruiz
"""
class Perro:

    def __init__(self):
        """
        Constructor init dog.
        """
        self.__ladra = 'Guau'

    def ladrar(self):
        print('Guau');

p = Perro();
p.ladrar();
