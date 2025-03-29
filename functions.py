# closures in python


def adder(value):
    def inner(base):
        return base + value
    
    return inner

adder_25 = adder(25)
# result = adder_25(50)

# print("Result ",result)



# decorators in python

def greeting(func):
    def wrapper():
        print("Nice to meet you")
        func()

    return wrapper


@greeting
def welcome():
    print("Welcome to the function")


# welcome()

x = ("Masala Tea","Lemon Tea","Ginger Tea")
y = enumerate(x)
print(list(y))