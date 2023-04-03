class Person:

    def __init__(self): #constructor
        self.__height = 180
        self.__weight = 0

    def get_height_cm(self):
        return self.__height
    
    def get_height_m(self):
        return self.__height / 100
