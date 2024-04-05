from random import choice
from resources.palabras import *
LETRA_OCULTA = "_"

def crear_juego(palabra_elegida):
    """..."""

    return {
        "PALABRA": palabra_elegida,
        "PALABRA_OCULTA": ocultar_palabra(palabra_elegida),
        "FALLOS": 0,
        "LETRAS_USADAS": [],
    }

def ocultar_palabra(palabra):
    """
    Oculta la palabra cambiando sus  letras por *.
    """
    
    return [LETRA_OCULTA for _ in range(len(palabra))]

def elegir_palabra():
    """
    Elige una palabra al azar de una lista de palabras y la devuelve.
    """

    return cambiar_letras(choice(PALABRAS)).upper()

def cambiar_letras(palabra):
    """
    Recibe una palabra y le quita los acentos, dieresis y la ñ.
    """

    letras_especiales = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u", "ü":"u", "ñ":"n"}
    for letra, letra_cambiada in letras_especiales.items():
        palabra = palabra.replace(letra, letra_cambiada)

    return palabra

def ganar_partida(palabra_oculta):
    """
    -Recibe: la palabra oculta
    -Devuelve: True si ya no hay letras ocultas en la palabra oculta o False en caso contrario
    """

    return not LETRA_OCULTA in palabra_oculta

def perder_partida(fallos):
    """
    -Recibe: la cantidad de fallos
    -Devuelve: True si fallos == 7 o False en caso contrario
    """

    return fallos == 7

def terminar_partida(fallos, palabra_oculta):
    """
    -Recibe: la cantidad de fallos y la palabra oculta
    -Termina la partida si se cumple la función de perder o la de ganar
    """

    return ganar_partida(palabra_oculta) or perder_partida(fallos)