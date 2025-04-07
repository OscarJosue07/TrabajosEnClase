def areaEsfera(radio):
    PI = 3.1416
    return 4 * PI * radio**2

def volumenEsfera(radio):
    PI = 3.1416
    return (4/3) * PI * radio**3

def areaCilindro(radio, altura):
    PI = 3.1416
    return 2 * PI * radio * (radio + altura)

def volumenCilindro(radio, altura):
    PI = 3.1416
    return PI * radio**2 * altura

def areaConoTruncado(radio, altura):
    PI = 3.1416
    return PI * (radio*2 + radio*altura + altura*2)

def volumenConoTruncado(radio, altura):
    PI = 3.1416
    return (1/3) * PI * altura * (radio*2 + radio*altura + altura*2)

radioEsfera = float(input("Ingresa el radio de la esfera: "))
radioCilindro = float(input("Ingresa el radio del cilindro: "))
alturaCilindro = float(input("Ingresa la altura del cilindro: "))
radioConoTruncado = float(input("Ingresa el radio del cono truncado: "))
alturaConoTruncado = float(input("Ingresa la altura del cono truncado: "))

print(f"El area de la esfera es: {areaEsfera(radioEsfera)}")
print(f"El volumen de la esfera es: {volumenEsfera(radioEsfera)}")
print(f"El area del cilindro es: {areaCilindro(radioCilindro, alturaCilindro)}")
print(f"El volumen del cilindro es: {volumenCilindro(radioCilindro, alturaCilindro)}")
print(f"El area del cono truncado es: {areaConoTruncado(radioConoTruncado, alturaConoTruncado)}")
print(f"El volumen del cono truncado es: {volumenConoTruncado(radioConoTruncado, alturaConoTruncado)}")