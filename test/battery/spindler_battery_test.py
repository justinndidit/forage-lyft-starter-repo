import sys
sys.path.insert(1,"C:/Users/holar/Desktop/Break-Coding/forage/swyft/forage-lyft-starter-repo")

import unittest
from batteries.spindler_battery import Spindler_Battery

class Test_Nubbin_Battery(unittest.TestCase):
    def test_Splindler_does_not_need_service(self):
        battery = Spindler_Battery(current_date="2024-01-31",last_service_date="2024-01-31")

        self.assertIsInstance(battery, Spindler_Battery)
        self.assertFalse(battery.needs_service())
        
    def test_Splinder_needs_service(self):
        battery =Spindler_Battery(current_date='2023-08-11', last_service_date='2017-08-11')

        self.assertIsInstance(battery, Spindler_Battery)
        self.assertTrue(battery.needs_service())

if __name__ == '__main__':
    unittest.main()