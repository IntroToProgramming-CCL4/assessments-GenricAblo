#'z' is a variable designed to create a loop during the line of code.
z = 0
#dictionary consisting of  days of the month. Each number is assigned a value that stores the number of days in that month number.
months = {
    '1' : 'January has 31 days', 
    '2': 'February has 28 days',
    '3' : 'March has 31 days',
    '4': 'April has 30 days',
    '5': 'May has 31 days',
    '6': 'June has 30 days',
    '7': 'July has 31 days',
    '8': 'August has 31 days',
    '9': 'September has 30 days',
    '10': 'October has 31 days',
    '11': 'November has 30 days',
    '12': 'December has 31 days',
    '13': 'February during a leap year has 29 days'
}
#I created a loop to continuously ask for the input of the user, this was done to check for possible errors 
#and for the convenience of the user so that they don't have to run the code over and over again 
while z < 10:
    #the value of z increases by increments of 1, this is to limit the number of inputs the code gets to only 10. So that the code doesn't run forever.
    z = z + 1
    #'x' stores the input of the user, asking to enter the month number.
    x = input('Enter the month number: ')
    #uses if-else statements to check whether the user input matches 1 of the 12 month numbers. 
    #If the input matches to the month number, it will print the number of days of the corresponding month number.
    if x == '1':
   
        print(months.get('1'))
    elif x == '2':
        y = str(input("Is it a leap year? (Y/N) : \n")).upper()
        if y == 'N' :
            print(months.get('2'))
        elif y == 'Y' :
            print(months.get('13'))
        else:
            print('You have entered an invalid input, please try again.')
    elif x == '3' :
        print(months.get('3'))
    elif x == '4':
        print(months.get('4'))
    elif x == '5':
        print(months.get('5'))
    elif x == '6':
        print(months.get('6'))
    elif x == '7':
        print(months.get('7'))
    elif x == '8':
        print(months.get('8'))
    elif x == '9':
        print(months.get('9'))
    elif x == '10':
        print(months.get('10'))
    elif x == '11':
        print(months.get('11'))
    elif x == '12':
        print(months.get('12'))
    #If the input does not match any of the month numbers, it will display the message below. The loop will continue even after it will display the message below.
    else :
        print("You have entered an invalid output, please try again.")
#When the loop is completed, the user has inputted 10 times, that displays the message below.   
print('You have entered 10 times, thank you for participating!')