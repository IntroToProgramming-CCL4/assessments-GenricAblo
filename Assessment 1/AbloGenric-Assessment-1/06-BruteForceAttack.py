#declares two variables for attempts and the correct password
password = '12345'
attempts = 5
#Asks input from the user and stores the value in the variable 'guess'
guess = input("please enter your 5-digit password. Keep in mind, you only have 5 attempts to successfully input the password: \n")
#the condition for the while loop is while the guess does not match the correct password AND attempts is greater than 1, the loop continues
while guess != password and attempts > 1:
    # decreases attempts after every loop
    attempts = attempts - 1

    # tells the user the amount of attempts remaining
    print(f"Incorrect, Try again, You have {str(attempts)} remaining")

    #requests for input again while inside the loop
    guess = input()

    #if attempts is less than zero it displays an 'incorrect' message
    if attempts < 0:
        print("You have run out of attempts, we have notified the authorities")
    else :
        #if loop ends and the user still has greater than 0 attempts, it displays a correct message
        print("Correct")