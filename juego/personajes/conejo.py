import pilas
from ojota import Ojota


class Conejo(pilas.actores.Martian):
    def __init__(self, *args, **kwags):
        pilas.actores.Martian.__init__(self, *args, **kwags)
        self.imagen = pilas.imagenes.cargar_grilla("conejothon.png", 12)
        self.definir_cuadro(0)
        self.municion = Ojota
        self.aprender(pilas.habilidades.Disparar,
                      municion=Ojota,
                      angulo_salida_disparo=-90,
                      frecuencia_de_disparo=8,
                      offset_disparo=(25,0),
                      offset_origen_actor=(25,23))
        self.velocidad = 8
        self.ingrediente = None