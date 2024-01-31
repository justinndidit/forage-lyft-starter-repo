import sys
sys.path.insert(1,"C:/Users/holar/Desktop/Break-Coding/forage/swyft/forage-lyft-starter-repo")

from battery import Battery
from datetime import datetime

class Nubbin_Battery(Battery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = datetime.fromisoformat(str(last_service_date))
        self.current_date = datetime.fromisoformat(str(current_date))

    def needs_service(self):
        return self.current_date.year - self.last_service_date.year > 4
    