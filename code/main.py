import json
username = input("What is your name?")
filename = './data/username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remeber you when you come back, "+username+'！')