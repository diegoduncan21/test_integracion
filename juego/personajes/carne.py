# -*- encoding: utf-8 -*-

import pilas
from pilas.actores import Actor


class Carne(Actor):
    """Muestra una carne que se combina (temáticamente) con un actor.

    .. image:: verduras/carne.png

    """

    def __init__(self, x=0, y=0):
        """ Constructor de la carne.

        :param x: Posición horizontal del Actor.
        :type x: int
        :param y: Posición vertical del Actor.
        :type y: int
        """
        Actor.__init__(self, x=x, y=y)
        self.imagen = pilas.imagenes.cargar_grilla("verduras/carne.png", 1)
        self.definir_cuadro(0)
        self.radio_de_colision = 30

    def definir_cuadro(self, indice):
        """ Define el frame de la carne a mostrar."""
        self.imagen.definir_cuadro(indice)

    def abrir(self):
        """Muestra el gráfico de la carne abierta con menos cáscara."""
        self.definir_cuadro(1)

    def cerrar(self):
        """Muestra el gráfico de carne normal (con cáscara)."""
        self.definir_cuadro(0)
