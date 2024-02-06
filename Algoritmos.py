#Ejercicio 1
def ej1(mat):
    suma = 0
    for i in mat:
        if len(i) != len(mat):
            return print("La matriz no es cuadrada")
    for i in range(len(mat)):
        suma += mat[i][i]
    return suma


#Ejercicio 2
def ej2(mat, numero):
    for fila in mat:
        for elemento in fila:
            if elemento == numero:
                return True
		
    return False




#Ejercicio 3
def ej3(arreglo, numero):
    for elemento in arreglo:
        if elemento == numero:
            return True
    return False

