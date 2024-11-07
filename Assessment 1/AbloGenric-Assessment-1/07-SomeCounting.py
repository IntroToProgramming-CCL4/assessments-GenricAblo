input("Click Enter to being the first loop: \n0 -> 50 in increments of 1") #Input functions are used to display loops one by one.
 #loop begins at 0 and counts up in increments of 1 until 50
for x in range(0, 51, 1):
    print(x)

input("Click Enter for the next loop to begin: \n50 -> 0 in decrements of 1")
#loop begins at 50 down to 0 in decrements of 1
for x in range(50, -1, -1) :
    print(x)
    
input("Click Enter for the next loop to begin: \n30 -> 50 in increments of 1")
#loop begins at 30 until 50 in increments of 1
for x in range(30, 51) :
    print(x)

input("Click Enter for the next loop to begin: \n50 -> 10 in decrements of 2")
#loop begins at 50 down to 10 in decrements of 2
for x in range(50, 9, -2):
    print(x)

input("Click Enter for the next loop to begin: \n100 -> 200 in increments of 5")
#loop begins at 100 up to 200 in increments of 5
for x in range(100, 205, 5):
    print(x)

print(" ")
#Final message for the user.
input("Thank you for participating:)")
