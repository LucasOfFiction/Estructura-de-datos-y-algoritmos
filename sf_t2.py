#Test 2 → validación de stock
import unittest
from shopfast import Cliente, Producto, Pedido

class TestPedidoStock(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente("22.222.222-2", "María López", "maria@mail.com", "987654321")
        self.prod1 = Producto("P001", "Laptop", 1200, 1)  # Solo hay 1 en stock
        self.pedido = Pedido(self.cliente, {self.prod1.codigo: self.prod1})

    def test_agregar_producto_stock_insuficiente(self):
        resultado = self.pedido.agregar_producto(self.prod1, 2)  # intenta comprar más del stock
        self.assertFalse(resultado)
        self.assertEqual(self.prod1.stock, 1)  # stock no cambia

    def test_agregar_producto_stock_disponible(self):
        resultado = self.pedido.agregar_producto(self.prod1, 1)
        self.assertTrue(resultado)
        self.assertEqual(self.prod1.stock, 0)

if __name__ == "__main__":
    unittest.main()
