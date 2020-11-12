#Nombre: Adhemar Vidal Pacajes Pabón     C.I.: 13280760


def operacion_1(a,b):
    d=0
    for a in range(a,b+1,a):
        d=d+1
    r=b-a
    print("EL resultado es: ", d)
    print("El residuo de la divison es: ", r)
def operacion_2(a):
    for i in range(1,a+1):
        m=i
        while m<a:
            m=m+i
        r=a-m
        if r==0:
            print(i)
def operacion_3(a):
    m=0
    n=3
    while n<=len(a):
        c=a[m:n]
        print(c)
        if c==c[::-1]:
            print("Si es capicua")
        else:
            print("no es capicua")
        m+=1
        n+=1
def operacion_4(n,d):
    aux1=n
    R=0
    cb=""
    while n>=d:
        for i in range(d,n+1,d):
            R=R+1
        rd=n-i
        cb=cb+str(rd)
        n=R
        aux=R
        R=0
    cb=cb+str(aux)
    cb=cb[::-1]
    print(aux1, "en base",d, "es igual a: ",cb)

usuario="lab111"
contrasena="prac111"
intento_us=input("Ingrese el usuario: ")
while intento_us!=usuario:
    print("El usuario no existe.")
    intento_us=input("Vuelva a intentarlo: ")
intento_con=input("Ingrese la contraseña: ")
while intento_con!=contrasena:
    print("La contraseña es incorrecta.")
    intento_con=input("Vuelva a intentarlo: ")

print("\n\tBIENVENIDO")
print("\n\tElija una operación")
menu=True
while menu==True:
    print("\n\t1.- Division de dos números")
    print("\t2.- Divisores de un número")
    print("\t3.- Números Capicua")
    print("\t4.- Cambio de base")
    print("\t5.- Salir")

    selector=int(input(""))
    if selector ==1:
        print("Eligió la primera operacion: ")
        b=int(input("\nIngrese el dividendo: "))
        a=int(input("Ingrese el divisor: "))
        while a>b:
            a=int(input("El divisor debe ser menor que el dividendo: "))
        operacion_1(a,b)
        print("\nEl ejercicio terminó, por favor, vuelva a elegir una opción.")
    elif selector ==2:
        print("Eligió la segunda operacion: ")
        a=int(input("Ingrese un número para hallar sus divisores: "))
        print("Los divisores de",a,"son:")
        operacion_2(a)
        print("\nEl ejercicio terminó, por favor, vuelva a elegir una opción.")
    elif selector ==3:
        print("Eligió la tercera operacion: ")
        a=input("Ingrese los números: ")
        operacion_3(a)
        print("\nEl ejercicio terminó, por favor, vuelva a elegir una opción.")
    elif selector ==4:
        print("Eligió la cuarta operacion: ")
        n=int(input("Ingrese un número: "))
        d=int(input("Ingrese el número de la base: "))
        while d>=10:
            d=int(input("Por favor, ingrese una base menor a 10: "))
        operacion_4(n,d)
        print("\nEl ejercicio terminó, por favor, vuelva a elegir una opción.")
    elif selector==5:
        print("Usted salio del programa.")
        menu=False
    else:
        print("Número incorrecto. Vuelva a elegir una opción")
