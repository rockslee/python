from function.function import  make_pizza,bulid_profile as bp
from classes.classes import Dog,Car,ElectricCar
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
user_profile=bp('rocks','lee',city='beijing',where='hebei')
print(user_profile)

my_dog = Dog('black',3)

print("My dog's name is "+my_dog.name.title()+'.')
print("My dog is "+str(my_dog.age)+' year old.')
my_dog.roll_over()
my_dog.sit()

your_dog = Dog('flower',6)
print("Your dog's name is "+your_dog.name.title()+\
      '.'+" It's "+str(your_dog.age)+' years old.')
your_dog.sit()
your_dog.roll_over()

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
print(my_new_car.model)
my_new_car.read_odometer()
my_new_car.update_odometer(100)
my_new_car.read_odometer()
my_new_car.update_odometer(99)
my_new_car.read_odometer()
my_new_car.odometer_reading = 101
my_new_car.read_odometer()
my_new_car.increment_odometer(-10)
my_new_car.read_odometer()
e_car = ElectricCar('tesla','model s','2020')
print(e_car.get_descriptive_name())
e_car.read_odometer()
e_car.update_odometer(200)
e_car.read_odometer()
e_car.battery.describe_battery()
e_car.battery.get_range()