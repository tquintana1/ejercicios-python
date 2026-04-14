# ============================================================
# ARCHIVO: bucle_for_basico1.py
# DESCRIPCIÓN: Ejercicios básicos con bucles for en Python
# ============================================================


# ------------------------------------------------------------
# EJERCICIO 1 - BÁSICO
# Imprime todos los números enteros del 0 al 100.
# range(101) genera números desde 0 hasta 100 (101 no incluido).
# ------------------------------------------------------------
print("=" * 40)
print("EJERCICIO 1: Números del 0 al 100")
print("=" * 40)

for numero in range(101):       # range(101) va de 0 a 100 inclusive
    print(numero)


# ------------------------------------------------------------
# EJERCICIO 2 - MÚLTIPLES DE 2
# Imprime todos los múltiplos de 2 entre 2 y 500.
# range(inicio, fin+1, paso) con paso=2 salta de dos en dos.
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 2: Múltiplos de 2 entre 2 y 500")
print("=" * 40)

for numero in range(2, 501, 2):  # empieza en 2, termina en 500, de 2 en 2
    print(numero)


# ------------------------------------------------------------
# EJERCICIO 3 - CONTANDO VANILLA ICE
# Imprime del 1 al 100.
# - Si el número es divisible por 10 → imprime "baby"
# - Si el número es divisible por 5  → imprime "ice ice"
# - De lo contrario                  → imprime el número
# NOTA: el caso de divisible por 10 se evalúa PRIMERO porque
#       todo múltiplo de 10 también es múltiplo de 5.
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 3: Contando Vanilla Ice")
print("=" * 40)

for numero in range(1, 101):            # del 1 al 100 inclusive
    if numero % 10 == 0:                # divisible por 10 → "baby"
        print("baby")
    elif numero % 5 == 0:               # divisible por 5 → "ice ice"
        print("ice ice")
    else:                               # cualquier otro número → se imprime tal cual
        print(numero)


# ------------------------------------------------------------
# EJERCICIO 4 - WOW. NÚMERO GIGANTE A LA VISTA
# Suma todos los números pares del 0 al 500,000 e imprime el total.
# Se usa una variable acumuladora (total) que parte en 0
# y se le van sumando los pares en cada iteración.
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 4: Suma de pares del 0 al 500,000")
print("=" * 40)

total = 0                               # variable acumuladora, arranca en cero

for numero in range(0, 500_001, 2):     # de 0 a 500,000 saltando de 2 en 2 (solo pares)
    total += numero                     # equivale a: total = total + numero

print(f"La suma total es: {total}")     # imprime el resultado final


# ------------------------------------------------------------
# EJERCICIO 5 - REGRÉSAME AL 3
# Imprime los números positivos comenzando desde 2024,
# contando de 3 en 3 hacia atrás, hasta llegar a 1 o más.
# range(inicio, fin, paso_negativo) cuenta en reversa.
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 5: Cuenta regresiva desde 2024 de 3 en 3")
print("=" * 40)

for numero in range(2024, 0, -3):       # de 2024 hasta 1, restando 3 en cada paso
    print(numero)


# ------------------------------------------------------------
# EJERCICIO 6 - CONTADOR DINÁMICO
# Usa tres variables configurables:
#   numInicial → desde dónde empieza la búsqueda
#   numFinal   → hasta dónde llega la búsqueda
#   multiplo   → qué múltiplo se quiere filtrar
# El bucle recorre todos los números entre numInicial y numFinal
# e imprime solo aquellos que sean múltiplos de 'multiplo'.
# Ejemplo: numInicial=3, numFinal=10, multiplo=2 → imprime 4,6,8,10
# ------------------------------------------------------------
print("\n" + "=" * 40)
print("EJERCICIO 6: Contador dinámico")
print("=" * 40)

numInicial = 3      # número desde donde comienza el recorrido
numFinal   = 10     # número donde termina el recorrido (incluido)
multiplo   = 2      # solo se imprimen los múltiplos de este valor

print(f"Múltiplos de {multiplo} entre {numInicial} y {numFinal}:")

for numero in range(numInicial, numFinal + 1):   # +1 para incluir numFinal
    if numero % multiplo == 0:                   # si el resto es 0, es múltiplo
        print(numero)
