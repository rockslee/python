from function.function import get_formatted
print("Enter 'q' at any time to quit:")
while True:
    first = input("\nPlease give me a first name:")
    if first == 'q':
        break
    last = input("Please give me a last name:")
    if last == 'q':
        break
    formatted_name = get_formatted(first,last)
    print("\nNeatly formatted name:"+formatted_name+".")