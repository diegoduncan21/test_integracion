import pilas
from escenas.niveles.tutorial import EscenaPrimerDesafio
from bases.menus import MenuDeIconos


class EscenaDeMenu(pilas.escena.Base):

    def __init__(self):
        pilas.escena.Base.__init__(self)

    def iniciar(self):
        pilas.fondos.Selva()
        
        opciones = [
            ('imagenes/menus/principal/jugar.png', self.primer_desafio, 100, 100), 
            ('imagenes/menus/principal/salir.png', self.salir, 600, 200), 
        ]
        
        #self.menu = pilas.actores.Menu(opciones)
        self.menu = MenuDeIconos(opciones)

    def primer_desafio(self):
        pilas.cambiar_escena(EscenaPrimerDesafio())

    def salir(self):
        import sys
        sys.exit(0)
