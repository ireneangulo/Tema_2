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
        
