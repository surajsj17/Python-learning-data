#write the program to the check the range

number = int(input("Enter the number to check: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))


def is_within_range(number, start, end):
    return start <= number <= end


if is_within_range(number, start, end):
    print(f"The number {number} is within the range [{start}, {end}].")
else:
    print(f"The number {number} is not within the range [{start}, {end}].")
    
'''
Output
Enter the number to check: 45
Enter the start of the range: 40
Enter the end of the range: 50
The number 45 is within the range [40, 50].
'''