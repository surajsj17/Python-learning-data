# Example of using assert for debugging
# assert exp ,'msg'
def divide(x, y):
    assert y != 0, "Divisor cannot be zero!.." #2!=0 T # 0 =F
    return x / y

# Testing the divide function
print(divide(10, 2))  # Output: 5.0
print(divide(8, 0))   # Raises an AssertionError with the message "Divisor cannot be zero!"
print("hello")

assert 5 <0 , 'should be less than zero '



