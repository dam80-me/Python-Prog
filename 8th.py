try:
    marks=int (input("Please enter your marks:"))

    if marks <0 or marks >100:
        print ("Invalid Input")
        marks=int (input("Please enter your marks:"))

    if marks >=75:
        print(f"Your grade {marks} is A.")
    elif marks >=65:
        print(f"Your grade {marks} is B.")
    elif marks >=55:
        print(f"Your grade {marks} is C.")
    elif marks >=35:
        print(f"Your grade {marks} is S.")
    else: 
        print(f"Your grade {marks} is W.")

except ValueError:
    print ("Invalid input. Please enter a valid whole number.")