class WGS84Coord:

    def __init__(self, lng=0.0, lat=0.0):
        self.setLongitude(lng)
        self.setLatitude(lat)

    def ausgabe(self):
        print(f"{self._longitude}")
        print(f"{self._latitude}")

    def getPrefix(self,x):
        if x>0:
            return 1
        else:
            return -1

    def setLongitude(self, lng):
        if abs(lng)>180:
            print("Eingabe ausserhalb des gültigen Wertebereichs")
        absoluteLongitude = abs(lng)
        if (int(abs(lng/180)+1)%2 == 0):
            self._longitude = ((absoluteLongitude%180)-180)* self.getPrefix(lng)
        else:
            self._longitude = (absoluteLongitude%360) *self.getPrefix(lng)

    def setLatitude(self,lat):
        self._latitude = lat




a = WGS84Coord(7.636308202373822, 47.5386323231523)
b = WGS84Coord(183.64, 95.53)


b.ausgabe()
