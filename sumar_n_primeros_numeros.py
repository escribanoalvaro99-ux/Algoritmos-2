'''
Algoritmo SumarNPrimerosNumeros
Escribir "Ingrese un número N:"
    Leer N
    
    suma <- 0
    
    Mientras N > 0 Hacer
        suma <- suma + N
        N <- N - 1
    FinMientras
    
    Escribir "La suma total es: ", suma
FinAlgoritmo
'''
def sumar_primeros_numeros(n):
    suma = 0
    m = n
    while n > 0:
        suma += n
        n -= 1
    return suma
print("Prueba 1 (N = 5):", sumar_primeros_numeros(5))
print("Prueba 2 (N = 10):", sumar_primeros_numeros(10))