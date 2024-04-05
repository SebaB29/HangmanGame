def comprobar_letra(letra, juego):
    """
    Recibe la letra ingresada por el jugador.
    Determina si esta en la palabra, en caso de que no este suma un fallo y devuelve la cantidad de fallos.
    """

    if verificar_entrada(letra):
        mensaje = ""
        if letra in juego["PALABRA"] and not letras_utilizadas(letra, juego["LETRAS_USADAS"]):
            for i in range(len(juego["PALABRA"])):
                if juego["PALABRA"][i] == letra:
                    juego["PALABRA_OCULTA"][i] = letra

        elif letras_utilizadas(letra, juego["LETRAS_USADAS"]):
            mensaje = f"La letra '{letra}' ya fue utilizada"

        else:
            mensaje = f"La letra {letra} no esta en la palabra"
            juego["FALLOS"] += 1
    else:
        mensaje = "Ingrese una letra"
    
    return mensaje

def verificar_entrada(letra):
    """
    Recibe el caracter ingresado por el jugador, devuelve True si es valido, en caso contrario devuelve False.
    """

    return letra.isalpha() and len(letra) == 1

def letras_utilizadas(letra, letras_usadas):
    """
    Verifica si la letra recibida ya se habia utilizado.
    Si no se utilizo la agrega a la lista de letras usadas y devuelve False, en caso contrario devuelve True.
    """

    if letra not in letras_usadas:
        letras_usadas.append(letra)
        return False
    return True