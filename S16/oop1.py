from autos import Car
from users import Person
from autos import GasStation




gas1 = GasStation(1234)
gas1.set_price(6.55, 1234)

vw = Car()
print(f"You have to pay {gas1.fill(vw, 10)}")
# print(gas1.get_price())

# ford = Car()

# print(ford.get_gas_percentage())
# print(ford.get_consumption())
# # ford.start_engine()
# # ford.refill(16)
# # ford.drive(250)
# # ford.drive(1)

# p1 = Person()
# p2 = Person()

# print(ford.get_consumption())
# ford.add_person(p1)
# ford.add_person(p2)
# print(ford.get_consumption())