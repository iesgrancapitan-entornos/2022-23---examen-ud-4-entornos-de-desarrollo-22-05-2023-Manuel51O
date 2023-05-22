"""
Clase Coche base para el Examen de la UD4
Refactorización
Extrae una superclase Vehículo con los campos
    num_serie
    fabricante
    color
:autor: Manuel Gómez Ruiz
"""


class Vehiculo:
    """
    Clase Vehículo

    :param color: Color
    :param fabricante: Fabricante
    :param num_serie: Número de serie
    """
    color = 'rojo';
    fabricante = 'seat';
    num_serie = 1;


class Coche(Vehiculo):
    """
    Clase Coche

    :param cilindrada: Cilindrada
    """

    cilindrada = 1000;

    def __init__(self):
        pass;

    def __init__(self, num_serie, cilindrada, fabricante, color):
        self.num_serie = num_serie;
        self.cilindrada = cilindrada;
        self.fabricante = fabricante;
        self.color = color;

    @property
    def num_serie(self):
        """
        :return: num_serie
        """
        return self.__num_serie

    @num_serie.setter
    def num_serie(self, value):
        self.__num_serie = value

    @property
    def color(self):
        """
        :return: color
        """
        return self.__color

    @color.setter
    def color(self, value: int):
        self.__color = value

    @property
    def cilindrada(self):
        """
        :return: cilindrada
        """
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, value):
        self.__cilindrada = value

    @property
    def fabricante(self):
        """
        :return: fabricante
        """
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, value):
        self.__fabricante = value
