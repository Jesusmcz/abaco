########################################################################################
''' Codigo para resolver un Abaco matematico,
Taller de cierre Modulo 2 Awakelab- Fullstack Python FSP 154-1 
'''
########################################################################################


########################################################################################

# Ingreso por pantalla de valor a evaluar

print("Ingrese a continuación un numero entero positivo no mayor a 1 millon : ") 
numero = int(input("¿que numero desea ingresar? :"))

# definición de variables para while verificador del numero ingresado

limite = 999999 #numero maximo admitido
prueba = False #se inicia en falso la variable para entrar al while 

while prueba == False:
    if int(numero) > int(limite):
        print("El numero ingresado es muy grande, ingrese numero menor a 1 millon, ")
        numero = int(input("¿que numero desea ingresar? :"))
    else:
        print("el numero ", numero , "ingresado es valido")
        prueba = True

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

########################################################################################


########################################################################################

