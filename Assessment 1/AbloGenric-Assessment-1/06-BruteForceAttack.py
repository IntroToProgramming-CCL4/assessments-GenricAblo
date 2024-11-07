#declares two variables for attempts and the correct password
password = '12345'
attempts = 5
x = True

guess = input("please enter your 5-digit password. Keep in mind, you only have 5 attempts to successfully input the password: \n")
while guess != password and attempts > 1:
    attempts = attempts - 1
    print(f"Incorrect, Try again, You have {str(attempts)} remaining")
    guess = input()
    if attempts < 0:
        print("You have run out of attempts, we have notified the authorities")
    else :
        print("Correct")