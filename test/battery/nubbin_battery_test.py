import sys
sys.path.insert(1,"C:/Users/holar/Desktop/Break-Coding/forage/swyft/forage-lyft-starter-repo")

import unittest
from batteries.nubbin_battery import Nubbin_Battery

class Test_Nubbin_Battery(unittest.TestCase):
    def test_Nubbin_does_not_need_service(self):
        battery = Nubbin_Battery(current_date="2024-01-31",last_service_date="2024-01-31")

        self.assertIsInstance(battery, Nubbin_Battery)
        self.assertFalse(battery.needs_service())
        
    def test_Nubbin_needs_service(self):
        battery =Nubbin_Battery(current_date='2023-08-11', last_service_date='2017-08-11')

        self.assertIsInstance(battery, Nubbin_Battery)
        self.assertTrue(battery.needs_service())

if __name__ == '__main__':
    unittest.main()