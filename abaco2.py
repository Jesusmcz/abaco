# Se definen funciones

# Se inicializa el tablero de abaco
def inicializar_tablero():
    tablero = []
    for i in range(0,9):
        fila = []
        for j in range(0,6):
            fila.append(" ||| ")
        tablero.append(fila)
    return tablero
# Se imprime en pantalla el tablero del abaco
def imprimir_tablero(tablero):
    tablero.reverse()
    for fila in tablero:
        for elemento in fila:
            print(elemento, sep="", end="")
        print()
# Llena el tablero del abaco con xxx
def llenar_tablero(digitos, tablero):
    for j in range(0, 6):
        for i in range(0, digitos[j]):
            tablero[i][j] = " XXX "
    return tablero
# Se pregunta y descompone el numero de 6 cifras
def preguntar_y_generar_digitos():
    numero = input("Ingrese un número de 6 digitos: ")
    lista_numeros = list(numero)
    numeros_separados = []
    for elemento in lista_numeros:
        numeros_separados.append(int(elemento))
    return numeros_separados
# Estructura del programa
tablero = inicializar_tablero()

print()

digitos = preguntar_y_generar_digitos()
tablero = llenar_tablero(digitos, tablero)
imprimir_tablero(tablero)

# FALTA DELIMITAR QUE SEA SOLO NUMEROS DE 6 CIFRAS, NO LETRAS NI SIMBOLOS
# GUARDAR RESPUESTA Y SALIR DEL LOOP CON PALABRA SALIR