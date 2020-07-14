def show_magicians(magicians_name):
    """
    将所有魔术师的名字打印出来
    :param magicians_name:
    :return:
    """
    while magicians_name:
        print('Printing Magicans name:'+magicians_name.pop())
names = ['aaa','bbb','ccc','ddd']
show_magicians(names)
print("#####################我是分割符#####################")
def print_models(unprinted_designs,completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到completed_models
    :param unprinted_designs:
    未打印的设计列表
    :param completed_models:
    打印完成的设计列表
    :return:
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing Model:'+current_design)
        completed_models.append(current_design)
def show_completed_models(competed_models):
    """
    显示打印好的所有模型
    :param competed_models:
    :return:
    """
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)
print("#####################我是分割符#####################")
#向函数内传递列表的副本，可以实现列表不被修改的情况下，打印所有作品
print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)
show_completed_models(unprinted_designs)
print("#####################我是分割符#####################")
#首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

#模拟打印每个设计，直到没有未打印的设计为止
#打印每个设计后，都将其移到completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    #模拟根据设计制作3D打印模型的过程
    print('Printing model:'+current_design)
    completed_models.append(current_design)
#显示打印号的所有模型
print('\nThe following models have been printed:')
for completed_model in completed_models:
    print(completed_model)
def greet_user(names):
    """向列表中每一位用户都发出问候"""
    for name in  names:
        msg = 'Hello '+ name.title()+'!'
        print(msg)
usernames = ['rockslee','tony','sentu']
greet_user(usernames)

def greet_user(username="lilei",sex="boy"):
    """显示简单的问候语"""
    print(username.title()+" is "+sex+"!")
greet_user()
greet_user("sarah","girl")
greet_user(username="rockslee")
greet_user(sex="boy",username="tony")

def make_shirt(size):
    """制作SHirt"""
    print("This shirt is "+size+" .")
make_shirt("100")

def make_big_shirt(word="I LOVE PYTHON"):
    """印有文字的Shirt"""
    print(word)
make_big_shirt()
make_big_shirt(word="L LOVE C++")

def discribe_city(city,country="china"):
    """描述城市"""
    msg = city.title()+" is in "+country.title()
    print(msg)
discribe_city("beijing")
discribe_city(city="nanjing")
discribe_city(city="tokyo",country="japan")

def get_formatted_name(first_name,last_name):
    """格式化名字"""
    full_name = first_name+" "+last_name
    return full_name.title()
engineer = get_formatted_name("lee","rocks")
print(engineer)
engineer = get_formatted_name(first_name="rocks",last_name="lee")
print(engineer)

def get_formatted_name_2(first_name,last_name,middle_name=""):
    """格式化名字"""
    if middle_name:
        full_name = first_name+" "+middle_name+" "+last_name
    else:
        full_name = first_name+" "+last_name
    return full_name.title()
print("#####################我是分割符#####################")
engineer_2 = get_formatted_name_2(first_name="lee",middle_name="xian",last_name='rocks')
print(engineer_2)
engineer_2 = get_formatted_name_2(first_name="lee",last_name='rocks')
print(engineer_2)

def dic_name(firstname,lastname,age=''):
    """返回一个包含个人名称的字典"""
    person = {'first':firstname,'last':lastname}
    if age:
        person['age']=age
    return person
person_name=dic_name('lee','rocks',age='18')
print(person_name)
print(person_name.keys())
print(person_name.values())
print(person_name['first'])
print(person_name['last'])

while True:
    print('\n请告诉我你的名字！')
    f_name=input('First_name:')
    l_name=input('Last_name:')
    formatted_name = get_formatted_name_2(f_name,l_name)
    print('\n早上好， '+formatted_name+' .')
