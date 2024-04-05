from inter_grafica import *
from ahorcado import *
from letra import comprobar_letra

def main():
    """..."""

    game.resize(ANCHO_VENTANA, ALTO_VENTANA)
    palabra = elegir_palabra()
    juego = crear_juego(palabra)
    mensaje = None

    while not terminar_partida(juego["FALLOS"], juego["PALABRA_OCULTA"]):
        game.draw_begin()
        definir_titulo_ventana()
        graficar_palabra_oculta(juego["PALABRA_OCULTA"])
        graficar_mensaje(mensaje)
        graficar_letras_usadas(juego["LETRAS_USADAS"])
        dibujar_horca()
        dibujar_persona(juego["FALLOS"])
        game.draw_end()

        event = game.wait(game.EventType.KeyPress)
        letra = event.key.upper()
        mensaje = comprobar_letra(letra, juego)

    game.draw_begin()
    dibujar_horca()
    dibujar_persona(juego["FALLOS"])
    graficar_mensaje_final(perder_partida(juego["FALLOS"]), palabra)
    graficar_boton_volver_a_jugar()
    game.draw_end()

    event = game.wait(game.EventType.ButtonPress)
    if event.x in range(int(ANCHO_BOTON[0]), int(ANCHO_BOTON[1]) + 1) and event.y in range(ALTO_BOTON[0], ALTO_BOTON[1] + 1):
        main()

game.init(main)