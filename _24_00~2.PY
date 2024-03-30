
import datetime

# asks for input in one line and split it into a list of integers
input_string = input("Enter three numbers separated by spaces: ")
inputs = [int(i) for i in input_string.split()]

# TODO: Create the logging_decorator() function 👇

def outer_decorator_logging_function(main_function):
    def inner_wrapper(*args, **kwargs):
        current_time = datetime.datetime.now()

        timestamp = current_time.strftime('%Y-%m-%d %H:%M:%S')

        print(f"\nDate & Time: {timestamp}. \nThe function and data being called: {main_function.__name__}{args}")
        print("The function will start this process:")
        return main_function(*args, **kwargs)
    return inner_wrapper



# TODO: Use the decorator 👇

@outer_decorator_logging_function
def a_function(a, b, c):
    print(f"Starting the multiplication process.\n")
    result = a * b * c
    print(f"Multiplication done. The result is: {result}")
    return result

a_function(inputs[0], inputs[1], inputs[2])