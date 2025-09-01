# shopfast_interactivo.py
# AUTOR: LUCAS KRIGER


#Clase cliente donde luego se instanciaran los datos para ingresarlos mediante inputs en iniciar_compra
class Cliente:
    def __init__(self, rut, nombre, correo, telefono):
        self.rut = rut
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} ({self.rut})" #str logra que al imprimir el objeto muestre nombre y rut en formato legible

#clase producto para poder instanciarlos mediante inputs en iniciar_compra
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.codigo} - {self.nombre} | ${self.precio} | Stock: {self.stock}"

#clase pedido para manejar los productos agregados y calcular total
class Pedido:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.items = {}  # codigo -> {producto, cantidad}
        self.productos = productos
    # Agrega producto al pedido y descuenta stock
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
    # Calcula el total del pedido   
    def calcular_total(self):
        total = 0
        for item in self.items.values():
            total += item["producto"].precio * item["cantidad"]
        return total
    # Formatea el resumen del pedido
    def __str__(self):
        detalle = ""
        for item in self.items.values():
            prod = item["producto"]
            cant = item["cantidad"]
            detalle += f"{prod.nombre} x{cant} = ${prod.precio * cant}\n"
        return f"--- RESUMEN DEL PEDIDO ---\nCliente: {self.cliente}\n{detalle}\nTOTAL: ${self.calcular_total()}"


# ====== Sistema Catalogo======
productos = {
    "P001": Producto("P001", "Laptop", 1200, 5),
    "P002": Producto("P002", "Mouse", 20, 15),
    "P003": Producto("P003", "Teclado", 50, 10),
}


def iniciar_compra():
    print("=== Bienvenido a ShopFast ===")

    # 1. Ingresar datos del cliente mediate inputs en la terminal
    rut = input("Ingrese RUT del cliente con dígito verificador: ")
    nombre = input("Ingrese el nombre completo del cliente: ")
    correo = input("Ingrese el correo electrónico del cliente: ")
    telefono = input("Ingrese el número de teléfono del cliente: ")
    cliente = Cliente(rut, nombre, correo, telefono)

    pedido = Pedido(cliente, productos) #2 Instancia pedido con el cliente y el catálogo de productos para poder acceder a stock
    while True:
        #3 Muestra catálogo de productos actualizado al inicio del ciclo 
        print("\n--- Lista de productos disponibles ---")
        for prod in productos.values():
            print(f"{prod.codigo} - {prod.nombre} | ${prod.precio} | Stock: {prod.stock}")

        codigo = input("\nIngrese código del producto a comprar: ").upper() #se accede al producto por su código mediante inputs
        if codigo not in productos:
            print(" Producto no encontrado.")
            continue

        try:
            cantidad = int(input(f"Ingrese cantidad de {productos[codigo].nombre}: ")) #recorre el diccionario productos para acceder al nombre del producto
        except ValueError:
            print(" Debe ingresar un número válido.")
            continue

        #4 Agregar al pedido (el método ya descuenta stock)
        pedido.agregar_producto(productos[codigo], cantidad)

        #5 Preguntar si desea agregar otro producto
        opcion = input(
            "\n--- ¿Desea agregar otro producto al carrito? ---\n"
            "(Ingresa 'ok' para continuar o escriba 'no' para terminar): "
        ).strip().lower()

        if opcion == "no":
            break
        else:
            continue

# 4. Mostrar resumen final
    print(pedido)
    print("\n Pedido registrado con éxito. Gracias por su compra.")

if __name__ == "__main__":
    iniciar_compra()
