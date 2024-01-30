from car import Car
from batteries.nubbin_battery import Nubbin_Battery
from batteries.spindler_battery import Spindler_Battery
from engines.capulet_engine import Capulet_Engine
from engines.sternman_engine import Sternman_Engine
from engines.willoughby_engine import Willoughby_Engine

def create_calliope(current_date, last_service_date,current_mileage, last_service_mileage): 
    new_engine = Capulet_Engine(current_mileage, last_service_mileage)
    new_battery = Spindler_Battery(current_date, last_service_date)

    return Car(new_engine, new_battery)

def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage): 
    new_battery = Spindler_Battery(current_date, last_service_date,)
    new_engine = Willoughby_Engine(current_mileage, last_service_mileage)

    return Car(new_engine, new_battery)

def create_palindrome(current_date, last_service_date, warning_light_on):
   new_battery = Spindler_Battery(current_date, last_service_date)
   new_engine = Sternman_Engine(warning_light_on)

   return Car(new_engine, new_battery)

def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage): 
    new_battery = Nubbin_Battery(current_date,last_service_date)
    new_engine = Willoughby_Engine(current_mileage, last_service_mileage)

    return Car(new_engine, new_battery)
    

def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage): 
    new_engine = Capulet_Engine(current_mileage, last_service_mileage)
    new_battery = Nubbin_Battery(current_date, last_service_date)

    return Car(new_engine, new_battery)

