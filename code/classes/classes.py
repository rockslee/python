class  Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name=name
        self.age=age
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+' is now sitting.')
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + ' rolled over.')

class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+' miles on it.')
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
class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self,make,model,year):
        """
        初始化父类的属性
        再初始化电动汽车特有的属性
        """
        super().__init__(make,model,year)
        self.battery_size = 0
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a "+str(self.battery_size)+"-KWh battery.")
    def fill_gas_tank(self):
        """电动汽车没有邮箱"""
        print("This car doesn't need a gas tank!")
class Battery():
    """一次模拟电动汽车电瓶的简易尝试"""
    def __init__(self,battery_size=70):
