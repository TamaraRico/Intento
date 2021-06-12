import math
import numpy as np
respuesta = 9
repetir= True
def angulo_2_planos():
#angulo entre dos planos
    u = []
    v= []
    for i in range(3):
        valor = input("introduce valor: {} de U\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        u.append(valor)
    for i in range(3):
        valor = ("introduce valor: {} de V\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        v.append(valor)
    i = 0
    den = 0
    lul = 0
    lvl = 0
    while i < 3:
      den += u[i]*v[i]
      lul += u[i]**2
      lvl += v[i]**2
      i += 1
    lul = math.sqrt(lul)
    lvl = math.sqrt(lvl)
    ang = np.arccos(den/(lul*lvl))
    print("El angulo con dos ecuaciones es:", ang)

def dos_rectas_paramericas():
# Dos rectas parametricas
    px = []
    u = []
    a= []
    for i in range(3):
        valor = input("introduce valor: {} de U\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        u.append(valor)
    for i in range(3):
        valor = input("introduce valor: {} de a\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        a.append(valor)
    u1 = []
    a1= []
    for i in range(3):
        valor = input("introduce valor: {} de U1\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        u1.append(valor)
    for i in range(3):
        valor = input("introduce valor: {} de a1\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        a1.append(valor)
    px.append((u[1]*u1[2])-(u[2]*u1[1]))
    px.append((u[2]*u1[0])-(u[0]*u1[2]))
    px.append((u[0]*u1[1])-(u[1]*u1[0]))

    i = 0
    lpxl = 0
    an = []
    pp = 0
    while i < 3:
      an.append(a[i]-a1[i])
      lpxl += px[i]**2
      pp += (an[i]*px[i])
      i += 1
    lpxl = math.sqrt(lpxl)
    res=pp/lpxl
    print("La distancia con dos ecuaciones es:",res)
def angulo_3_puntos():
#angulo por 3 puntos
    p = []
    q = []
    r = []
    for i in range(3):
        valor = input("introduce valor: {} de p\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        p.append(valor)
    for i in range(3):
        valor = input("introduce valor: {} de q\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        q.append(valor)
    for i in range(3):
        valor = input("introduce valor: {} de r\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        r.append(valor)
    p1 = []
    q1 = []
    r1 = []
    for i in range(3):
        valor = input("introduce valor: {} de p1\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        p1.append(valor)
    for i in range(3):
        valor = input("introduce valor: {} de q1\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        q1.append(valor)
    for i in range(3):
        valor = input("introduce valor: {} de r1\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        r1.append(valor)
    pq=[]
    pr=[]
    pq1=[]
    pr1=[]
    i=0
    while i<3:
      pq.append(q[i]-p[i])
      pr.append(r[i]-p[i])
      pq1.append(q1[i]-p1[i])
      pr1.append(r1[i]-p1[i])
      i += 1
    n=[]
    n1 = []
    n.append((pq[1]*pr[2])-(pq[2]*pr[1]))
    n.append((pq[2]*pr[0])-(pq[0]*pr[2]))
    n.append((pq[0]*pr[1])-(pq[1]*pr[0]))
    n1.append((pq1[1]*pr1[2])-(pq1[2]*pr1[1]))
    n1.append((pq1[2]*pr1[0])-(pq1[0]*pr1[2]))
    n1.append((pq1[0]*pr1[1])-(pq1[1]*pr1[0]))

    u = n
    v = n1

    i = 0
    den = 0
    lul = 0
    lvl = 0
    while i < 3:
      den += u[i]*v[i]
      lul += u[i]**2
      lvl += v[i]**2
      i += 1
    lul = math.sqrt(lul)
    lvl = math.sqrt(lvl)
    ang = np.arccos(den/(lul*lvl))
    print("El angulo cuando tienes 3 putnos es:", ang)

def dospuntos_dosrectas():
# De dos puntos a distancia entre dos rectas
    p1 = []
    p2= []
    for i in range(3):
        valor = input("introduce valor: {} de p1\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        p1.append(valor)
    for i in range(3):
        valor = input("introduce valor: {} de p2\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        p2.append(valor)
    u = []
    a = []
    u1 = []
    a1= []
    for i in range(3):
        valor = input("introduce valor: {} de u1\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        u1.append(valor)
    for i in range(3):
        valor = input("introduce valor: {} de a1\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        a1.append(valor)
    px = []
    i = 0
    while i<3:
      u.append(-p1[i]+p2[i])
      a.append(p1[i])
      i += 1
    #aqui intenta sacar el producto
    px.append((u[1]*u1[2])-(u[2]*u1[1]))
    px.append((u[2]*u1[0])-(u[0]*u1[2]))
    px.append((u[0]*u1[1])-(u[1]*u1[0]))

    i = 0
    lpxl = 0
    an = []
    pp = 0
    while i < 3:
      an.append(a[i]-a1[i])
      lpxl += px[i]**2
      pp += (an[i]*px[i])
      i += 1
    lpxl = math.sqrt(lpxl)
    res=abs(pp/lpxl)
    print("La distancia con dos puntos y la recta es: ",res)

def perpendicular():
# Perperndicular
    l1 = []
    l2= []
    for i in range(3):
        valor = input("introduce valor: {} de l1\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        l1.append(valor)
    for i in range(3):
        valor = input("introduce valor: {} de l2\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        l2.append(valor)
    #En este caso lista tres son los valores de la ecuacion perpednicular
    l3= []
    for i in range(3):
        valor = input("introduce valor: {} de l3 (ecuacion perpendicular)\t".format(i))
        if valor == "s":
            return
        valor = float(valor)
        l3.append(valor)
    l4 = []
    i = 0
    while i < 3:
      l4.append(l1[i]-l2[i])
      i += 1
    px = []
    px.append((l3[1]*l4[2])-(l3[2]*l4[1]))
    px.append((l3[2]*l4[0])-(l3[0]*l4[2]))
    px.append((l3[0]*l4[1])-(l3[1]*l4[0]))

    con = (px[0]*(-l1[0]))+(px[1]*(-l1[1]))+(px[2]*(-l1[2]))
    con = -con
    a=con/px[0]
    b=con/px[1]
    c=con/px[2]
    print(" De ejercicio perpendicular: A es: ",a, "B es: ", b, "C es: ", c)

def tres_puntos():
    #3 puntos
    l1 = []
    l2 = []
    l3 = []
    for i in range(3):
        valor = input("introduce valor: {} de l1\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        l1.append(valor)
    for i in range(3):
        valor = input("introduce valor: {} de l2\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        l2.append(valor)
    for i in range(3):
        valor = input("introduce valor: {} de l3\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        l3.append(valor)
    u = []
    v = []
    px = []
    for i in range(3):
        px.append(0)
    i = 0
    while i < 3:
      u.append(l2[i]-l1[i])
      v.append(l3[i]-l1[i])
      i += 1

    px[0] = ((u[1]*v[2])-(u[2]*v[1]))
    px[1] = ((u[2]*v[0])-(u[0]*v[2]))
    px[2] = ((u[0]*v[1])-(u[1]*v[0]))

    con = (px[0]*(-l1[0]))+(px[1]*(-l1[1]))+(px[2]*(-l1[2]))
    con = -con
    a=con/px[0]
    b=con/px[1]
    c=con/px[2]
    print(" De ejercicio 3 puntos: A es: ",a, "B es: ", b, "C es: ", c)

def plano_equisdistante():
    #plano equisdistante
    l1 = []
    l2= []
    for i in range(3):
        valor = input("introduce valor: {} de l1\t".format(i))
        if valor == "s":
            return
        valor = float(valor)
        l1.append(valor)
    for i in range(3):
        valor = input("introduce valor: {} de l2\t".format(i))
        if valor == "s":
            return
        valor = float(valor)
        l2.append(valor)
    con = 0
    i = 0
    while i < 3:
      con += l1[i]**2
      con -= l2[i]**2
      i += 1

    con = -con
    a=con/((-l1[0]*2)-(-l2[0]*2))
    b=con/((-l1[1]*2)-(-l2[1]*2))
    c=con/((-l1[2]*2)-(-l2[2]*2))
    print(" De ejercicio equidistantes: A es: ",a, "B es: ", b, "C es: ", c)

def mon():
    #conseguir m o n
    l1 = []
    l2= []
    l3= []
    for i in range(3):
        valor = input("introduce valor: {} de l1\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        l1.append(valor)
    for i in range(3):
        valor = input("introduce valor: {} de l2\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        l2.append(valor)
    for i in range(3):
        valor = input("introduce valor: {} de l3\t".format(i+1))
        if valor == "s":
            return
        valor = float(valor)
        l3.append(valor)
    u = []
    v = []
    px = []
    for i in range(3):
        px.append(0)
    i = 0
    while i < 3:
      u.append(l2[i]-l1[i])
      v.append(l3[i]-l1[i])
      i += 1

    px[0] = ((u[1]*v[2])-(u[2]*v[1]))
    px[1] = ((u[2]*v[0])-(u[0]*v[2]))
    px[2] = ((u[0]*v[1])-(u[1]*v[0]))
    mx = -px[1]/px[0]
    nx = -px[2]/px[0]
    mz = -px[0]/px[2]
    nz = -px[1]/px[2]
    my = -px[0]/px[1]
    ny = -px[2]/px[1]


    print(" m en la forma x = my + nz + A es igual a: ", mx)
    print(" n en la forma x = my + nz + A es igual a: ", nx)
    print(" m en la forma z = mx + ny + A es igual a: ", mz)
    print(" n en la forma z = mx + ny + A es igual a: ", nz)
    print(" m en la forma y = mx + nz + A es igual a: ", my)
    print(" n en la forma y = mx + nz + A es igual a: ", ny)
while(repetir == True):
    print("Resolvedor de calculo ejercucios planos y puntos.")
    print("si quiere salir de la funcion presione \"s\"")
    print("***************************Menu***************************")
    print("********** teclea lo que quieras resolver **********")
    print("1. Angulo entre 2 planos.\n2. Dos Rectas paramedicas.\n3. Angulos por 3 Puntos.\n4.La distancia entre dos puntos y dos rectas\n5.Sacar la perpendicular\n6."
          "tres puntos\n7. Equisendante\n8. M o N\n")
    while(respuesta > 8):
        respuesta = float(input())
        respuesta = int(respuesta)
    if respuesta == 1:
        dos_rectas_paramericas()
    if respuesta == 2:
        dospuntos_dosrectas()
    if respuesta == 3:
        angulo_3_puntos()
    if respuesta == 4:
        dospuntos_dosrectas()
    if respuesta == 5:
        perpendicular()
    if respuesta == 6:
        tres_puntos()
    if respuesta == 7:
        plano_equisdistante()
    if respuesta == 8:
        mon()
    respuesta = 9