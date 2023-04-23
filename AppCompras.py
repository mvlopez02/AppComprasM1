# Definir los productos y sus precios 
products = {"brownie": 4500, "galleta chocochip": 3000, "galleta arequipe": 2500, "torta zanahoria":5000}

# Muestra el menú
print("Bienvenido a la pastelería Baked! Este es nuestro menú:")
for product, price in products.items():
    print(f"{product.capitalize()}: ${price}")

# Le pregunta al usuario su orden
order = {}
while True:
    product = input("Ingrese el nombre del producto que desea ordenar (o 'fin' para finalizar su compra): ").lower()
    if product == "fin":
        break
    if product not in products:
        print("Lo sentimos, ese producto no se encuentra en nuestro menú.")
        continue
    quantity = int(input("Ingrese la cantidad que desea"))
    order[product] = order.get(product, 0) + quantity

# Muestra el resumen de la orden
print("Resumen de la compra:")
total_cost = 0
for product, quantity in order.items():
    price = products[product]
    cost = price * quantity
    total_cost += cost
    print(f"{quantity} x {product.capitalize()} (${price}): ${cost}")
print(f"El costo total de su compra es de: ${total_cost}")

# Pregunta al usuario si desea aprobar o cancelar la orden
while True:
    response = input("Desea confirmar su compra? Escriba (aceptar/cancelar) ").lower()
    if response == "aceptar":
        print("Su orden ha sido aprobada. Gracias por su compra!")
        break
    elif response == "cancelar":
        print("La orden ha sido cancelada.")
        break
    else:
        print("La respuesta inválida. Ingrese únicamente 'aceptar' o 'cancelar'.")
