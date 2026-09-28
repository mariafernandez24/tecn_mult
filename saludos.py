"""Un módulo de ejemplo: un solo fichero .py."""


def saludar(nombre):
    print("Hola,", nombre)


def saludar_a_todos(nombres):
    for n in nombres:
        saludar(n)
