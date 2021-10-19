import random

TAMANIO_GRILLA = 4
TECLAS = ["w", "d", "s", "a"]
NUMERO_FINAL = 2048
VALORES_ALEATORIOS = [2, 4]
VALOR_VACIO = " "
SEPARADOR_VERTICAL = "|"
SEPARADOR_HORIZONTAL = "-----------" * TAMANIO_GRILLA


# Inicializar juego
def inicializar_juego():
    """
    :return: Devuelve un nuevo juego
    """
    juego = [[VALOR_VACIO for _ in range(TAMANIO_GRILLA)] for _ in range(TAMANIO_GRILLA)]
    juego = insertar_nuevo_random(juego)
    juego = insertar_nuevo_random(juego)
    return juego


# Mostrar juego
def mostrar_juego(grilla):
    print()
    for linea in grilla:
        for elemento in linea:
            print(f"{SEPARADOR_VERTICAL}{elemento:^10}", end="")
        print(f"{SEPARADOR_VERTICAL}\n{SEPARADOR_HORIZONTAL}")

    print("\n")


# Juego ganado
def juego_ganado(juego):
    """
    :param juego:
    :return: True, si juego ganado; False, caso contrario
    """

    for fila in juego:
        if NUMERO_FINAL in fila:
            return True
    return False


# Juego perdido
def juego_perdido(juego):
    """El juego se considera perdido cuando se llena el tablero y no hay ningun movimiento posible"""
    if validar_tablero_lleno(juego):
        # Si el tablero está lleno, verificamos si existe combinacion posible en el
        return validar_tablero_lleno(juego)
        # Si NO existe combinacion posible, el juego se considera perdido
    return False


# Pedir direccion
def pedir_direccion(juego):
    """
    movimiento_valido = False
    while not movimiento_valido:
        dir = input("Seleccione una direccion (w, a, s,d): ")
        movimiento_valido = verificar_validez_movimiento(dir)
        if direccion_valida(juego, dir):
            return dir """

    while True:
        # Mientras la tecla no sea valida se pide.
        dir = input("Seleccione una direccion (w, a, s, d): ")
        # Para que sea valida, debe ser del alfabeto y debe estar en las posibles teclas
        if (not dir.isalpha()) or (not tecla_valida(dir)):
            print("La tecla ingresada es invalida\n")
        else:
            break  # Condicion de corte

    return dir.lower()


# Actualizar juego
def actualizar_juego(juego, dir):
    """
    - Trasponer el tablero si es necesario
    - Por cada fila:
        - Invertir la fila si es necesario
        - Combinar en nueva fila
        - Invertir la fila resultante si es necesario
    - Trasponer el tablero resultante si es necesario"""

    nuevo_juego = []

    if dir == 'a':
        for fila in juego:

            nueva_fila = combinar_en_nueva_fila(fila)
            nuevo_juego.append(nueva_fila)
        return nuevo_juego
    if dir == 'd':
        for fila in juego:
            nueva_fila = combinar_en_nueva_fila(invertir_fila(fila))
            nuevo_juego.append(invertir_fila(nueva_fila))
        return nuevo_juego
    if dir == 'w':
        juego_traspuesto = invertir_matriz(juego)
        for fila in juego_traspuesto:

            nueva_fila = combinar_en_nueva_fila(fila)
            nuevo_juego.append(nueva_fila)
        return invertir_matriz(nuevo_juego)

    if dir == 's':
        juego_traspuesto = invertir_matriz(juego)
        for fila in juego_traspuesto:
            nueva_fila = combinar_en_nueva_fila(invertir_fila(fila))
            nuevo_juego.append(invertir_fila(nueva_fila))
        return invertir_matriz(nuevo_juego)


def combinar_en_nueva_fila(fila):
    """
    :param fila:
    :return: Devuelve una nueva fila, combinando los elementos si son iguales.
    """

    len_original = len(fila)

    fila = eliminar_none(fila)

    len_fila = len(fila)
    cantidad_none_a_agregar = len_original - len_fila

    actual = 0
    siguente = 1
    resultante = []

    if fila == resultante:
        fila = agregar_none(fila, cantidad_none_a_agregar)
        return fila

    if len_fila == 1:
        resultante.append(fila[0])
        resultante = agregar_none(resultante, cantidad_none_a_agregar)
        return resultante

    for _ in range(len_fila):

        if fila[actual] == fila[siguente]:
            resultante.append(fila[actual] + fila[siguente])
            cantidad_none_a_agregar += 1
            actual = siguente + 1
            siguente += 2
            if actual == len_fila:
                break
            elif siguente == len_fila:
                resultante.append(fila[actual])
                break
        elif fila[actual] != fila[siguente]:
            resultante.append(fila[actual])
            actual += 1
            siguente += 1
            if siguente == len_fila:
                resultante.append(fila[actual])
                break

    resultante = agregar_none(resultante, cantidad_none_a_agregar)
    return resultante


def eliminar_none(fila):
    """
    :param fila:
    :return: fila quitando los valores vacios para operar
    """
    nueva_fila = []
    for elemento in fila:
        if elemento != VALOR_VACIO:
            nueva_fila.append(elemento)
    return nueva_fila


def agregar_none(fila, cantidad):
    """
    :param fila:
    :param cantidad:
    :return: Fila con los valores vacios correspondientes
    """
    for i in range(cantidad):
        fila.append(VALOR_VACIO)
    return fila


def invertir_fila(fila):
    return fila[::-1]


def invertir_matriz(juego):
    """
    :param juego:
    :return: La grilla invertira
    """
    matriz_invertida = []
    for col in range(TAMANIO_GRILLA):
        fila_invertida = []
        for fila in range(TAMANIO_GRILLA):
            fila_invertida.append(juego[fila][col])
        matriz_invertida.append(fila_invertida)

    return matriz_invertida


# Insertar nuevo random
def insertar_nuevo_random(nuevo_juego):
    """
    :param nuevo_juego: 
    :return: Devuelve el juego luego de insertar un nuevo elemento en una posicion random
    """""
    while True:
        fila = random.randint(0, TAMANIO_GRILLA - 1)
        col = random.randint(0, TAMANIO_GRILLA - 1)

        if nuevo_juego[fila][col] == VALOR_VACIO:
            nuevo_juego[fila][col] = VALORES_ALEATORIOS[random.randint(0, len(VALORES_ALEATORIOS) - 1)]
            break
    return nuevo_juego


def tecla_valida(movimiento):
    """
    :param movimiento:
    :return: True, si la tecla esta contemplada; False, caso contrario
    """
    return movimiento.lower() in TECLAS


def validar_existencia_combinacion_posible(juego):
    """
    :param juego:
    :return: Devuelve True si hay una combinacion posible en el juego; Devuelve False si no existe combinacion posible
    En el caso que ninguna combinacion sea posible y el tablero este lleno, el juego resulta perdido

    Para verificar evaluamos el juego en todas las direcciones posibles, si el nuevo_juego resulta
    diferente para alguno de ellos,
    quiere decir que hay movimiento posible
    """
    for direccion in TECLAS:
        juego_nuevo = actualizar_juego(juego, direccion)
        if juego_nuevo != juego:
            return True
    return False


def validar_tablero_lleno(juego):
    """
    :param juego:
    :return: True si no existen espacios vacios en el tablero; False en caso contrario
    """
    for fila in juego:
        if VALOR_VACIO in fila:
            return False
    return True

