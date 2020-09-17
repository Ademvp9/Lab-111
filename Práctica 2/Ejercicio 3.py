h=int(input("Ingrese las horas:"))
m=int(input("Ingrese las minutos:"))
s=int(input("Ingrese las segundos:"))
s=s+1
if s>59:
    m=m+1
    s=0
    if m>59:
        h=h+1
        m=0
        if h>23:
            h=0
        else:
            pass
print(h,"Horas")
print(m,"Minutos")
print(s,"Segundos")
