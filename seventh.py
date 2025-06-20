#Ask the user to enter an integer
#Using a try-except block to handle potention ValueError if non-integer

try:
    number=int (input("Please enter an integer:"))

    # Check if the number is positive, negative or zero
    if number >0:
        print(f"The number {number} is positive.")
    elif number <0:
        print(f"The number {number} is negative.")
    else: #This condition will be true if number is 0
        print(f"The number {number} is zero.")

except ValueError:
    print ("Invalid input. Please enter a valid whole number.")