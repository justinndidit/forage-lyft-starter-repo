import sys
sys.path.insert(1,"C:/Users/holar/Desktop/Break-Coding/forage/swyft/forage-lyft-starter-repo")

import unittest
from engines.capulet_engine import Capulet_Engine
from engines.sternman_engine import Sternman_Engine
from engines.willoughby_engine import Willoughby_Engine
from batteries.spindler_battery import Spindler_Battery
from batteries.nubbin_battery import Nubbin_Battery
from datetime import date
from car_factory import create_calliope, create_glissade, create_palindrome, create_rorschach, create_thovex
from car import Car

class TestEngines(unittest.TestCase):
    def test_capulet_engine_initialization(self):
        engine = Capulet_Engine(current_mileage=50000, last_service_mileage=45000)
        self.assertIsInstance(engine, Capulet_Engine)
        
    def test_sternman_engine_initialization(self):
        engine = Sternman_Engine(warning_light_is_on=True)
        self.assertIsInstance(engine, Sternman_Engine)
        
    def test_willoughby_engine_initialization(self):
        engine = Willoughby_Engine(current_mileage=60000, last_service_mileage=55000)
        self.assertIsInstance(engine, Willoughby_Engine)

class TestBatteries(unittest.TestCase):
    def test_spindler_battery_initialization(self):
        battery = Spindler_Battery(current_date=date.today(), last_service_date=date.today())
        self.assertIsInstance(battery, Spindler_Battery)
        
    def test_nubbin_battery_initialization(self):
        battery = Nubbin_Battery(current_date=date.today(), last_service_date=date.today())
        self.assertIsInstance(battery, Nubbin_Battery)

# class TestCar(unittest.TestCase):
#     def test_calliope(self):
#         car = create_calliope(current_date=date.today(), last_service_date=date.today(), current_mileage=50000, last_service_mileage=45000)
#         self.assertIsInstance(car, Car)


if __name__ == '__main__':
    unittest.main()
