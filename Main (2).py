#Tyler MacPhee, Integration Project, COP-1500
#Import modules
import turtle
import wikipedia 
#Class creation for question system
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
#I later got rid of this global variable an changed it to a returning variable down below


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

print("Welcome, " + user + ", to my integration project!\nWe'll be enjoying trivia, fun with symbols, and finally watch a turtle draw.")


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
#This allows the user to play around with their own input and create a big, or small table of symbols.
user_row = int(input("\nHow many rows would you like? "))
user_column = int(input("How many columns would you like? "))

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


print("We'll next be allowing you to have three go's at searching whatever you'd like to know... be safe.")
#Making use of a cool module called wiki, does it what you expect it to do.
wikiuser = str(input("What would you like to know more about? - Type an unambiguous keyword or name. "))
#print(wikipedia.search(wikiuser, results = 5))
print(wikipedia.summary(wikiuser, sentences = 2))

wikiuser2 = input("What next? ")

#print(wikipedia.search(wikiuser2, results = 5))
print(wikipedia.summary(wikiuser2, sentences = 2))

wikiuser3 = input("And finally... ")

#print(wikipedia.search(wikiuser3, results = 5))
print(wikipedia.summary(wikiuser3, sentences = 2))



print("\nSo now lets watch a turtle draw some nice shapes for us.")
print("\nPlease note to exit the window after the shape has been completed to continue")
#While looking into graphic applications in Python, I discovered "Turtle"
#A relatively easy to use graphics package
loadWindow = turtle.Screen()
thor = turtle.Turtle()
#I'm now using more than just stating a color, i'm converting my colors to the RGB 255 scale for more accurate colors
turtle.colormode(255)

#Draw speed
thor.speed(0)
#setting shape of turtle
thor.shape("turtle")
#Function that draws continues circles in a figure 8
for i in range(127):
    thor.circle(5*i)
    thor.circle(-5*i)
    thor.left(i)
    b = i
    if b > 51:
        b = 51
    thor.color(i, 2*i, 3*b)

#This function should be a fast generating graphic that goes from black to blue and then to green/light green quickly
turtle.resetscreen()
hex = turtle.Turtle()
hex.speed(0)
num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides*30):
    hex.forward(side_length-5)
    hex.right(angle)
    hex.right(i)



turtle.done()


#This creates a basic hexagon with a twist, a big twist
loadWindow.bye() #Closes window
