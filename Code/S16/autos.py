class Car:
    """Representation of a virtual car."""

    def __init__(self):
        self.__cmc = 1600
        self.__doors = 4
        self.__tank_capacity = 45
        self.__gas_in_tank = 0
        self.__passengers = []
        self.__engine_running = False

    def add_person(self, person):
        if len(self.__passengers) == self.__doors:
            raise ValueError("Not enough space.")
        self.__passengers.append(person)

    def get_gas_percentage(self):
        """Get current gas level in tank."""
        return self.__gas_in_tank / self.__tank_capacity * 100
    
    def start_engine(self):
        if not self.__engine_running:
            self.__engine_running = True

    def stop_engine(self):
        if self.__engine_running:
            self.__engine_running = False

    def drive(self, km):
        """1. verifica daca motorul functioneaza, daca nu - exceptie
        2. verifica daca poti parcurge km doriti, daca nu - exceptie
        3. daca este combustibil suficient - se consuma benzina *scade gas in tank
        
        - consumul per km se calculeaza ca fiind __cmc/1000"""

        if not self.__engine_running:
            raise ValueError("Engine not running.")
        if not self.can_drive(km):
            raise ValueError("Not enough gas.")
        
        self.__gas_in_tank -= self.get_consumption() * km

    def refill(self, liters):
        if liters > self.__tank_capacity - self.__gas_in_tank:
            raise ValueError("Overflow")
        self.__gas_in_tank = liters

    def get_doors(self):
        return self.__doors
    
    def can_drive(self, km):
        _range = self.__gas_in_tank / self.get_consumption()
        if _range < km:
            return False
        
        return True
    
    def get_consumption(self):
        return self.__cmc / 100000 * 4 + 0.5 * len(self.__passengers)
    
class GasStation:

    def __init__(self, pin):
        self.__price = 0
        self.__busy = False
        self.__pin = pin

    def is_busy(self):
        return self.__busy
    
    def get_price(self):
        return self.__price
    
    def set_price(self, price, pin):
        if pin is not self.__pin:
            raise ValueError("Wrong PIN!")
        self.__price = price

    def fill(self, car: Car, liters):
        if self.__busy:
            raise ValueError("Busy")
        car.stop_engine()
        self.__busy = True
        for x in range(1, liters + 1):
            try:
                car.refill(1)
            except ValueError:
                break
        self.__busy = False
        return x * self.__price