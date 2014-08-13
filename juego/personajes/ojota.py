# -*- encoding: utf-8 -*-
import pilas
from pilas.actores import Actor


class Ojota(Actor):
    def __init__(self, x=0, y=0, rotacion=0, velocidad_maxima=6,
                 angulo_de_movimiento=90):

        """
        Construye la Ojota.

        :param x: Posición x del proyectil.
        :param y: Posición y del proyectil.
        :param rotacion: Angulo de rotación del Actor.
        :param velocidad_maxima: Velocidad máxima que alcanzará el proyectil.
        :param angulo_de_movimiento: Angulo en que se moverá el Actor..

        """
        imagen = pilas.imagenes.cargar('imagenes/proyectiles/chancleta.png')
        Actor.__init__(self, imagen)
        self.x = x
        self.y = y
        self.rotacion = rotacion
        self.escala = 2
        self.radio_de_colision = 20

        self.hacer(pilas.comportamientos.Proyectil(velocidad_maxima=velocidad_maxima,
                                                   aceleracion=1,
                                                   angulo_de_movimiento=angulo_de_movimiento,
                                                   gravedad=0))

    def actualizar(self):
        self.rotacion += 13
