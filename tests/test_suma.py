import unittest

"""
*** Cobertura Básica de Funciones ***
1. Escribe un conjunto de pruebas unitarias para la función suma() de la calculadora.
2. Usa pytest para ejecutar las pruebas y utiliza coverage.py para verificar que la cobertura de código sea del 100%."
"""

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    
    def test_positive_add(self):
        self.assertEqual(add(3, 5), 8)

    def test_negative_add(self):
        self.assertEqual(add(-3, -5), -8)

    def test_mixed_add(self):
        self.assertEqual(add(10, -3), 7)

    def test_zero_add(self):
        self.assertEqual(add(0, 0), 0)