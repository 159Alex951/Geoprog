class punkt:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class strecke:
    def __init__(self, x1,y1, x2,y2):
        self.A = punkt(x1,y1)
        self.B = punkt(x2,y2)


S = strecke(3,4,4,5)