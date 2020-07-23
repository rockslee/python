def make_pizza(size,*toppings):
    """
    概述要制作的比萨
    :param size:
    :param topping:
    :return:
    """
    print('\nMaking a '+str(size)+'-inch pizza with the following topping:')
    for topping in toppings:
        print('-'+topping)

def bulid_profile(first,last,**user_info):
    """创建一个字典，其中包括我们知道的用户的一切"""
    profile = {}
    profile[first]=first
    profile[last]=last
    for key,value in user_info.items():
        profile[key]=value
    return profile

def get_formatted(first,last):
    full_name = first+" "+last
    return full_name.title()