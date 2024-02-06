#Ejercicio 1
def suma_diagonal_principal(mat):
    suma = 0
    for i in mat:
        if len(i) != len(mat):
            return print("La matriz no es cuadrada")
    for i in range(len(mat)):
        suma += mat[i][i]
    return suma


#Ejercicio 2
def buscar_numero(mat, numero):
    for fila in mat:
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

