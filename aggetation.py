class punkt:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class strecke:
    def __init__(self, punkt1, punkt2):
        self.A = punkt1
        self.B = punkt2

A = punkt(3,4)
B = punkt(4,5)
S = strecke(A,B)