class Car:
    """Representation of a virtual car."""

    def __init__(self):
        self.__cmc = 1600
        self.__doors = 4
        self.__tank_capacity = 45
        self.__gas_in_tank = 0
        self.__passengers = []
        self.__engine_running = False

    def start_engine(self):
        pass

    def stop_engine(self):
        pass

    def drive(self, km):
        """1. verifica daca motorul functioneaza, daca nu - exceptie
        2. verifica daca poti parcurge km doriti, daca nu - exceptie
        3. daca este combustibil suficient - se consuma benzina *scade gas in tank
        
        - consumul per km se calculeaza ca fiind __cmc/1000"""
        pass

    def refill(self, liters):
        if liters > self.__tank_capacity - self.__gas_in_tank:
            raise ValueError("Overflow")
        self.__gas_in_tank = liters

    def get_doors(self):
        return self.__doors
    
    def get_gas_percentage(self):
        """Get current gas level in tank."""
        return self.__gas_in_tank / self.__tank_capacity * 100

vw = Car()
ford = Car()

vw.refill(25)
print(f"Combustibil ramas: {vw.get_gas_percentage(): .1f} %")