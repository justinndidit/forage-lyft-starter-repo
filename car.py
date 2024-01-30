from serviceable import Serviceable
from engine import Engine
from battery import Battery

class Car(Serviceable):
    def __init__(self, engine,battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return Engine.needs_service() and Battery.needs_service()
    

