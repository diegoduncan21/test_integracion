# -*- encoding: utf-8 -*-

import pilas
from pilas.actores import Actor


class Caldera(Actor):
    """Muestra una carldera que se combina (temáticamente) con un actor.

    .. image:: verduras/carldera.png

    """

    def __init__(self, x=0, y=0):
        """ Constructor de la carldera.

        :param x: Posición horizontal del Actor.
        :type x: int
        :param y: Posición vertical del Actor.
        :type y: int
        """
        Actor.__init__(self, x=x, y=y)
        self.imagen = pilas.imagenes.cargar_grilla("caldera.png", 1)
        self.definir_cuadro(0)
        self.radio_de_colision = 30
        self.ingredientes = []

    def definir_cuadro(self, indice):
        """ Define el frame de la carldera a mostrar."""
        self.imagen.definir_cuadro(indice)

    def abrir(self):
        """Muestra el gráfico de la carldera abierta con menos cáscara."""
        self.definir_cuadro(1)

    def cerrar(self):
        """Muestra el gráfico de carldera normal (con cáscara)."""
        self.definir_cuadro(0)
