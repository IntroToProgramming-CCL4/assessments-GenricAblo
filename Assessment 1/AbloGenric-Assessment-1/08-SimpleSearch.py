names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
user_search = input("Who are you searching for?: \n")

if user_search in names:
    print(f"{user_search} is part of the list.")
else:
    print(f"{user_search} is not in the list")