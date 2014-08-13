#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pilas
pilas.iniciar()

from escenas.presentacion import EscenaDeMenu


def main():

    # Carga la nueva escena
    pilas.cambiar_escena(EscenaDeMenu())
    pilas.ejecutar()

    return 0

if __name__ == '__main__':
    main()
