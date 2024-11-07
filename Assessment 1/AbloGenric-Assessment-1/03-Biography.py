#Displays a message to introduce the user to what is going to happen
input("Hello This is just a simple survey for me to get to know you \n Press Enter to continue.")
#creating variables 
name = input("What is your name? : ")
hometown = input("Where is your hometown? : ")
age_input = input("How old are you? : ")
user_info = {
    "name" : name,
    "hometown" : hometown,
    "age" : age_input}
try:
    age = int(age_input)
except ValueError:
    print("Invalide age input. Enter a valid integer for age.")
    

print(f"Name :  {user_info["name"]} \n Hometown: {user_info["hometown"]} \n Age: {user_info["age"]}")

