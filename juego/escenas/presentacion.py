import pilas
from escenas.niveles.tutorial import EscenaPrimerDesafio
class EscenaDeMenu(pilas.escena.Base):

	def __init__(self):
		pilas.escena.Base.__init__(self)

	def iniciar(self):
		pilas.fondos.Selva()

		opciones = [
			('Jugar', self.primer_desafio),
			('Salir', self.salir)]

		self.menu = pilas.actores.Menu(opciones)
	
	def primer_desafio(self):
		pilas.cambiar_escena(EscenaPrimerDesafio())

	def salir(self):
		import sys
		sys.exit(0)
