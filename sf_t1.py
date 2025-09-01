#Test 1 → agregar productos y calcular total.
import unittest
from shopfast import Cliente, Producto

class TestShopFastClienteProducto(unittest.TestCase):

    def test_cliente(self):
        cliente = Cliente("12345678-9", "Lucas Kriger", "lucas@email.com", "999999999")
        self.assertEqual(cliente.rut, "12345678-9")
        self.assertEqual(cliente.nombre, "Lucas Kriger")
        self.assertEqual(cliente.correo, "lucas@email.com")
        self.assertEqual(cliente.telefono, "999999999")

    def test_producto(self):
        producto = Producto("P001", "Laptop", 1200, 5)
        self.assertEqual(producto.codigo, "P001")
        self.assertEqual(producto.nombre, "Laptop")
        self.assertEqual(producto.precio, 1200)
        self.assertEqual(producto.stock, 5)

if __name__ == "__main__":
    unittest.main()