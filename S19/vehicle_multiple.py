class ElectricVehicle:

    def charge(self):
        print("charging")


class DieselVehicle:

    def refill(self):
        print("refuelling diesel tank")


class HybridVehicle(ElectricVehicle, DieselVehicle):
    pass


toyota = HybridVehicle()

toyota.refill()
