from src.EcuacionSegundoGrado import EcuacionSegundoGrado

if __name__ == "__main__":
    print("Ingrese los tres coeficientes de su ecuación de segundo grado en orden: ")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    ecuacionSegundoGrado = EcuacionSegundoGrado([a, b, c])
    raiz1, raiz2 = ecuacionSegundoGrado.calcular_raices()
    print(f"Las raíces de la ecuación son: {raiz1}, {raiz2}")