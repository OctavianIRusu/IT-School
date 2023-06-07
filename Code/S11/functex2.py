# Functie care returneaza volumul unui cilindru in litri.
# Primeste doua argumente, inaltimea si raza bazei in metri.

PI = 3.14

def cil_volume(height, radius):
    """Calculate the volume in liters of a cylinder given the height and the radius in meters"""
    return 2 * PI * radius ** 2 * height * 1000

height1 = float(input("Enter the cylinder height in meters: "))
radius1 = float(input("Enter the cylinder radius in meters: "))

print(f"The cylinder has a volume of {cil_volume(height1, radius1)} liters.")
