#funciones en python

#funciones
def suma(a,b):
    return a + b 

def potencia (a,b):
    return a**b

def multiplicar (a,b):
    return a*b

def restar (a,b):
    return a-b

#Operaciones Aritmeticas
print("Operaciones Aritmeticas")
x=int(input("a:  "))
y=int(input("b:  "))

#s=suma(x,y)
print(f"{x}+{y}={suma(x,y)}")

#s=suma(x,y)
print(x,"+",y,"=",suma(x,y))

#p=potencia(x,y)
print(f"{x}^{y}={potencia(x,y)}")

#m=multiplicar(x,y)
print(f"{x}*{y}={multiplicar(x,y)}")

#r=restar(x,y)
print(f"{x}-{y}={restar(x,y)}")
