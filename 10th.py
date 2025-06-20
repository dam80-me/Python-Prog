try:
    for number in range (1,6):
        number = int(input("Please enter your marks:"))
        while number < 0 or number > 100:
        
                if number >=75:
                    print(f"Your grade {marks} is A.")
                elif number >=65:
                    print(f"Your grade {marks} is B.")
                elif number >=55:
                    print(f"Your grade {marks} is C.")
                elif number >=35:
                    print(f"Your grade {marks} is S.")
                else: 
                    print(f"Your grade {marks} is W.")

except ValueError:
        print ("Invalid input. Please enter a valid whole number.")