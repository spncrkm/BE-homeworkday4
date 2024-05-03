# Lesson 5: Python Functions
# Problem 1 == The Calculator App
# Task 1

def add_numbers(a,b):
    return a + b

def multiply_nums(a,b):
    return a * b

def subtract_nums(a,b):
    return a - b

def divide_nums(a,b):
    return a / b


# Task 2 and 3

user_nums = int(input("Enter first number "))
user_nums2 = int(input("Enter second number "))
operation = input("Do you want to add, subtract, multiply, divide ")

if operation == "add":
    result = add_numbers(user_nums, user_nums2)
    print(f"The answer is ", result)
elif operation == "subtract":
    result = subtract_nums(user_nums, user_nums2)
    print(f"The answer is ", result)
elif operation == "multiply":
    result = multiply_nums(user_nums, user_nums2)
    print(f"The answer is ", result)
elif operation == "divide":
    if user_nums2 is not 0:
        result = divide_nums(user_nums, user_nums2)
        print(f"The answer is ", result)
    else:
        print("Cannot divide by zero. Try again")
else:
    print("Invalid input")


# Problem 2 == The Shopping List Maker
# Task 1

# shopping_list = []
# while True:
#     items = input("Add items to your cart. Type 'quit' to quit adding. ")
#     if items != "quit":
#         items = shopping_list.append(items)
#     else:
#         break
#     print(shopping_list)

# Task 2

cart = []

print("Lets go grocery shopping!")
while True:
    user_input = input("Would you like to add or remove from your cart or say 'done' to finish: ")
    if user_input == "done":
        print("Thanks for shopping here are your items: ")
        for item in cart:
            print(item)
        break
    elif user_input == "remove":
        removal = input("what item would you like to remove?")
        if removal in cart:
            cart.remove(removal)
            print(removal, " is removed from the shopping cart.")
    else:
        cart.append(user_input)
        print(f"Your cart so far {cart}")
        
# shopping_list = []
# user_input = input("Add items to your cart. Type 'delete' to remove item and type 'quit' to quit adding. ")
# shopping_list.append(user_input)
# while user_input is not "quit":
#         print("thanks for shopping here are you items: ")
    
# elif user_input == "delete":
#     remove_item = input("Which item would you like to remove? ")
#     if remove_item in shopping_list:
#         shopping_list.remove(remove_item)
#         print(remove_item, " is removed from the shopping cart.")
# print(shopping_list)

# cart = []

# print("Lets go grocery shopping!")
# while True:
#     user_input = input("Tell us what you'd like to add to your cart or say 'quit' to quit: ")
#     if user_input == "quit":
#         print("Thanks for shopping here are your items: ")
#         for item in cart:
#             print(item)
#         break
#     elif user_input == "remove":
#         remove_item = input("what item do you want to remove? ")
#         for item in cart:
#             cart.remove(remove_item)
#             print(item, " is removed from the shopping cart.")

#     else:
#         cart.append(user_input)
#         print(f"Your cart so far {cart}")