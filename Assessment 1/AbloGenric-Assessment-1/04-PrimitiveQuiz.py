#Created variables for the number of correct answers and messages for correct and incorrect answers.
correct_answers = 0
correct_message = "Congratulations! You have "
incorrect_message = "Nice Try!"
    #introduces the quiz and what it's about
print("hello, this is a simple quiz to test you on your knowledge on capitals of europe. To pass the test you will need at least 5 correct answers")
    #asks for the user input in the same line as the question.
answer = input("First question is what is the capital of France? : ")
  #created a conditional statement that states that if the user input matches the correct answer, it will print out the appropriate message and the amount of correct answers they have.
if (answer).lower() == "paris".lower(): #the .lower() line of code is what helps ignore the capitalization from the user input. for example : PaRis or PArIS.
    correct_answers = correct_answers + 1 #this line will add up the number of correct answers throughout the whole game and will be different in the beginning.
    print(f"{correct_message} {correct_answers} correct answer")
else : #if the answer DOESN'T match  the correct answer it will display the value of the incorrect message value.
    print(incorrect_message)
    #The same thing will happen throughout the next set of questions
answer = input("Question 2: What is the capital of Germany? : ")
if answer.lower() == "berlin".lower():
    correct_answers = correct_answers + 1
    print(f" {correct_message} {correct_answers} correct answers")
else :
    print(incorrect_message)
answer = input("Question 3: What is the capital of Ireland? : ")
if str(answer).lower() == "dublin".lower():
    correct_answers = correct_answers + 1
    print(correct_message + str(correct_answers) + " correct answers")
else :
    print(incorrect_message)
answer = input("Question 4: What is the capital of Spain? : ")
if str(answer).lower() == "madrid".lower():
    correct_answers = correct_answers + 1
    print(correct_message + str(correct_answers) + " correct answers")
else :
    print(incorrect_message)
answer = input("Question 5: What is the capital of Russia? : ")
if str(answer).lower() == "moscow".lower():
    correct_answers = correct_answers + 1
    print(correct_message + str(correct_answers) + " correct answers")
else :
    print(incorrect_message)
answer = input("Question 6: What is the capital of Norway? : ")
if str(answer).lower() == "oslo".lower():
    correct_answers = correct_answers + 1
    print(correct_message + str(correct_answers) + " correct answers")
else :
    print(incorrect_message)
answer = input("Question 7: What is the capital of Italy? : ")
if str(answer).lower() == "rome".lower():
    correct_answers = correct_answers + 1
    print(correct_message + str(correct_answers) + " correct answers")
else :
    print(incorrect_message)
answer = input("Question 8: What is the capital of Austria? : ")
if str(answer).lower() == "vienna".lower():
    correct_answers = correct_answers + 1
    print(correct_message + str(correct_answers) + " correct answers")
else :
    print(incorrect_message)
answer = input("Question 9: What is the capital of Hungary? : ")
if str(answer).lower() == "budapest".lower():
    correct_answers = correct_answers + 1
    print(correct_message + str(correct_answers) + " correct answers")
else :
    print(incorrect_message)
answer = input("Final Question: What is the capital of the United Kingdom? : ")
if str(answer).lower() == "london".lower():
    correct_answers = correct_answers + 1
    print(correct_message + str(correct_answers) + " correct answers")
else :
    print(incorrect_message)

if correct_answers < 5 : #This conditional statement states that if the user has a final score that is lower than 5, it will show a unique message.
    print("Unlucky, You can try again next time!")
elif correct_answers == 10 : #This adds another condition that if the user answers all 10 questions correctly, it will also show a unique message.
    print("Congratulations! You have a perfect score! your prize is NOTHING YAY.")
else : #This last statement shows that if these two statements were not met, it will display a different message.
    print("Congratulations you have completed the quiz with " + str(correct_answers)+ " correct answers")
