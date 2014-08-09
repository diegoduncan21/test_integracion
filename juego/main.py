# -*- encoding: utf-8 -*-
# Permite que este ejemplo funcion incluso si no has instalado pilas.
import sys
sys.path.insert(0, "..")
import pilas

# Personajes


class Conejo(pilas.actores.Martian):
    def __init__(self, *args, **kwags):
        pilas.actores.Martian.__init__(self, *args, **kwags)
        self.imagen = pilas.imagenes.cargar_grilla("conejothon.png", 1)


# Mapa


def crear_mapa(filas=15, columnas=20):
    mapa = pilas.actores.Mapa(filas=filas, columnas=columnas)

    # Plataforma superior (la que esta en medio de la pantalla)
    # mapa.pintar_bloque(4, 6, 0)
    # mapa.pintar_bloque(5, 7, 1)
    # mapa.pintar_bloque(6, 8, 1)
    # mapa.pintar_bloque(7, 9, 1)
    # mapa.pintar_bloque(8, 10, 1)
    # mapa.pintar_bloque(9, 11, 1)
    # mapa.pintar_bloque(10, 12, 2)

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

    mapa.pintar_bloque(13, 0, 7, True)
    mapa.pintar_bloque(12, 0, 7, True)
    mapa.pintar_bloque(11, 0, 7, True)
    mapa.pintar_bloque(10, 0, 7, True)

    mapa.pintar_bloque(13, 19, 7, True)
    mapa.pintar_bloque(12, 19, 7, True)
    mapa.pintar_bloque(11, 19, 7, True)
    mapa.pintar_bloque(10, 19, 7, True)

    # Pinta todo el suelo
    for columna in range(0, 15):
        mapa.pintar_bloque(6, columna, 1)

    # Pinta todo el suelo
    for columna in range(0, columnas):
        mapa.pintar_bloque(14, columna, 1)

    return mapa

pilas.iniciar()

pilas.fondos.DesplazamientoHorizontal()

mapa = crear_mapa()
martian = Conejo(mapa)
martian.aprender(pilas.habilidades.SiempreEnElCentro)

pilas.avisar("Usa los direccionales para controlar al personaje.")
pilas.ejecutar()

pilas.ejecutar()
