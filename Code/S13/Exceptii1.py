import logger

def circle_area(radius):
    """Calculate the circle area. Radius has to be a positive integer.
    
    Args:
        - radius (float): Circle radius

    Raises:
        - ValueError: if radius is less than 0
    """
    if radius < 0:
        raise ValueError(f"Circle area cannot be a negative number. Had: {radius}")
    
    return 3.14 * radius ** 2

try:
    number = float(input("Raza cerc: "))
except ValueError as err:
    logger.error(err)
else:
    try:
        print(circle_area(number))
    except ValueError as err:
        print(f"[ERROR] {err}")

try:
    1 / 0
except Exception as err:
    print(err)

print("END")