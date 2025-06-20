try:
    numerator_input = input ("Please enter the numerator:")
    numerator = float (numerator_input)  #Use float to allow for decimal

    denominator_input = input ("Please enter the denominator:")
    denominator = float (denominator_input) #Use float to allow for decimal

    result = numerator/denominator


    print(f"You entered : Numerator = {numerator}, Denominator = {denominator}")
    print (f"The result of the division is : {result}")

except ValueError:

    print ("Invalid input. Please enter valid numbers for both numerator and denominator")

except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    #Catch any other unexpected errors
    print(f"An unexpected error occured: {e}")

