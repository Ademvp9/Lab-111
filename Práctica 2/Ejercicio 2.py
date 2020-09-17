print("en base a la fórmula cuadrática ax+bx+c, ingrese a,b,c respectivamente")
a=int(input("ingrese a:"))
b=int(input("ingrese b:"))
c=int(input("ingrese c:"))
d=(b*b)-(4*a*c)
if d>0:
    print("La ecuación tiene dos soluciones distintas.")
elif d==0:
    print("La ecuación tiene una única solución.")
else:
    print("La ecuación no tiene una solución real")
