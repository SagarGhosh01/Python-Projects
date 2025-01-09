from os.path import defpath


def guess_name(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Hurray!! You gave the correct answer")
            score += 1
            still_guessing = False
        else:
            if attempt < 2:
                guess =input("Sorry, Try again..")
            attempt += 1

    if attempt == 3:
        print("The correct answer was: ",answer )

score = 0
print("!!! ---- Welcome To Python Quiz ----!!!")
guess_1 = input("Which is the keyword used for declaring a function :")
guess_name(guess_1, "def")

guess_2 = input("What is the datatype for 123.7 :")
guess_name( guess_2, "float")

guess_3 = input("Who is the father of python? :")
guess_name(guess_3,"Van rossum")

print("Your score is: ", str(score))