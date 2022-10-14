import math
class Punto: 
    def __init__ (self, x=0, y=0):
        self.x= x
        self.y= y
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def cuadrante (self):
        if self.x >0 and self.y >0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x <0 and self.y >0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x <0 and self.y <0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x >0 and self.y <0:
            print("{} pertenece al cuarto cuadrante".format(self))
        elif self.x !=0 and self.y ==0:
            print("{} se sitúa sobre el eje x".format(self))
        elif self.x ==0 and self.y !=0:
            print("{} se situa sobre el eje y".format(self))
        else:
            print("{}se encuentra sobre el origen".format(self))
    
    def vector (self, p):
        print("El vector  entre {} y {} es ({}, {}".format(self, p, p.x - self.x, p.y - self.y))

    def distancia(self, p):
        d= math.sqrt ( (p.x - self.x)**2 + (p.y - self.y)**2 )
        print("La distancia entre los puntos {} y {} es {}".format (self, p, d))

class Rectangulo:
    def __init__(self, inicial=Punto(), final=Punto()):
        self.inicial = inicial
        self.final = final

        self.vBase= abs(self.final.x - self.inicial.x)
        self.vAltura= abs(self.final.y - self.inicial.y)
        self.vArea= self.vBase * self.vAltura
    
    def base(self):
        print("La base del rectangulo es {}".format(self.vBase))
    
    def altura(self):
        print("La altura del rectangulo es {}".format(self.vAltura))
    
    def area(self):
        print("El area del rectangulo es {}".format(self.vArea))
#Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
A= Punto(2,3)
B= Punto(5,5)
C= Punto(-3, -1)
D= Punto(0,0)

#Consulta a que cuadrante pertenecen el punto A, C y D.
A.cuadrante()
C.cuadrante()
D.cuadrante()

#Consulta los vectores AB y BA.
A.vector(B)
B.vector(A)

#(Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
A.distancia(B)
B.distancia(A)

#(Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
#Al calcular la distancia ponemos la D entre parentesis ya que es el punto (0,0)
A.distancia(D)
B.distancia(D)
C.distancia(D)

#Crea un rectángulo utilizando los puntos A y B.
R= Rectangulo(A,B)

#Consulta la base, altura y área del rectángulo.
R.base()
R.altura()
R.area()






    





    
        
