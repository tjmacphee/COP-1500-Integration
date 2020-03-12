class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

user = input("What is your name? ")
while True:
    if user.isalpha():
        break
    else:
        print("No numbers or symbols please")
        user = input("What is your name ? ")


# Initialization stuff
total_score = 0  # The global variable that keeps track of the total score throughout the game.


def run_test(question_list):
    """
    Function that tests the user given a list of questions.
    :param question_list: A list of questions

    :return: The score achieved for this round of questions.
    """
    current_score = 0
    for question in question_list:
        answer = input(question.prompt)
        if answer == question.answer:
            current_score += 1
    print("You got " + str(current_score) + "/" + str(len(question_list)) + " correct")
    return current_score
##Had help from a youtube video on this,
#https://www.youtube.com/watch?v=SgQhwtIoQ7o

print("Welcome, " + user + ", to my integration project!\nWe'll be engaging in some classic trivia, followed by,\n"
      "a dictionary for python.")
answer = input("Continue? Type Y/N: ")
while answer != "Y":
    print("Sorry, but you wont be able to advance further unless you type Y.")
    answer = input("Continue? Type Y/N: ")
# This can let me manipulate user input to only allow the following code to be executed when the answer is "Y"

print("Ok, " + user + ", today we will be going through four topics, with 3 questions each.")
print("First, we'll be begin with 2000's Movies")
# I created a file that contains some rules so i can do things a little easier without interfering with my own code
# from Question import Question

question_prompts = [
    "What movie features the great adventure of a lone robot?\n (A) Robo dog's escape\n (B) Wall-E\n (C) Tomorrowland\n (D) Jimmy Neutron\n\n",
    "Who was Cpt. Jack Sparrow in the hit movie series Pirates of the Caribbean?\n (A) Johnny Depp\n (B) Tom Cruise\n (C) George Clooney\n (D) Will Smith\n\n",
    "Who won at the end of The Dark Knight?\n (A) Batman\n (B) Joker\n (C) Harley Quinn\n (D) No one, this movie is a cliffhanger.\n\n",
]

questions = [
    Question(question_prompts[0], "B"),
    Question(question_prompts[1], "A"),
    Question(question_prompts[2], "A"),
]

# I'm keeping track of their score and adding 1 to it each time they get one correct
total_score += run_test(questions)

print("Alright, round 2 will be asking questions about basic math")
question_prompts2 = [
    "What would be the answer if I took 20% of 365?\n (A) 64.53\n (B) 73\n (C) 18.25\n\n",
    "A mile is 5,280 feet, a plane is flying at at 400mph: How many miles does the plane travel every 10 seconds?\n (A) .93\n (B) .1\n (C) This sucks :(\n\n",
    "What is the cube root of 50, divided by 18, then rounded to the nearest whole number?\n (A) 13\n (B) 9\n (C) 0\n (D) Can't be simplified.\n\n",
]

questions2 = [
    Question(question_prompts2[0], "B"),
    Question(question_prompts2[1], "B"),
    Question(question_prompts2[2], "C"),
]

total_score += run_test(questions2)

print("Okay, final round! This time, it won't be multiple choice, good luck! (Answers are case-sensitive)")
question_prompts3 = [
    "My first name in binary code is this - |01010100|01111001|01101100|01100101|01110010|00001101|\nWhat's my name?: ",
    "I'm hotter the more you feed me, but die if you give me a drink.\nWhat am I?: ",
    "If you mix blue and orange paint together, what color is the result?: ",
]

questions3 = [
    Question(question_prompts3[0], "Tyler"),
    Question(question_prompts3[1], "Fire" or "Phone"),
    Question(question_prompts3[2], "Brown"),
]

total_score += run_test(questions3)

if (total_score) >= 4.5:
    print("Congratulations!, " + user + ", you earned a total score of: " + str(total_score) + "/9" + " correct!")
else:
    print("Well, " + user + ", you still got a score of: " + str(total_score) + "/9" + " correct, better luck next time!")
print("Thanks for playing!\nGoodbye.\n\n")

print("The next part of the program will be about the arrangement of symbols")
print("This is a just a test for you to get the feel of how it works.")

user_row = int(input("\nHow many rows would you like? "))
user_column =  int(input("How many columns would you like? "))
for y in range(user_row):
    for y in range(user_column):
        print(end = " * ")
    print()
print("\nNow we can play around with it a little more...")
print("I took whatever you entered for the numbers, then printed out a display of what that looks like in terms of asteriks.")

user_row2 = int(input("How many rows would you like? "))
user_column3 = int(input("How many columns would you like? "))
user_choice = input("Type the kind of symbol you would like, or anything words you'd like. ( * , # , ! , etc.): ")
for y in range(user_row2):
    for y in range(user_column3):
        print(end = user_choice + " ")
    print()
print("\nThis should be a little more obvious, but I did the same thing, but printed whatever you wanted instead of just asteriks.")
print("\nSo I have a challenge for you", + user + ": Guess the country by their flag.")
stars = "*"
lines = "~"
for y in range(20):
    if stars < 10:
        print(stars)
    else:
        print(lines)








#my_dictionary = ("Variable" = "A place to store information.",
           #      "Keyword" = "A reserved name in Python that has a specific function",
            #     "While" = "Boolean statement that tests if something is true or false, a loop.",
            #     "String" = "Something in quotations that can be printed/tested")




