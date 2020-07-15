from function.function import  make_pizza,bulid_profile as bp
from classes.classes import Dog
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')
user_profile=bp('rocks','lee',city='beijing',where='hebei')
print(user_profile)

my_dog = Dog('black',3)

print("My dog's name is "+my_dog.name.title()+'.')
print("My dog is "+str(my_dog.age)+' year old.')
my_dog.roll_over()
my_dog.sit()