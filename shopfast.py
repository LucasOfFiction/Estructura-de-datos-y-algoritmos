# shopfast_interactivo.py
# AUTOR: LUCAS KRIGER

class Cliente:
    def __init__(self, rut, nombre, correo, telefono):
        self.rut = rut
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} ({self.rut})"


class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.codigo} - {self.nombre} | ${self.precio} | Stock: {self.stock}"


class Pedido:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.items = {}  # codigo -> {producto, cantidad}
        self.productos = productos

    def agregar_producto(self, producto, cantidad):
        if cantidad <= producto.stock:
            if producto.codigo in self.items:
                self.items[producto.codigo]["cantidad"] += cantidad
            else:
                self.items[producto.codigo] = {"producto": producto, "cantidad": cantidad}
            producto.stock -= cantidad
            print(f" {cantidad} x {producto.nombre} agregado al pedido.")
            return True
        else:
            print(f" Stock insuficiente para {producto.nombre}. Disponible: {producto.stock}")
            return False

    def calcular_total(self):
        total = 0
        for item in self.items.values():
            total += item["producto"].precio * item["cantidad"]
        return total

    def __str__(self):
        detalle = ""
        for item in self.items.values():
            prod = item["producto"]
            cant = item["cantidad"]
            detalle += f"{prod.nombre} x{cant} = ${prod.precio * cant}\n"
        return f"--- RESUMEN DEL PEDIDO ---\nCliente: {self.cliente}\n{detalle}\nTOTAL: ${self.calcular_total()}"


# ====== Sistema ======
productos = {
    "P001": Producto("P001", "Laptop", 1200, 5),
    "P002": Producto("P002", "Mouse", 20, 15),
    "P003": Producto("P003", "Teclado", 50, 10),
}


def iniciar_compra():
    print("=== Bienvenido a ShopFast ===")

    # 1. Ingresar datos del cliente
    rut = input("Ingrese RUT del cliente con dígito verificador: ")
    nombre = input("Ingrese el nombre completo del cliente: ")
    correo = input("Ingrese el correo electrónico del cliente: ")
    telefono = input("Ingrese el número de teléfono del cliente: ")
    cliente = Cliente(rut, nombre, correo, telefono)

    pedido = Pedido(cliente, productos)
    while True:
        # Mostrar catálogo actualizado al inicio del ciclo
        print("\n--- Lista de productos disponibles ---")
        for prod in productos.values():
            print(f"{prod.codigo} - {prod.nombre} | ${prod.precio} | Stock: {prod.stock}")

        codigo = input("\nIngrese código del producto a comprar: ").upper()
        if codigo not in productos:
            print(" Producto no encontrado.")
            continue

        try:
            cantidad = int(input(f"Ingrese cantidad de {productos[codigo].nombre}: "))
        except ValueError:
            print(" Debe ingresar un número válido.")
            continue

        if cantidad > productos[codigo].stock:
            print(" No hay suficiente stock disponible.")
            continue

        pedido.agregar_producto(productos[codigo], cantidad)
        productos[codigo].stock -= cantidad  # actualizar stock real
        print(f" {cantidad} x {productos[codigo].nombre} agregado al pedido.")

        # Preguntar si quiere seguir
        opcion = input(
            "\n--- ¿Desea agregar otro producto al carrito? ---\n"
            "(Ingresa 'ok' para continuar o escriba 'fin' para terminar): "
        ).strip().lower()
        if opcion == "fin":

            # 4. Mostrar resumen final
            print(pedido)
            print("\n Pedido registrado con éxito. Gracias por su compra.")
        break


if __name__ == "__main__":
    iniciar_compra()
