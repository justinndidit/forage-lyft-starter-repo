import sys
sys.path.insert(1,"C:/Users/holar/Desktop/Break-Coding/forage/swyft/forage-lyft-starter-repo")

from abc import ABC, abstractmethod

class Battery(ABC):
    @abstractmethod
    def needs_service(self): 
            pass