import sys
sys.path.insert(1,"C:/Users/holar/Desktop/Break-Coding/forage/swyft/forage-lyft-starter-repo")

from tire import Tire

class Carrigan_Tire(Tire):
    def __init__(self, tire_pressures):
        self.tire_pressures = tire_pressures

    def needs_service(self):
        pressure = 0
        for tire_pressure in self.tire_pressures:
            if tire_pressure >= 0.9:
                return True


        return False