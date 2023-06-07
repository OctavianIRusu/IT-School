class Car:

    sound = "ti ti ti"

    def __init__(self) -> None:
        self.__engine_started = False
        Car.horn()  # acces catre metoda statica din metoda normala

    def start_engine(self):
        self.__engine_started = True

    def __stop_engine(self):
        # metoda privata (o anumita functionalitate - de ex. stergere doar daca administrator)
        self.__engine_started = False

    @staticmethod
    def horn():
        # din metoda statica nu exista acces catre atributele de instanta
        # pot fi accesate in schimb atributele statice
        print(Car.sound)


# Client code
vw = Car()
vw.horn()
Car.horn()
