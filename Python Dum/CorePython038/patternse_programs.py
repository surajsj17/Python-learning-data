
def print_pyramid(n: int):
    print("pyramid")
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

n = int(input("Enter the number of rows: "))
print_pyramid(n)

print("@"*100)
def print_diamond(n: int):
    print("Diamond")
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

n = int(input("Enter the number of rows: "))
print_diamond(n)
print("@"*100)
def print_inverted_half_pyramid(n: int):
    print("Half pyramid")
    for i in range(n, 0, -1):
        print("*" * i)

n = int(input("Enter the number of rows: "))
print_inverted_half_pyramid(n)
print("@"*100)

def print_number_pattern(n: int):
    print("Number Patterns")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

n = int(input("Enter the number of rows: "))
print_number_pattern(n)

