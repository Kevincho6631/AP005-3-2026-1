# =========================================
# 🔹 SISTEMA DE PRUEBA CON DICCIONARIOS
# =========================================

# 📌 Diccionarios base
temperaturas = {
    "sala": 21,
    "cocina": 23,
    "habitacion": 20,
    "despensa": 22
}

camaras = {
    "patio": 6,
    "garaje": 2,
    "entrada": 1
}

print("🌡️ Temperaturas:", temperaturas)
print("📷 Cámaras:", camaras)


# =========================================
# 🔹 TRADUCCIONES
# =========================================

diccionario_traduccion = {
    "mountain": "orod",
    "bread": "bass",
    "friend": "mellon",
    "horse": "roch"
}

print("\n📖 Traducciones:")
for palabra, traduccion in diccionario_traduccion.items():
    print(f"{palabra} → {traduccion}")


# =========================================
# 🔹 DICCIONARIO CON LISTAS
# =========================================

familias = {
    "Von Trapp": ["Johannes", "Rosmarie", "Eleonore"],
    "Corleone": ["Sonny", "Fredo", "Michael"]
}

print("\n👨‍👩‍👧 Familias:", familias)


# =========================================
# 🔹 MENÚ (CRUD BÁSICO)
# =========================================

menu = {
    "avena": 3,
    "tostada": 6,
    "jugo": 5,
    "muffin": 2
}

print("\n🍽️ Menú inicial:", menu)

# ➕ Agregar elemento
menu["cheesecake"] = 8

# 🔄 Modificar valor
menu["avena"] = 4

print("🍽️ Menú actualizado:", menu)


# =========================================
# 🔹 USO DE MÉTODOS ÚTILES
# =========================================

# 🔍 Buscar con get (evita errores)
precio = menu.get("tostada", "No existe")
print("\nPrecio de tostada:", precio)

# ❌ Eliminar elemento
menu.pop("muffin", None)

print("Menú sin muffin:", menu)


# =========================================
# 🔹 ACTUALIZACIÓN MASIVA
# =========================================

temperaturas.update({
    "patio": 30,
    "oficina": 25
})

print("\n🌡️ Nuevas temperaturas:", temperaturas)


# =========================================
# 🔹 CREACIÓN CON ZIP
# =========================================

nombres = ["Ana", "Luis", "Pedro", "Sofia"]
edades = [20, 25, 22, 19]

personas = dict(zip(nombres, edades))

print("\n👥 Personas:", personas)


# =========================================
# 🔹 COMPRENSIÓN DE DICCIONARIOS
# =========================================

cuadrados = {x: x**2 for x in range(1, 6)}
print("\n🔢 Cuadrados:", cuadrados)


# =========================================
# 🔹 DICCIONARIO ANIDADO
# =========================================

biblioteca = {
    "musica": {
        "Imagine": 44,
        "Respect": 94
    },
    "peliculas": {}
}

print("\n🎬 Biblioteca:", biblioteca)


# =========================================
# 🔹 RECORRIDO COMPLETO
# =========================================

print("\n📊 Recorrido de menú:")
for item, precio in menu.items():
    print(f"{item}: ${precio}")
