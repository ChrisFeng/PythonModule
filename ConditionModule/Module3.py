if __name__ == "__main__":
    print("Module3.py is being run directly")
else:
    print("Module3.py is being imported into another module")

def if_function(inumber):
    if inumber > 0:
        print(f"{inumber} is bigger than 0")
    elif inumber < 0:
        print(f"{inumber} is smaller than 0")
    else:
        print(f"{inumber} is 0")

def while_function(inumber):
    i = 0
    while i < inumber:
        print(i)
        i = i + 1

def for_function(inumber):
    assert inumber > 0, "必須大於0"
    i = 0
    for i in range(inumber):
        print(i)