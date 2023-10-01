def hello(user_name):
    print(f"Hello, {user_name}! How are you?")
    
def pack(arg_1, arg_2, arg_3):
    return [arg_1, arg_2, arg_3]

def eat_lunch(Lunch_items):
    if len(Lunch_items) == 0:
        print("You have no lunch items")
    else:
        for index in range(len(Lunch_items)):
            if index == 0:
                print(f"First I eat: {Lunch_items[index]}")
            else:
                print(f"Then I eat: {Lunch_items[index]}")
    
print (pack("apples", "bananas", "oranges"))
hello("Rudy")

eat_lunch(pack("apples", "bananas", "oranges"))