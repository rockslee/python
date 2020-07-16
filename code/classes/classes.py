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