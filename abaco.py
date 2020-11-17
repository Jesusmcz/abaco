
########################################################################################
<<<<<<< HEAD
''' 

Codigo para resolver un Abaco matematico,
Taller de cierre Modulo 2 Awakelab- Fullstack Python FSP 154-1 
GRUPO 3
ALVARO SILVA
JESUS CONTRERAS 
GERMAN MELGAREJO
JEAN CARLOS GUIA MOY
https://github.com/Jesusmcz/abaco

=======
''' Codigo para resolver un Abaco matematico,
Taller de cierre Modulo 2 Awakelab- Fullstack Python FSP 154-1 
GRUPO 3
ALVARO
JESUS
GERMAN
JEAN CARLOS GUIA MOY
https://github.com/Jesusmcz/abaco
>>>>>>> 36a51defdeb0e3ea359164540f7cb5a111a6001e
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
<<<<<<< HEAD
    numero = input("Ingrese a continuación un numero entero positivo no mayor
     a 1 millon: ")
=======
    numero = input("Ingrese a continuación un numero entero positivo no mayor a 1 millon: ")
>>>>>>> 36a51defdeb0e3ea359164540f7cb5a111a6001e
    limite = 999999 #numero maximo admitido
    prueba = False #se inicia en falso la variable para entrar al while 
    while prueba == False:
        if int(numero) > int(limite): # probamos que el numero ingresado sea valido
<<<<<<< HEAD
            print("El numero ingresado es muy grande, ingrese numero menor
             a 1 millon, ")
=======
            print("El numero ingresado es muy grande, ingrese numero menor a 1 millon, ")
>>>>>>> 36a51defdeb0e3ea359164540f7cb5a111a6001e
            numero = int(input("¿que numero desea ingresar? :"))
        else:
            print("el numero ", numero , "ingresado es valido")
            prueba = True
        break
    lista_numeros = list(numero)# Separamos el numero en elementos
<<<<<<< HEAD

=======
>>>>>>> 36a51defdeb0e3ea359164540f7cb5a111a6001e
    numeros_separados = []
    for elemento in lista_numeros:
        numeros_separados.append(int(elemento))
    return numeros_separados
    
<<<<<<< HEAD
=======
########################################################################################
#almacenar todos los numeros solicitados x el usuario en una lista

########################################################################################
# función abrir numero en unidades, decenas centenas y asi susesivamente

def abaco(entrada_abaco):

    centenares_miles = entrada_abaco // 100000
    resto = entrada_abaco - centenares_miles * 100000
    
    decenas_miles =  ( resto // 10000 )
    resto = resto - decenas_miles *  10000
    
    miles = (resto // 1000 )
    resto = resto - miles * 1000
    
    centenas =( resto // 100)
    resto = resto - centenas * 100
    
    decenas = (resto // 10)
    resto = resto - decenas * 10
    
    unidades =(resto // 1 )
    resto = resto - unidades
    abaco_ordenado = [centenares_miles, decenas_miles, miles, centenas, decenas, unidades]
    print(abaco_ordenado)

    return (abaco_ordenado)

>>>>>>> 36a51defdeb0e3ea359164540f7cb5a111a6001e

########################################################################################
# Estructura del programa
tablero = inicializar_tablero()

print()

digitos = preguntar_y_generar_digitos()
tablero = llenar_tablero(digitos, tablero)
imprimir_tablero(tablero)


