# -*- encoding: utf-8 -*-
# Permite que este ejemplo funcion incluso si no has instalado pilas.
import sys
sys.path.insert(0, "..")
import pilas

from personajes.conejo import Conejo
from personajes.carne import Carne
from personajes.caldera import Caldera
from personajes.barra import Barra


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

        barra = Barra(x=150, y=200)
        barra.aprender(pilas.habilidades.SeMantieneEnPantalla)

        temporizador = pilas.actores.Temporizador(x=0, y=200)
        # ajustamos que despues de 10 segundos llame a funcion_callback
        temporizador.ajustar(10, self.fin_temporizador)
        # iniciamos temporizador
        temporizador.iniciar()

        conejo = Conejo(mapa)
        conejo.aprender(pilas.habilidades.SiempreEnElCentro)

        banana = pilas.actores.Banana(x=-200, y=100)
        self.carne = carne =  Carne(x=200, y=-100)

        self.caldera = caldera = Caldera(x=-200, y=-185)

        # Colisiones
        pilas.escena_actual().colisiones.agregar(conejo, banana, self.llevar)
        pilas.escena_actual().colisiones.agregar(conejo, carne, self.llevar)

        pilas.escena_actual().colisiones.agregar(conejo, caldera, self.dejar)

        pilas.avisar("""Comandos: < ^ > y barra espaciadora""")

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

        # Pinta primer piso
        for columna in range(0, 15):
            mapa.pintar_bloque(6, columna, 1)

        # Pinta todo el suelo
        for columna in range(0, columnas):
            mapa.pintar_bloque(14, columna, 1)

        return mapa

    def llevar(self, conejo, ingrediente):
        if not conejo.ingrediente:
            ingrediente.aprender(pilas.habilidades.Imitar, conejo)
            conejo.ingrediente = ingrediente

    def dejar(self, conejo, caldera):
        if conejo.ingrediente:
            ingrediente = conejo.ingrediente
            ingrediente.eliminar_habilidad(pilas.habilidades.Imitar)
            caldera.ingredientes.append(ingrediente)
            conejo.ingrediente = None
            ingrediente.eliminar()

    def fin_temporizador(self):
		if self.carne in self.caldera.ingredientes:
			pilas.cambiar_escena(EscenaGanador())
		else:
			pilas.cambiar_escena(EscenaPerdedor())
		

class EscenaGanador(pilas.escena.Base):
	def __init__(self):
		pilas.escena.Base.__init__(self)

	def iniciar(self):
		pilas.fondos.Selva()

		opciones = [
			('Genial! Conseguiste todos los ingredientes!\nJuega el siguiente nivel...', self.primer_desafio)
		]

		self.menu = pilas.actores.Menu(opciones)
	def primer_desafio(self):
		pilas.cambiar_escena(EscenaPrimerDesafio())


class EscenaPerdedor(pilas.escena.Base):
	def __init__(self):
		pilas.escena.Base.__init__(self)

	def iniciar(self):
		pilas.fondos.Selva()

		opciones = [('Se termino el tiempo!\nIntentalo de nuevo...', self.primer_desafio)]

		self.menu = pilas.actores.Menu(opciones)
	def primer_desafio(self):
		pilas.cambiar_escena(EscenaPrimerDesafio())
