import random

# Inicializar juego
def inicializar_juego():
    juego = [[None for _ in range(4)] for _ in range(4)]
    juego = insertar_nuevo_random(juego)
    juego = insertar_nuevo_random(juego)
    return juego

# Mostrar juego
def mostrar_juego(grilla):

    print()
    print(f"    {grilla[0][0]}  |   {grilla[0][1]}  |   {grilla[0][2]}  |   {grilla[0][3]}  ")
    print("---------------------------------------")
    print(f"    {grilla[1][0]}  |   {grilla[1][1]}  |   {grilla[1][2]}  |   {grilla[1][3]}  ")
    print("---------------------------------------")
    print(f"    {grilla[2][0]}  |   {grilla[2][1]}  |   {grilla[2][2]}  |   {grilla[2][3]}  ")
    print("---------------------------------------")
    print(f"    {grilla[3][0]}  |   {grilla[3][1]}  |   {grilla[3][2]}  |   {grilla[3][3]}  ")
    print("---------------------------------------")
# Juego ganado
def juego_ganado(juego):
    for fila in juego:
        if 2048 in fila:
            return True
    return False

# Juego perdido
def juego_perdido(juego):
    for fila in juego:
        if None in fila:
            return False
    return True


# Pedir direccion
def pedir_direccion(juego):
  '''
    movimiento_valido = False
    while not movimiento_valido:
        dir = input("Seleccione una direccion (w, a, s,d): ")
        movimiento_valido = verificar_validez_movimiento(dir)
        if direccion_valida(juego, dir):
            return dir
'''
  dir = input("Seleccione una direccion (w, a, s,d): ")
  return dir
# Actualizar juego

def actualizar_juego(juego, dir):
    '''
    - Trasponer el tablero si es necesario
    - Por cada fila:
        - Invertir la fila si es necesario
        - Combinar en nueva fila
        - Invertir la fila resultante si es necesario
    - Trasponer el tablero resultante si es necesario'''

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
    nueva_fila = []
    for elemento in fila:
        if elemento:
            nueva_fila.append(elemento)
    return nueva_fila

def agregar_none(fila, cantidad):
    for i in range(cantidad):
        fila.append(None)
    return fila

def invertir_fila(fila):
    return fila[::-1]

def invertir_matriz(juego):
    matriz_invertida = []
    for col in range(len(juego)):
        fila_invertida = []
        for fila in range(len(juego)):
            fila_invertida.append(juego[fila][col])
        matriz_invertida.append(fila_invertida)

    return matriz_invertida
# Insertar nuevo random
def insertar_nuevo_random(nuevo_juego):
    ''' Insertar un nuevo elemento a la grilla y devolver un nuevo juego'''
    while True:
        fila = random.randint(0, 3)
        col = random.randint(0, 3)
        if nuevo_juego[fila][col] == None:
            nuevo_juego[fila][col] = 2
            break
    return nuevo_juego




