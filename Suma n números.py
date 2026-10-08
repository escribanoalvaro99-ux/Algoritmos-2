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
N = int(input("Ingrese un número N: "))

suma = 0

while N > 0:
    suma += N  # Equivale a: suma = suma + N
    N -= 1     # Equivale a: N = N - 1

print(f"La suma total es: {suma}")