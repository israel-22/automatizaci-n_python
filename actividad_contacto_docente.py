#1. Escribe un código que solicite al usuario un número y,
#  utilizando un for, imprime el factorial del número ingresado. Pista:
#  necesitarás una variable extra para guardar el resultado.

# Solicitar al usuario un número
numero = int(input("Ingresa un número entero: "))

# Inicializar la variable para almacenar el resultado del factorial
factorial = 1

# Usar un bucle for para calcular el factorial
for i in range(1, numero + 1):
    factorial *= i

# Mostrar el resultado
print(f"El factorial de {numero} es {factorial}")



#2. Escribe un código que imprima todos los números perfectos que hay entre 0 y 100. 

# Los números perfectos son números cuya suma de sus divisores son equivalentes al mismo número. 
# Ej: el 6 es un número perfecto, ya que es divisible para 1, 2 y 3, y si sumamos estos tres números 
# obtenemos como resultado de nuevo el 6.

# Pista: necesitarás un for anidado.


        # Recorrer los números entre 1 y 100
print("Números perfectos entre 0 y 100:")
for num in range(1, 101):
    suma_divisores = 0  # Almacena la suma de los divisores del número

    # Encontrar los divisores del número
    for i in range(1, num):
        if num % i == 0:  # Si es divisor
            suma_divisores += i

    # Verificar si el número es perfecto
    if suma_divisores == num:
        print(num)


#ejercicio 3 usando for

# # Número de filas de la pirámide
filas = int(input("Ingresa el número de filas para la pirámide: "))

# Generar el patrón
for i in range(1, filas + 1):
    # Espacios iniciales
    print(" " * (filas - i), end="")
    
    # Primera estrella
    print("*", end="")
    
    # Espacios entre las estrellas
    if i > 1:
        print(" " * (2 * (i - 1) - 1), end="")
        print("*")
    else:
        print()  # Salto de línea para la primera fila



#ejercicio 4 usando for

# # pino perfecto

# # Número de filas para la pirámide superior
# filas = int(input("Ingresa el número de filas para la pirámide: "))

# # Generar la pirámide superior
# for i in range(1, filas + 1):
#     # Espacios iniciales
#     print(" " * (filas - i), end="")
    
#     # Asteriscos y espacios intercalados
#     for j in range(1, i * 2):
#         if j % 2 == 0:  # Espacios intermedios
#             print(" ", end="")
#         else:  # Asteriscos
#             print("*", end="")
#     print()  # Salto de línea al final de cada fila

# # Generar la parte inferior (línea vertical de asteriscos)
# for _ in range(3):  # Tres líneas
#     print(" " * (filas - 1) + "*")



    

# Número de filas para la pirámide superior
filas = int(input("Ingresa el número de filas para la pirámide: "))

# Generar la pirámide superior
for i in range(1, filas + 1):
    # Espacios iniciales
    if i == 1:  # Primera fila
        print(" " * (filas - 1) + "*")
    elif i == 2:  # Segunda fila
        print(" " * (filas - 2) + "***")
    else:  # Filas posteriores
        print(" " * (filas - i) + "*" + " " * (1 * (i - 1) - 1) + "*" + " " * (1 * (i - 1) - 1) + "*")

# Generar la parte inferior (línea vertical de asteriscos)
for _ in range(3):  # Tres líneas
    print(" " * (filas - 1) + "*")




# Ejercicio 5 usando for

filas = int(input("Ingresa el número de filas para la pirámide: "))

# Generar la pirámide superior
for i in range(1, filas + 1):
    # Espacios iniciales
    if i == 1:  # Primera fila
        print(" " * (filas - 1) + "*")
    elif i == 2:  # Segunda fila
        print(" " * (filas - 2) + "***")
    else:  # Filas posteriores
        print(" " * (filas - i) + "*" + " " * (1 * (i - 1) - 1) + "*" + " " * (1 * (i - 1) - 1) + "*")

# Imprimir la base de la pirámide (línea completa de asteriscos)
print("*" * (2 * (filas - 1) + 1))

# Generar la parte inferior (línea vertical de asteriscos)
for _ in range(4):  # Cuatro líneas
    print(" " * (filas - 1) + "*")


# ejercicio 6 usando for:

# Solicitar al usuario el número de filas para la flecha
filas = int(input("Ingresa el número de filas para la flecha: "))

# Parte ascendente de la flecha (igual al número de filas ingresado)
for i in range(1, filas + 1):
    print(" " * (filas - i) + "*" * i)

# Fila recta
print("*" + "*" * (2 * filas - 1))  # Ajuste en la longitud de la fila recta para alinearla correctamente

# Parte descendente de la flecha (el mismo número de filas que la parte ascendente)
for i in range(filas - 1, 0, -1):
    print(" " * (filas - i) + "*" * i)


# ejercicio 7 usando for:

# ejercicio 7 usando for:

# Solicitar al usuario el número de filas para la flecha
filas = int(input("Ingresa el número de filas para la flecha hueca: "))

# Parte ascendente (pirámide hueca)
for i in range(1, filas + 1):
    if i == 1:
        print(" " * (filas - i) + "*")  # Solo un asterisco en la punta
    else:
        print(" " * (filas - i) + "*" + " " * (1* i - 2) + "*")  # Asteriscos en los bordes

# Fila recta
# print(" " * (2 * filas-1))

print("* " ," " * (filas -4) + "*" * (2 * filas - 1))


# Parte descendente (pirámide hueca invertida)
for i in range(filas - 0,  0, -1):
    if i == 1:
        print(" " * (filas - i) + "*")  # Solo un asterisco en la base
    else:
        print(" " * (filas - i) + "*" + " " * (1 * i - 2) + "*")  # Asteriscos en los bordes





