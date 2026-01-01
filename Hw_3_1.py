number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))

first_choise = 1
print("If you need to add, choose 1")
second_choise = 2
print("If you need to subtract, choose 2")
third_choise = 3
print("If you need to multiply, choose 3")
frorth_choise = 4
print("If you need to divide, choose 4")

choice = int(input("Enter what you want to do with the numbers:"))

if choice == 1:
    print("Result:", number_one + number_two)

elif choice == 2:
    print("Result:", number_one - number_two)

elif choice == 3:
    print("Result:", number_one * number_two)

elif choice == 4:
    if number_two != 0:
        print("Result:", number_one / number_two)
    else:
        print("Error: division by zero")

else:
        print("it havent that choice")

