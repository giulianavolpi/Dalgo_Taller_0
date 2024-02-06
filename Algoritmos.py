#Ejercicio 1
def suma_diagonal_principal(matriz):
    suma = 0
    for i in matriz:
        if len(i) != len(matriz):
            return print("La matriz no es cuadrada")
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma


#Ejercicio 2
def buscar_numero(matriz, numero):
    for fila in matriz:
        for elemento in fila:
            if elemento == numero:
                return True
		
    return False




#Ejercicio 3
def buscar_numero2(arreglo, numero):
    for elemento in arreglo:
        if elemento == numero:
            return True
    return False

