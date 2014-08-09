# -*- encoding: utf-8 -*-
# Permite que este ejemplo funcion incluso si no has instalado pilas.
import sys
sys.path.insert(0, "..")
import pilas

from personajes.conejo import Conejo

class EscenaPrimerDesafio(pilas.escena.Base):
	def __init__(self):
		pilas.escena.Base.__init__(self)

	def iniciar(self):
		pilas.fondos.Selva()

		opciones = [('Comenzar a jugar', self.primer_desafio)]

		self.menu = pilas.actores.Menu(opciones)
	def primer_desafio(self):
		pilas.cambiar_escena(EscenaNivelTurorial())

class EscenaNivelTurorial(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        
        fondo = pilas.fondos.DesplazamientoHorizontal()

        fondo.agregar("selva.jpg")

        mapa = self.crear_mapa()
        conejo = Conejo(mapa)
        conejo.aprender(pilas.habilidades.SiempreEnElCentro)

        banana1 = pilas.actores.Banana(x=-200, y=100)

        bananas = [banana1]

        pilas.escena_actual().colisiones.agregar(conejo, bananas, self.llevar)

        pilas.avisar("""Usa los direccionales para controlar al personaje.
		Presiona la barra espaciadora para arojar ojotas y eliminar obstaculos""")

    def crear_mapa(self, filas=15, columnas=20):
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

    def llevar(self, conejo, banana):
        banana.aprender(pilas.habilidades.Imitar, conejo)
