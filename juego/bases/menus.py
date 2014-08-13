import pilas
import pdb;
class MenuDeIconos(pilas.actores.Menu):
	
	def __init__(self, opciones, x=0, y=0, fuente=None,
					color_normal=pilas.colores.gris,
					color_resaltado=pilas.colores.blanco):
						
		op = [(icono[0], "", [icono[1]]) for icono in opciones]
		pilas.actores.Menu.__init__(self, op, x=x, y=y, fuente=fuente,
					color_normal=color_normal, color_resaltado=color_resaltado)
		
		print self.opciones_como_actores
		
		for opcion, icono in zip(opciones, self.opciones_como_actores):
			if len(opcion) >= 3:
				icono.derecha -= opcion[2]
			if len(opcion) == 4:
				icono.arriba -= opcion[3]
