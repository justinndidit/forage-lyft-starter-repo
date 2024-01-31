import sys
sys.path.insert(1,"C:/Users/holar/Desktop/Break-Coding/forage/swyft/forage-lyft-starter-repo")

import unittest
from engines.capulet_engine import Capulet_Engine
from datetime import date

class Test_Capulet_Engine(unittest.TestCase):
    def test_capulet_does_not_need_service(self):
        engine = Capulet_Engine(current_mileage=0,last_service_mileage=0)
        self.assertIsInstance(engine, Capulet_Engine)
        self.assertFalse(engine.needs_service())
        
    def test_capulet__needs_service(self):
        engine = Capulet_Engine(current_mileage=6000, last_service_mileage=2000)

        self.assertIsInstance(engine, Capulet_Engine)
        self.assertTrue(engine.needs_service())

if __name__ == '__main__':
    unittest.main()