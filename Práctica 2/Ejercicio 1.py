print("Ingrese el tiempo disponible en segundos: ")
x=int(input())
print("Ingrese el trabajo representado en horas, segundo, minutos")
h=int(input("Ingrese las horas: "))
m=int(input("Ingrese los minutos: "))
s=int(input("Ingrese los segundos: "))
h=h*60*60
m=m*60
z=h+m+s
if z>x:
    print("El trabajo no se puede realizar")
else:
    print("El trabajo se pude realizar")
