#Function to check if a number is even or odd
def check_even_or_odd(num):
    if num % 2 == 0:
        return "Number is even."
    else:
        return "Number is odd."

#main function
def main():
    # Asks the user for a number
    try:
        num = int(input("Please enter a number: "))
        # Call the check_even_odd function and print the result
        result = check_even_or_odd(num)
        print(result)
    except ValueError:
        print("Incorrect, enter a valid number.")

# runs the main function
if __name__ == "__main__":
    main()
