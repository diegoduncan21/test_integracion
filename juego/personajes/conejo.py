import pilas

class Conejo(pilas.actores.Martian):
	def __init__(self, *args, **kwags):
		pilas.actores.Martian.__init__(self, *args, **kwags)
		self.imagen = pilas.imagenes.cargar_grilla("imagenes/conejothon.png", 12)
