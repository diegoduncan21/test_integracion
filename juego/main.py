# -*- encoding: utf-8 -*-
# Permite que este ejemplo funcion incluso si no has instalado pilas.
import sys
sys.path.insert(0, "..")
import pilas

from pilas.actores import Actor

# Objectos


class Ojota(Actor):
    def __init__(self,x=0,y=0,rotacion=0,velocidad_maxima=6,
                 angulo_de_movimiento=90):

        """
        Construye la Ojota.

        :param x: Posición x del proyectil.
        :param y: Posición y del proyectil.
        :param rotacion: Angulo de rotación del Actor.
        :param velocidad_maxima: Velocidad máxima que alcanzará el proyectil.
        :param angulo_de_movimiento: Angulo en que se moverá el Actor..

        """
        imagen = pilas.imagenes.cargar('chancleta.png')
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



# Personajes


class Conejo(pilas.actores.Martian):
    def __init__(self, *args, **kwags):
        pilas.actores.Martian.__init__(self, *args, **kwags)
        self.imagen = pilas.imagenes.cargar_grilla("conejothon.png", 12)
        self.definir_cuadro(0)
        self.mapa = mapa
        self.municion = Ojota
        self.aprender(pilas.habilidades.Disparar,
                      municion=Ojota,
                      angulo_salida_disparo=-90,
                      frecuencia_de_disparo=8,
                      offset_disparo=(25,0),
                      offset_origen_actor=(25,23))
        self.velocidad = 8



# Mapa


def crear_mapa(filas=15, columnas=20):
    mapa = pilas.actores.Mapa(filas=filas, columnas=columnas)

    # Plataforma pequeña, mas abajo que la anterior.
    mapa.pintar_bloque(12, 12, 0)
    mapa.pintar_bloque(12, 13, 1)
    mapa.pintar_bloque(12, 14, 1)
    mapa.pintar_bloque(12, 15, 2)

    mapa.pintar_bloque(13, 12, 8, False)
    mapa.pintar_bloque(13, 13, 9, False)
    mapa.pintar_bloque(13, 14, 9, False)
    mapa.pintar_bloque(13, 15, 10, False)

    # bloque derecha
    mapa.pintar_bloque(9, 18, 2)

    # topes
    for tope in range(15):
        # izq
        mapa.pintar_bloque(tope, 0, 7, True)
        # der
        mapa.pintar_bloque(tope, 19, 7, True)

    # Pinta todo el suelo
    for columna in range(0, 15):
        mapa.pintar_bloque(6, columna, 1)

    # Pinta todo el suelo
    for columna in range(0, columnas):
        mapa.pintar_bloque(14, columna, 1)

    return mapa

def llevar(conejo, banana):
    banana.aprender(pilas.habilidades.Imitar, conejo)

pilas.iniciar(usar_motor='qtgl')

fondo = pilas.fondos.DesplazamientoHorizontal()

fondo.agregar("selva.jpg")

mapa = crear_mapa()
conejo = Conejo(mapa)
conejo.aprender(pilas.habilidades.SiempreEnElCentro)

banana1 = pilas.actores.Banana(x=-200, y=100)

bananas = [banana1]

pilas.escena_actual().colisiones.agregar(conejo, bananas, llevar)

pilas.avisar("Usa los direccionales para controlar al personaje.")
# pilas.avisar("Usa espacio para tirar una ojota.")

pilas.ejecutar()
