# --- App de Paletas (Versión Consola) ---

productos = {
    "Fresa 🍓": 25.0,
    "Chocolate 🍫": 25.0,
    "Limón 🍋": 23.0,
    "Vainilla 🌼": 25.0,
    "Mango 🥭": 25.0
}

print("--- 🍦 BIENVENIDO A PALETERÍA TORRES ---")
print("Catálogo de precios:")
for nombre, precio in productos.items():
    print(f"{nombre}: ${precio}")

print("\n--- 🧮 PRESUPUESTO ---")
total = 0

for nombre, precio in productos.items():
    try:
        cantidad = int(input(f"¿Cuántas paletas de {nombre} quieres? "))
        total += cantidad * precio
    except ValueError:
        print("Por favor, ingresa solo números.")

print("\n" + "="*30)
print(f"💰 EL TOTAL DE TU PEDIDO ES: ${total:.2f}")
print("="*30)
