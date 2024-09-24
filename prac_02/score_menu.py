import random
MENU = ("(G)et a valid score (must be 0-100 inclusive)\n(P)rint result (copy or import your function to determine the result from score.py)\n(S)how stars (this should print as many stars as the score)\n(Q)uit")
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
PASS_THRESHOLD = 50
PASSABLE_SCORE = 90

def main():
    score = int(input("Enter score: "))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))
            determine_score(score)
        elif choice == "P":
            feedback = print_feedback(score)
            print(feedback)
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye")

def determine_score(score):
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Score must between 0 and 100")
        score = int(input("Enter score: "))
    return score

def print_feedback(score):
    if score < PASS_THRESHOLD:
        return "Bad"
    elif score < PASSABLE_SCORE:
        return "Passable"
    else:
        return "Excellent"

main()