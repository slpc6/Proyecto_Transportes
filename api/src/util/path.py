"""Modulo para manejar las rutas de la aplicacion"""

import os


class Path:
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ROUTERS = os.path.join(ROOT, "router")
    MODELS = os.path.join(ROOT, "model")
    UTIL = os.path.join(ROOT, "util")
    INPUT = os.path.join(ROOT, "input")
    OUTPUT = os.path.join(ROOT, "output")
