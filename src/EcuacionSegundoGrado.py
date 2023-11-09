import cmath

class ExceptionDatos(Exception):
    pass

class EcuacionSegundoGrado:
    def __init__(self, coeficientes):
        if coeficientes is not None:
            self.__coeficientes = self.validarCoeficientes(coeficientes)
        else:
            raise ExceptionDatos("Se requieren tres coeficientes.")

    def validarCoeficientes(self, coeficientes):
        if coeficientes is not None:
            if len(coeficientes) != 3:
                raise ExceptionDatos("Se requieren tres coeficientes.")
            for coeficiente in coeficientes:
                if not isinstance(coeficiente, (int, float)):
                    raise ExceptionDatos("Los coeficientes deben ser números.")
            return coeficientes
        else:
            raise ExceptionDatos("Se requieren tres coeficientes.")

    @property
    def coeficientes(self):
        return self.__coeficientes

    @coeficientes.setter
    def coeficientes(self, coeficientes):
        try:
            self.__coeficientes = self.validarCoeficientes(coeficientes)
        except ExceptionDatos as e:
            raise e

    def calcular_raices(self):
        a, b, c = self.__coeficientes

        # Calcula el discriminante
        discriminante = b**2 - 4*a*c

        # Comprueba el tipo de raíces
        if discriminante > 0:
            # Dos raíces reales diferentes
            raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a)
            raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a)
            return raiz1, raiz2

        elif discriminante == 0:
            # Una raíz real (raíz doble)
            raiz = -b / (2*a)
            return raiz, raiz
        else:
            # Dos raíces complejas conjugadas
            raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a)
            raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a)
            return raiz1, raiz2