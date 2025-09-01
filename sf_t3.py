#Test 3 → formato del resumen del pedido
import unittest
from shopfast import Cliente, Producto, Pedido

class TestPedidoResumen(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("33.333.333-3", "Pedro Gómez", "pedro@mail.com", "555555555")
        self.prod1 = Producto("P001", "Laptop", 1200, 5)
        self.prod2 = Producto("P002", "Mouse", 20, 10)
        self.pedido = Pedido(self.cliente, {self.prod1.codigo: self.prod1, self.prod2.codigo: self.prod2})

    def test_resumen_pedido(self):
        self.pedido.agregar_producto(self.prod1, 1)
        self.pedido.agregar_producto(self.prod2, 2)
        resumen = str(self.pedido)

        self.assertIn("Laptop x1 = $1200", resumen)
        self.assertIn("Mouse x2 = $40", resumen)
        self.assertIn("TOTAL: $1240", resumen)

if __name__ == "__main__":
    unittest.main()
