# ============================================================
# ARCHIVO: funciones_intermedias_1.py
# DESCRIPCIÓN: Práctica de iteración de diccionarios y listas,
#              y creación de funciones intermedias en Python
# ============================================================


# ============================================================
# EJERCICIO 1 - ACTUALIZAR VALORES EN DICCIONARIOS Y LISTAS
# ============================================================

# --- Estructuras de datos originales ---

matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne",     "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile":  ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# --- Cambio 1: valor 3 en matriz por 6 ---
# matriz[1] accede a la segunda lista → [3, 7, 14]
# matriz[1][0] accede al primer elemento de esa lista → 3
matriz[1][0] = 6
print("Matriz actualizada:", matriz)
# Resultado esperado: [ [10, 15, 20], [6, 7, 14] ]

# --- Cambio 2: nombre del primer cantante ---
# cantantes[0] accede al primer diccionario
# ["nombre"] accede a la clave "nombre" de ese diccionario
cantantes[0]["nombre"] = "Enrique Martin Morales"
print("Cantantes actualizados:", cantantes)
# Resultado esperado: primer cantante con nombre "Enrique Martin Morales"

# --- Cambio 3: "Cancún" por "Monterrey" en ciudades ---
# ciudades["México"] accede a la lista de ciudades de México → [..., "Cancún"]
# .index("Cancún") encuentra la posición de "Cancún" en esa lista → 2
indice_cancun = ciudades["México"].index("Cancún")   # busca la posición de "Cancún"
ciudades["México"][indice_cancun] = "Monterrey"       # reemplaza en esa posición
print("Ciudades actualizadas:", ciudades)
# Resultado esperado: "Cancún" reemplazado por "Monterrey"

# --- Cambio 4: latitud en coordenadas ---
# coordenadas[0] accede al primer (y único) diccionario de la lista
# ["latitud"] accede a la clave "latitud"
coordenadas[0]["latitud"] = 9.9355431
print("Coordenadas actualizadas:", coordenadas)
# Resultado esperado: latitud = 9.9355431


# ============================================================
# EJERCICIO 2 - ITERAR A TRAVÉS DE UNA LISTA DE DICCIONARIOS
# Función: iterarDiccionario(lista)
# Recibe una lista de diccionarios e imprime cada llave
# con su valor correspondiente en formato: llave - valor
# ============================================================
def iterarDiccionario(lista):
    for diccionario in lista:                        # recorre cada diccionario de la lista
        linea = ""                                   # cadena que armará una línea por diccionario
        pares = []                                   # lista temporal de pares "llave - valor"

        for llave, valor in diccionario.items():     # recorre cada par llave-valor del diccionario
            pares.append(f"{llave} - {valor}")       # agrega cada par formateado

        print(", ".join(pares))                      # une los pares con coma e imprime en una línea


# ============================================================
# EJERCICIO 3 - OBTENER VALORES DE UNA LISTA DE DICCIONARIOS
# Función: iterarDiccionario2(llave, lista)
# Recibe el nombre de una llave y una lista de diccionarios.
# Imprime el valor de esa llave en cada diccionario.
# ============================================================
def iterarDiccionario2(llave, lista):
    for diccionario in lista:                        # recorre cada diccionario de la lista
        if llave in diccionario:                     # verifica que la llave exista en el diccionario
            print(diccionario[llave])                # imprime el valor correspondiente a esa llave


# ============================================================
# EJERCICIO 4 - ITERAR A TRAVÉS DE UN DICCIONARIO CON LISTAS
# Función: imprimirInformacion(diccionario)
# Recibe un diccionario donde los valores son listas.
# Imprime la cantidad de elementos y luego cada valor de la lista.
# ============================================================
def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():         # recorre cada par clave-lista del diccionario
        print(f"{len(lista)} {clave.upper()}")       # imprime cantidad + nombre de clave en mayúsculas
        for elemento in lista:                       # recorre cada elemento de la lista
            print(elemento)                          # imprime el elemento
        print()                                      # línea en blanco entre secciones


# ============================================================
# BLOQUE DE PRUEBAS
# Se ejecuta solo al correr este archivo directamente.
# ============================================================
if __name__ == "__main__":

    # --- Prueba Ejercicio 2 ---
    print("\n" + "=" * 45)
    print("EJERCICIO 2: iterarDiccionario")
    print("=" * 45)
    cantantes_full = [
        {"nombre": "Ricky Martin",    "pais": "Puerto Rico"},
        {"nombre": "Chayanne",        "pais": "Puerto Rico"},
        {"nombre": "José José",       "pais": "México"},
        {"nombre": "Juan Luis Guerra","pais": "República Dominicana"}
    ]
    iterarDiccionario(cantantes_full)

    # --- Prueba Ejercicio 3 ---
    print("\n" + "=" * 45)
    print("EJERCICIO 3: iterarDiccionario2 - por 'nombre'")
    print("=" * 45)
    iterarDiccionario2("nombre", cantantes_full)

    print("\nEJERCICIO 3: iterarDiccionario2 - por 'pais'")
    print("=" * 45)
    iterarDiccionario2("pais", cantantes_full)

    # --- Prueba Ejercicio 4 ---
    print("\n" + "=" * 45)
    print("EJERCICIO 4: imprimirInformacion")
    print("=" * 45)
    costa_rica = {
        "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
        "comidas":  ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
    }
    imprimirInformacion(costa_rica)
