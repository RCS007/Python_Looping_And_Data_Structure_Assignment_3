# Question 3

# Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the message “Too
# low” and ask them to try again. If they enter a value above 20, display the message “Too high” and ask them to
# try again. Keep repeating this until they enter a value that is between 10 and 20 and then display the message
# “Thank you”.

# Loop until the user enters a number between 10 and 20
while True:
    # Ask the user to input a number
    user_input = int(input("Enter a number between 10 and 20: "))
    
    # Check if the number is too low, too high, or valid
    if user_input < 10:
        print("Too low. Try again.")
    elif user_input > 20:
        print("Too high. Try again.")
    else:
        print("Thank you!")
        break  # Exit the loop if the input is valid
