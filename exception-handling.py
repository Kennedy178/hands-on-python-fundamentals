def access_services(age):
    try:
        if age < 18:
            raise ValueError("You must be at least 18 years old to register.")
        print("Registration successful.")
    except ValueError as e:
        print(e)
    finally:
        print("Thank you for using our service.")

try:
    age = float(input("Enter your age: "))
    access_services(age)
except ValueError:
    print("Invalid input. Please enter a number.")







def get_item_at_index(lst, index):
    try:
        print("Item at index", index, "is:", lst[index])
    except IndexError:
        print("Index out of range. Please try a valid index.")
    finally:
        print("Operation completed.")

# Sample list
lst = ['A', 'B', 'C', 'D', 'E']

# Get user input
try:
    index = int(input("Enter an index to retrieve the item: "))
    get_item_at_index(lst, index)
except ValueError:
    print("Invalid input! Please enter a valid number.")





def add_numbers(a, b):
    try: 
        a = int(a)
        b = int(b)
        c = a + b
        return c
    except ValueError:
        print("Invalid input. Please enter only numbers.")

# Get input
a = input("Enter the first number: ")
b = input("Enter the second number: ")

# Call function and show result if valid
result = add_numbers(a, b)
if result is not None:
    print("The sum is:", result)








