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
