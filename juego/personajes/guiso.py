# -*- encoding: utf-8 -*-

import pilas
from pilas.actores import Actor


class Guiso(Actor):

    def __init__(self, x=0, y=0):
        """ Constructor de la guiso.

        :param x: Posición horizontal del Actor.
        :type x: int
        :param y: Posición vertical del Actor.
        :type y: int
        """
        Actor.__init__(self, x=x, y=y)
        self.imagen = pilas.imagenes.cargar_grilla(
            "imagenes/personajes/guiso.png", 1)
        self.definir_cuadro(0)
        self.radio_de_colision = 30
        self.ingredientes = []

    def definir_cuadro(self, indice):
        """ Define el frame de la guiso a mostrar."""
        self.imagen.definir_cuadro(indice)

    def abrir(self):
        """Muestra el gráfico de la guiso abierta con menos cáscara."""
        self.definir_cuadro(1)

    def cerrar(self):
        """Muestra el gráfico de guiso normal (con cáscara)."""
        self.definir_cuadro(0)
