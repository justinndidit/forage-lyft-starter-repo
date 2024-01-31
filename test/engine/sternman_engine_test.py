import sys
sys.path.insert(1,"C:/Users/holar/Desktop/Break-Coding/forage/swyft/forage-lyft-starter-repo")

import unittest
from engines.sternman_engine import Sternman_Engine
from datetime import date

class Test_Sternman_Engine(unittest.TestCase):
    def test_capulet_does_not_need_service(self):
        engine = Sternman_Engine(warning_light_is_on=False)
        
        self.assertIsInstance(engine, Sternman_Engine)
        self.assertFalse(engine.needs_service())
        
    def test_capulet__needs_service(self):
        engine = Sternman_Engine(warning_light_is_on=True)

        self.assertIsInstance(engine, Sternman_Engine)
        self.assertTrue(engine.needs_service())

if __name__ == '__main__':
    unittest.main()