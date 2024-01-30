import sys
sys.path.insert(1,"C:/Users/holar/Desktop/Break-Coding/forage/swyft/forage-lyft-starter-repo")

from datetime import datetime

from battery import Battery

class Nubbin_Battery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        print('tt')
        return datetime.utcfromtimestamp(self.current_date).year - datetime.utcfromtimestamp(self.last_service_date).year  > 4
    


