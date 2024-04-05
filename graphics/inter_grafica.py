import graphics.gamelib as game

ALTO_VENTANA, ANCHO_VENTANA = (500, 500)
MARGEN_X, MARGEN_Y = (40, 40)
ANCHO_BOTON, ALTO_BOTON = ((ANCHO_VENTANA * 1/4, ANCHO_VENTANA * 3/4), (400, 450))
PARTES_PERSONA = {
    "CABEZA":(ANCHO_VENTANA / 2 - 10, MARGEN_Y * 5, ANCHO_VENTANA / 2 + 10, MARGEN_Y * 5 + 20),
    "CUERPO":(ANCHO_VENTANA / 2, MARGEN_Y * 5 + 20, ANCHO_VENTANA / 2, MARGEN_Y * 6.5),
    "BRAZO_DERECHO":(ANCHO_VENTANA / 2, MARGEN_Y * 5 + 20, ANCHO_VENTANA / 2 + 20, MARGEN_Y * 5 + 40),
    "BRAZO_IZQUIERDO":(ANCHO_VENTANA / 2, MARGEN_Y * 5 + 20, ANCHO_VENTANA / 2 - 20, MARGEN_Y * 5 + 40),
    "PIERNA_DERECHA":(ANCHO_VENTANA / 2, MARGEN_Y * 6.5, ANCHO_VENTANA / 2 + 20, MARGEN_Y * 6.5 + 30),
    "PIERNA_IZQUIERDA":(ANCHO_VENTANA / 2, MARGEN_Y * 6.5, ANCHO_VENTANA / 2 - 20, MARGEN_Y * 6.5 + 30),
    "AHORCADO":(ANCHO_VENTANA / 2 - 10, MARGEN_Y * 5 + 20, ANCHO_VENTANA / 2 + 10, MARGEN_Y * 5 + 20)
    }


def definir_titulo_ventana():
    """..."""

    game.title("AHORCADO")

def graficar_palabra_oculta(palabra_oculta):
    """..."""

    game.draw_text(palabra_oculta, ANCHO_VENTANA / 2, MARGEN_Y, size=20)

def graficar_mensaje(mensaje):
    """..."""

    game.draw_text(mensaje, ANCHO_VENTANA / 2, MARGEN_Y * 2)

def graficar_letras_usadas(letras_usadas):
    """..."""

    game.draw_text("LETRAS USADAS", ANCHO_VENTANA / 2, ALTO_VENTANA - MARGEN_Y * 2)
    game.draw_text(", ".join(letras_usadas), ANCHO_VENTANA / 2, ALTO_VENTANA - MARGEN_Y)

def graficar_mensaje_final(condicion, palabra):
    """..."""

    if condicion:
        game.draw_text("PERDISTE", ANCHO_VENTANA / 2, MARGEN_Y * 2)
    else:
        game.draw_text("GANASTE!!!", ANCHO_VENTANA / 2, MARGEN_Y * 2)

    game.draw_text(f"La palabra era: {palabra}", ANCHO_VENTANA / 2, MARGEN_Y * 4)

def graficar_boton_volver_a_jugar():
    """..."""

    game.draw_rectangle(ANCHO_BOTON[0], ALTO_BOTON[0], ANCHO_BOTON[1], ALTO_BOTON[1], fill="#000000", outline="#FFFFFF")
    game.draw_text("Volver a empezar", sum(ANCHO_BOTON) / 2, sum(ALTO_BOTON) / 2, size=15)

def dibujar_horca():
    """..."""

    game.draw_line(ANCHO_VENTANA / 2, MARGEN_Y * 5, ANCHO_VENTANA / 2 + MARGEN_X, MARGEN_Y * 5)
    game.draw_line(ANCHO_VENTANA / 2 + MARGEN_X, MARGEN_Y * 5, ANCHO_VENTANA / 2 + MARGEN_X, MARGEN_Y * 8)

def dibujar_persona(fallos):
    """..."""

    partes = list(PARTES_PERSONA)
    for i in range(fallos):
        coord_parte_cuerpo = PARTES_PERSONA[partes[i]]
        if i == 0:
            game.draw_oval(coord_parte_cuerpo[0], coord_parte_cuerpo[1], coord_parte_cuerpo[2], coord_parte_cuerpo[3])
        else:
            game.draw_line(coord_parte_cuerpo[0], coord_parte_cuerpo[1], coord_parte_cuerpo[2], coord_parte_cuerpo[3])