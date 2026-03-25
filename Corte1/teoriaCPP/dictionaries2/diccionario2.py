# =========================================
# 🔹 ACCESO Y MANEJO DE DICCIONARIOS
# =========================================

# 📌 Base de datos de edificios (altura en metros)
edificios = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte Tower": 554.5,
    "One World Trade": 541.3
}

# 🔍 Acceso directo a valores
print("Altura Burj Khalifa:", edificios["Burj Khalifa"])
print("Altura Ping An:", edificios["Ping An"])


# =========================================
# 🔹 DICCIONARIO CON LISTAS
# =========================================

elementos = {
    "agua": ["Cancer", "Scorpio", "Pisces"],
    "fuego": ["Aries", "Leo", "Sagittarius"],
    "tierra": ["Taurus", "Virgo", "Capricorn"],
    "aire": ["Gemini", "Libra", "Aquarius"]
}

print("\nSignos de tierra:", elementos["tierra"])


# =========================================
# 🔹 ACCESO SEGURO (SIN ERRORES)
# =========================================

clave = "Empire Tower"

# ✔ Forma segura usando condición
if clave in edificios:
    print(edificios[clave])
else:
    print(f"⚠️ {clave} no está registrado")


# ✔ Forma pro usando get()
altura = edificios.get("Mi Casa", "No disponible")
print("Consulta segura:", altura)


# =========================================
# 🔹 USO INTELIGENTE DE GET()
# =========================================

usuarios = {
    "devMaster": 101,
    "codeGirl": 202,
    "loopKing": 303
}

# Obtener con valor por defecto
user_id = usuarios.get("devMaster", 0)
print("\nID usuario:", user_id)

# Caso donde no existe
nuevo_id = usuarios.get("usuarioX", 999)
print("ID por defecto:", nuevo_id)


# =========================================
# 🔹 ELIMINACIÓN CONTROLADA (POP)
# =========================================

premios = {
    1: "Laptop",
    2: "Audífonos",
    3: "Mouse",
    4: "Teclado"
}

# Eliminar elemento existente
premio = premios.pop(3, "Sin premio")
print("\nPremio obtenido:", premio)

# Intentar eliminar uno inexistente
premio = premios.pop(10, "Sin premio")
print("Intento inválido:", premio)

print("Premios restantes:", premios)


# =========================================
# 🔹 CASO PRÁCTICO (VIDEOJUEGO)
# =========================================

inventario = {
    "pocion": 10,
    "elixir": 20,
    "pan": 5
}

vida = 50

# Consumir items (si existen)
vida += inventario.pop("pocion", 0)
vida += inventario.pop("pan", 0)
vida += inventario.pop("objetoX", 0)

print("\nInventario actual:", inventario)
print("Vida total:", vida)


# =========================================
# 🔹 CLAVES, VALORES E ITEMS
# =========================================

notas = {
    "Ana": [80, 90, 85],
    "Luis": [70, 60, 75],
    "Sofia": [95, 92, 98]
}

# 🔑 Obtener claves
print("\nEstudiantes:", list(notas.keys()))

# 🔢 Recorrer valores
print("\nNotas:")
for lista_notas in notas.values():
    print(lista_notas)


# =========================================
# 🔹 SUMA DE VALORES
# =========================================

ejercicios = {
    "funciones": 10,
    "listas": 15,
    "loops": 20
}

total = sum(ejercicios.values())
print("\nTotal ejercicios:", total)


# =========================================
# 🔹 RECORRIDO COMPLETO
# =========================================

empresas = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80
}

print("\nValor de empresas:")
for nombre, valor in empresas.items():
    print(f"{nombre} vale {valor} billones USD")


# =========================================
# 🔹 OTRO EJEMPLO REAL
# =========================================

ocupaciones = {
    "Ingeniero": 30,
    "Doctor": 45,
    "Abogado": 40
}

print("\nParticipación femenina:")
for trabajo, porcentaje in ocupaciones.items():
    print(f"{porcentaje}% en {trabajo}")
