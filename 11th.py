#Initialize a variable for the countdown starting from 10
countdown_number =10

# Use a while loop to continue as long as countdown_number is greater than 0
while countdown_number >0:
    # Print the current number in the countdown
    print(countdown_number)
    # Decrement the countdown_number by 1 in each iteratioon
    countdown_number-=1 # This is equyivalent to countdown_number = countdown_number -1
# After the loop finishes (when countdown_number becomes 0 or less),
print("Lift off!")