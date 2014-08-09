# -*- encoding: utf-8 -*-
# Permite que este ejemplo funcion incluso si no has instalado pilas.
import sys
sys.path.insert(0, "..")
import pilas

from personajes.conejo import Conejo

class EscenaNivelTurorial(pilas.escena.Base):

	def __init__(self):
		pilas.escena.Base.__init__(self)

	def iniciar(self):
		
		pilas.fondos.DesplazamientoHorizontal()

		mapa = self.crear_mapa()
		conejo = Conejo(mapa)
		conejo.aprender(pilas.habilidades.SiempreEnElCentro)

		pilas.avisar("Usa los direccionales para controlar al personaje.")

	def crear_mapa(self, filas=15, columnas=20):
		mapa = pilas.actores.Mapa(filas=filas, columnas=columnas)
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
