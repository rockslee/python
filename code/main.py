from classes.classes import Car,ElectricCar

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
e_car = ElectricCar('tesla','model s','2020')
print(e_car.get_descriptive_name())
e_car.battery.range.modify_type(0)
e_car.battery.range.modify_energy(75)
e_car.battery.range.get_range()
my_new_car.odometer_reading.get_range()