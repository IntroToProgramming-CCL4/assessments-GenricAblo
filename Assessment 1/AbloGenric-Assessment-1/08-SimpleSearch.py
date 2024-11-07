# Function to search for a string in a list of names
def search_name(name_list, search):
    if search in name_list:
        return f"'{search}' is in the list."
    else:
        return f"'{search}' is in the list."

# Main function
def main():
    #list of names
    names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

    # Asks for an input for the user
    search = input("Enter the name you are looking for: ")

    # Call the search function and print the result
    result = search_name(names, search)
    print(result)

# Run the main function
if __name__ == "__main__":
    main()
