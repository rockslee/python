with open('./file/love.txt','a') as file_object:
    file_object.write("I love you.\n")
    file_object.write("biu biu biu.\n")
    file_object.write("123456789\n")
with open('./file/love.txt') as file:
    contents = file.read()
    print(contents)
