class Person:

    def __init__(self): #constructor
        self.__height = 180
        self.__weight = 0

    def get_height_cm(self):
        return self.__height
    
    def get_height_m(self):
        return self.__height / 100


vlad = Person()
maria = Person()

print(f"The height is {vlad.get_height_cm()} cm.")
print(f"The height is {vlad.get_height_m()} m.")