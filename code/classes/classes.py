class Odometer():
    """
    支持电动汽车，燃油汽车里程计算
    电动汽车类型为：1，燃油汽车类型为：0
    """
    def __init__(self,type=1,energy=55):
        self.type = type
        self.energy = energy
    def get_range(self):
        if self.type == 0:
            if self.energy == 55:
                range = 100
            elif self.energy == 75:
                range = 120
        elif self.type == 1:
            if self.energy == 55:
                range = 250
            elif self.energy == 75:
                range = 400
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)
    def modify_energy(self,energy):
        self.energy = energy
    def modify_type(self,type):
        self.type = type
    def update_odometer(self,mileage):
        """
        将里程表读数设置未指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Your can't roll back an odometer!")
    def increment_odometer(self,miles):
        """
        将里程表读数增加指定的量
        禁止里程表负增长
        """
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("Your can't roll back an odometer!")
class Battery():
    """一次模拟电动汽车电瓶的简易尝试"""
    def __init__(self,battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
        self.range = Odometer()
    def describe_battery(self):
        """打印一条描述电瓶容量的参数"""
        print("This car has a "+str(self.battery_size)+"-KWh battery.")
class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = Odometer()
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make,model,year)
        self.battery = Battery()
    def fill_gas_tank(self):
        """电动汽车没有邮箱"""
        print("This car doesn't need a gas tank!")
