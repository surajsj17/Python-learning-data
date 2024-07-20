def example_function(number): #type: ignore
    if number < 0:
        raise ValueError("Number must be non-negative.")
    else:
        return number * number # type: ignore

try:
    result = example_function(-5) # 5
except ValueError as e:
    print(f"Caught an exception: {e}")
else:
    print(f"The result is: {result}")

#Example-2:
class CustomError(Exception):
    def __init__(self, message ="A custom error occurred"):  #type: ignore
        self.message = message
        super().__init__(self.message)

# Example of using the custom exception
def example_function(value): #type: ignore
    if value == 0:
        raise CustomError #("Value cannot be zero.")
    else:
        return 10 / value  #type: ignore

result = example_function(5)
print(result)

try:
    v = int(input("enter value:")) # 0
    result = example_function(v)
except CustomError as e:
    print(f"Caught a custom exception: {e}")
else:
    print(f"The result is: {result}")

