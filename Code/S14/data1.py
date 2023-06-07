from faker import Faker
fake = Faker("ro_RO")

for i in range(5):
    print(fake.address())

for i in range(3):
    print(fake.license_plate())