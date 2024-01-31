import sys
sys.path.insert(1,"C:/Users/holar/Desktop/Break-Coding/forage/swyft/forage-lyft-starter-repo")

import unittest
from tires.carrigan_tire import Carrigan_Tire

class Test_Carrigan_Tire(unittest.TestCase):
    def test_Carrigan_does_not_need_service(self):
        tire = Carrigan_Tire(tire_pressures=[0.1,0.1,0.1,0.1])

        self.assertIsInstance(tire, Carrigan_Tire)
        self.assertFalse(tire.needs_service())
        
    def test_Carrigan_needs_service(self):
        tire = Carrigan_Tire(tire_pressures=[1,1,1,1])

        self.assertIsInstance(tire, Carrigan_Tire)
        self.assertTrue(tire.needs_service())

if __name__ == '__main__':
    unittest.main()