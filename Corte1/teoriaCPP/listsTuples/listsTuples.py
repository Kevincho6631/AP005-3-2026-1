# =========================================
# 🔹 MANEJO DE LISTAS EN PYTHON
# =========================================

# Lista inicial de colores
colores = ["Rojo", "Azul", "Amarillo", "Naranja", "Violeta", "Verde"]

print("Lista original:", colores)
print("Tipo de dato:", type(colores))

# Acceso a elementos
print("Tercer elemento:", colores[2])

# Tamaño de la lista
print("Cantidad de elementos:", len(colores))

# Sublistas (slicing)
print("Primeros dos elementos:", colores[:2])
print("Desde índice 1 hasta 3:", colores[1:4])


# =========================================
# 🔹 MODIFICACIÓN DE LISTAS
# =========================================

# Agregar elemento al final
colores.append("Blanco")
print("\nDespués de append:", colores)

# Insertar en posición específica
colores.insert(3, "Negro")
print("Después de insert:", colores)

# Agregar múltiples elementos
colores.extend(["Marrón", "Gris"])
print("Después de extend:", colores)

# Buscar posición
print("Índice de Azul:", colores.index("Azul"))

# Eliminar elemento
colores.remove("Marrón")
print("Después de remove:", colores)

# Eliminar último elemento
ultimo = colores.pop()
print("Elemento eliminado:", ultimo)
print("Lista actual:", colores)

# Repetir lista
colores_repetidos = colores * 2
print("Lista duplicada:", colores_repetidos)


# =========================================
# 🔹 ORDENAMIENTO
# =========================================

print("\nOrdenando lista...")

# Ordena la lista directamente
colores.sort()
print("Orden ascendente:", colores)

# Lista numérica
numeros = [10, 3, 5, 8, 1, 9]

numeros.sort()
print("Números ordenados:", numeros)

numeros.sort(reverse=True)
print("Números descendentes:", numeros)


# =========================================
# 🔹 TUPLAS
# =========================================

print("\n==============================")
print("        TUPLAS")
print("==============================")

# Convertir lista a tupla
colores_tupla = tuple(colores)
print("Tupla de colores:", colores_tupla)

# Acceso a elementos
print("Primer elemento:", colores_tupla[0])

# Verificar existencia
print("¿Está 'Rojo'?:", "Rojo" in colores_tupla)

# Contar ocurrencias
print("Veces que aparece 'Rojo':", colores_tupla.count("Rojo"))


# =========================================
# 🔹 TUPLAS ESPECIALES
# =========================================

# Tupla de un solo elemento (importante la coma)
tupla_unitaria = ("Blanco",)
print("Tupla unitaria:", tupla_unitaria)

# Empaquetado automático
datos = "Carlos", 15, 7, 2000
print("Tupla empaquetada:", datos)

# Desempaquetado
nombre, dia, mes, anio = datos

print("\nDatos separados:")
print("Nombre:", nombre)
print("Día:", dia)
print("Mes:", mes)
print("Año:", anio)


# =========================================
# 🔹 CONVERSIONES
# =========================================

# Convertir tupla a lista
lista_desde_tupla = list(datos)
print("\nLista desde tupla:", lista_desde_tupla)
