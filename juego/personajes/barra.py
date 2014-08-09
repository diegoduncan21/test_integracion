# -*- encoding: utf-8 -*-

import pilas
from pilas.actores import Actor


class Barra(Actor):
    """Muestra una Barra que from pilas.actores import Textose combina (temáticamente) con un actor.
    """

    def __init__(self, x=0, y=0):
        """ Constructor de la Barra.

        :param x: Posición horizontal del Actor.
        :type x: int
        :param y: Posición vertical del Actor.
        :type y: int
        """
        Actor.__init__(self, x=x, y=y)
        self.imagen = pilas.imagenes.cargar_grilla("verduras_2/barreta2.png", 1)
        self.definir_cuadro(0)

    def definir_cuadro(self, indice):
        """ Define el frame de la Barra a mostrar."""
        self.imagen.definir_cuadro(indice)

    def abrir(self):
        """Muestra el gráfico de la Barra abierta con menos cáscara."""
        self.definir_cuadro(1)

    def cerrar(self):
        """Muestra el gráfico de Barra normal (con cáscara)."""
        self.definir_cuadro(0)
