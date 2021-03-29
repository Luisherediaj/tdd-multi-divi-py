import unittest
from calculadora import Calculadora

class TestOperaciones(unittest.TestCase):

    # metodo setUp() para crear la instancia automaticamente 

    def setUp(self):
        self.calc = Calculadora()

    def test_inicial(self):
        calc = Calculadora()
        self.assertEqual(0, calc.value())

    def test_multi(self):
        self.calc.mult(2, 3)
        self.assertEqual(6, self.calc.value)

    def test_divi(self):
        self.calc.divi(15, 3)
        self.assertEqual(5, self.calc.value)