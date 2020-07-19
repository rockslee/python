with open('file\pi_million_digits.txt') as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

while True:
    b = input("输入您的生日，格式（MMDDYY）:")
    if b in pi_string:
        print("恭喜！！！您的生日在Π中！！！")
    else:
        print("您的生日没有在Π中")