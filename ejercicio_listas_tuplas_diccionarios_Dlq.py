# ============================================================
# ARCHIVO: ejercicio_listas_tuplas_diccionarios.py
# DESCRIPCIÓN: Análisis básico de datos de ventas usando
#              listas, tuplas y diccionarios en Python
# ============================================================


# ============================================================
# PASO 1 - CARGA DE DATOS
# Se crea una lista de diccionarios llamada "ventas".
# Cada diccionario representa una venta con las claves:
#   - "fecha"    : fecha de la venta (string)
#   - "producto" : nombre del producto (string)
#   - "cantidad" : unidades vendidas (entero)
#   - "precio"   : precio unitario (flotante)
# ============================================================
ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop",   "cantidad": 3,  "precio": 1200.00},
    {"fecha": "2024-01-01", "producto": "Mouse",    "cantidad": 10, "precio": 25.50},
    {"fecha": "2024-01-02", "producto": "Teclado",  "cantidad": 5,  "precio": 45.00},
    {"fecha": "2024-01-02", "producto": "Laptop",   "cantidad": 2,  "precio": 1200.00},
    {"fecha": "2024-01-03", "producto": "Mouse",    "cantidad": 8,  "precio": 25.50},
    {"fecha": "2024-01-03", "producto": "Monitor",  "cantidad": 4,  "precio": 350.00},
    {"fecha": "2024-01-04", "producto": "Teclado",  "cantidad": 6,  "precio": 45.00},
    {"fecha": "2024-01-04", "producto": "Monitor",  "cantidad": 2,  "precio": 350.00},
    {"fecha": "2024-01-05", "producto": "Laptop",   "cantidad": 1,  "precio": 1200.00},
    {"fecha": "2024-01-05", "producto": "Mouse",    "cantidad": 15, "precio": 25.50},
]

print("=" * 55)
print("LISTA DE VENTAS ORIGINAL")
print("=" * 55)
for venta in ventas:                        # recorre e imprime cada venta de la lista
    print(venta)


# ============================================================
# PASO 2 - CÁLCULO DE INGRESOS TOTALES
# Se multiplica cantidad * precio de cada venta y se acumulan.
# Ingreso por venta = cantidad vendida × precio unitario
# ============================================================
ingresos_totales = 0                        # acumulador que parte en 0

for venta in ventas:                        # recorre cada venta
    ingreso_venta = venta["cantidad"] * venta["precio"]   # ingreso de esa venta
    ingresos_totales += ingreso_venta       # se suma al acumulador

print("\n" + "=" * 55)
print("INGRESOS TOTALES")
print("=" * 55)
print(f"Ingresos totales generados: ${ingresos_totales:,.2f}")
# :,.2f formatea el número con separador de miles y 2 decimales


# ============================================================
# PASO 3 - ANÁLISIS DEL PRODUCTO MÁS VENDIDO
# Se crea un diccionario "ventas_por_producto" donde:
#   - clave : nombre del producto
#   - valor : cantidad total vendida de ese producto
# Luego se usa max() para encontrar el producto más vendido.
# ============================================================
ventas_por_producto = {}                    # diccionario vacío para acumular cantidades

for venta in ventas:
    producto = venta["producto"]            # nombre del producto de esta venta
    cantidad = venta["cantidad"]            # cantidad vendida en esta venta

    if producto in ventas_por_producto:     # si el producto ya existe en el diccionario
        ventas_por_producto[producto] += cantidad       # se suma la cantidad
    else:                                   # si es la primera vez que aparece
        ventas_por_producto[producto] = cantidad        # se inicializa con su cantidad

# max() con key= busca el producto cuyo valor (cantidad) sea el mayor
producto_mas_vendido = max(ventas_por_producto, key=lambda p: ventas_por_producto[p])

print("\n" + "=" * 55)
print("PRODUCTO MÁS VENDIDO")
print("=" * 55)
print(f"Cantidades por producto: {ventas_por_producto}")
print(f"Producto más vendido   : {producto_mas_vendido}")
print(f"Cantidad total vendida : {ventas_por_producto[producto_mas_vendido]} unidades")


# ============================================================
# PASO 4 - PROMEDIO DE PRECIO POR PRODUCTO
# Se crea "precios_por_producto" donde:
#   - clave : nombre del producto
#   - valor : tupla → (suma_de_precios_totales, cantidad_total_vendida)
# Con esos dos datos se calcula el precio promedio por producto.
# ============================================================
precios_por_producto = {}                   # diccionario vacío para acumular precios

for venta in ventas:
    producto = venta["producto"]
    precio   = venta["precio"]
    cantidad = venta["cantidad"]
    ingreso  = precio * cantidad            # ingreso total de esta línea de venta

    if producto in precios_por_producto:
        suma_anterior, cant_anterior = precios_por_producto[producto]   # desempaqueta la tupla
        precios_por_producto[producto] = (suma_anterior + ingreso, cant_anterior + cantidad)
    else:
        precios_por_producto[producto] = (ingreso, cantidad)            # primera aparición

print("\n" + "=" * 55)
print("PRECIO PROMEDIO POR PRODUCTO")
print("=" * 55)
for producto, (suma_precios, cantidad_total) in precios_por_producto.items():
    promedio = suma_precios / cantidad_total        # precio promedio = ingresos / unidades
    print(f"{producto:10} → Precio promedio: ${promedio:,.2f}")


# ============================================================
# PASO 5 - VENTAS POR DÍA
# Se crea "ingresos_por_dia" donde:
#   - clave : fecha de la venta
#   - valor : ingresos totales generados ese día
# ============================================================
ingresos_por_dia = {}                       # diccionario vacío para acumular por fecha

for venta in ventas:
    fecha   = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]   # ingreso de esta venta

    if fecha in ingresos_por_dia:           # si ya hay registro para ese día
        ingresos_por_dia[fecha] += ingreso  # se acumula
    else:                                   # primer registro del día
        ingresos_por_dia[fecha] = ingreso

print("\n" + "=" * 55)
print("INGRESOS TOTALES POR DÍA")
print("=" * 55)
for fecha, ingreso in ingresos_por_dia.items():
    print(f"{fecha} → ${ingreso:,.2f}")


# ============================================================
# PASO 6 - REPRESENTACIÓN DE DATOS (RESUMEN DE VENTAS)
# Se crea "resumen_ventas" donde:
#   - clave : nombre del producto
#   - valor : diccionario anidado con:
#       * "cantidad_total"   : unidades vendidas en total
#       * "ingresos_totales" : ingresos generados en total
#       * "precio_promedio"  : precio promedio de venta
# Se construye combinando los datos ya calculados en pasos anteriores.
# ============================================================
resumen_ventas = {}                         # diccionario vacío para el resumen final

for producto in ventas_por_producto:        # recorre cada producto ya registrado
    cantidad_total   = ventas_por_producto[producto]                    # del paso 3
    suma_p, cant_p   = precios_por_producto[producto]                   # del paso 4
    ingresos_totales_prod = suma_p                                      # ingresos del producto
    precio_promedio  = suma_p / cant_p                                  # promedio calculado

    resumen_ventas[producto] = {            # diccionario anidado por producto
        "cantidad_total"   : cantidad_total,
        "ingresos_totales" : ingresos_totales_prod,
        "precio_promedio"  : round(precio_promedio, 2)  # redondea a 2 decimales
    }

print("\n" + "=" * 55)
print("RESUMEN DE VENTAS POR PRODUCTO")
print("=" * 55)
for producto, datos in resumen_ventas.items():
    print(f"\n📦 {producto}")
    print(f"   Cantidad total vendida : {datos['cantidad_total']} unidades")
    print(f"   Ingresos totales       : ${datos['ingresos_totales']:,.2f}")
    print(f"   Precio promedio        : ${datos['precio_promedio']:,.2f}")

print("\n" + "=" * 55)
print(f"💰 INGRESOS TOTALES GLOBALES: ${ingresos_totales:,.2f}")
print("=" * 55)
# ============================================================
# Un saludo al Profero Adán, Silvia y toda la gente de forge por esta oportunidad, Atte Thiago De La Quintana