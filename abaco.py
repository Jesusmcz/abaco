
########################################################################################
''' 

Codigo para resolver un Abaco matematico,
Taller de cierre Modulo 2 Awakelab- Fullstack Python FSP 154-1 
GRUPO 3
ALVARO SILVA
JESUS CONTRERAS 
GERMAN MELGAREJO
JEAN CARLOS GUIA MOY
https://github.com/Jesusmcz/abaco

'''
########################################################################################
# Se inicializa el tablero de abaco
def inicializar_tablero():
    tablero = []
    for i in range(0,9):
        fila = []
        for j in range(0,6):
            fila.append(" ||| ")
        tablero.append(fila)
    return tablero
########################################################################################
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
########################################################################################
# Se pregunta y descompone el numero de 6 cifras

def preguntar_y_generar_digitos():
    numero = input("Ingrese a continuación un numero entero positivo no mayor
     a 1 millon: ")
    limite = 999999 #numero maximo admitido
    prueba = False #se inicia en falso la variable para entrar al while 
    while prueba == False:
        if int(numero) > int(limite): # probamos que el numero ingresado sea valido
            print("El numero ingresado es muy grande, ingrese numero menor
             a 1 millon, ")
            numero = int(input("¿que numero desea ingresar? :"))
        else:
            print("el numero ", numero , "ingresado es valido")
            prueba = True
        break
    lista_numeros = list(numero)# Separamos el numero en elementos

    numeros_separados = []
    for elemento in lista_numeros:
        numeros_separados.append(int(elemento))
    return numeros_separados
    

########################################################################################
# Estructura del programa
tablero = inicializar_tablero()

print()

digitos = preguntar_y_generar_digitos()
tablero = llenar_tablero(digitos, tablero)
imprimir_tablero(tablero)

