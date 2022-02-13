WELCOME_MESSAGE = "Welcome to my computer quiz!"
PLAY_PERMESSION = "Do you want to play?"
CORRECT_MESSAGE = "Correct!"
WRONG_MESSAGE = "Wrong!"
LEAVING_MESSAGE = "Have a good day."
STARTING_MESSAGE = "Oky, Let's play :)"

print(WELCOME_MESSAGE)

playing = input(f"{PLAY_PERMESSION} ")
active_score = 0
score = 0

def quiz(question, answer):
    global score, active_score

    userAnswer = input(f"{question} ? ").lower()

    if userAnswer == answer.lower():
        score += 1
        active_score += 1
        print(CORRECT_MESSAGE)
    else:
        active_score = 0
        print(WRONG_MESSAGE)

    if active_score >= 3:
        print(f"Keep Going you just answered {active_score} questions correct in the row")

if playing.lower() != "yes":
    print(LEAVING_MESSAGE)
    quit()

print(STARTING_MESSAGE)

quiz("What is software?","Instructions that tell the hardware what to do")
quiz("The computer's main circuit board is called a","motherboard")
quiz("RAM is like a computer's","short-term memory/long-term memory")
quiz("What does GPU stand for","graphics proccessing unit")
quiz("What is an Ethernet port used for","Connecting to the Internet")

print(f"Your score is {str(score)}")