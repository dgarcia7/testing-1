import unittest

"""
*** Cobertura Básica de Funciones ***
1. Escribe un conjunto de pruebas unitarias para la función suma() de la calculadora.
2. Usa pytest para ejecutar las pruebas y utiliza coverage.py para verificar que la cobertura de código sea del 100%."
"""

def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    
    def test_positive_suma(self):
        self.assertEqual(suma(3, 5), 8)

    def test_negative_suma(self):
        self.assertEqual(suma(-3, -5), -8)

    def test_mixed_suma(self):
        self.assertEqual(suma(10, -3), 7)

    def test_zero_suma(self):
        self.assertEqual(suma(0, 0), 0)