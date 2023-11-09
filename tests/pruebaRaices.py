import unittest
from src.EcuacionSegundoGrado import EcuacionSegundoGrado, ExceptionDatos

class PruebaRaices(unittest.TestCase):
    def setUp(self):
        self.ecuacionSegundoGrado = EcuacionSegundoGrado([])
    def tearDown(self):
        self.ecuacionSegundoGrado = None

    def test_TresCoeficientesEnteros_retornaRaicesReales(self):
        self.ecuacionSegundoGrado.coeficientes = []

        # Arrange
        self.ecuacionSegundoGrado.coeficientes = [3, -5, 1]
        raiz1 = 1.43
        raiz2 = 0.23

        # Do
        raiz1Actual,  raiz2Actual = self.ecuacionSegundoGrado.calcular_raices()

        # Assert
        self.assertAlmostEqual(raiz1Actual, raiz1, places=2)
        self.assertAlmostEqual(raiz2Actual, raiz2, places=2)

