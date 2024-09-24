import random
MINIMUM_SCORE = 0
PASS_THRESHOLD = 50
MAXIMUM_SCORE = 100
PASSABLE_SCORE = 90

def main():
    score = float(input("Enter score: "))
    feedback = print_feedback(score)
    print(feedback)
    random_score = random.randint(0,100)
    print(random_score)
    random_feedback = print_feedback(random_score)
    print(random_feedback)

def print_feedback(score):
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score < PASS_THRESHOLD:
        return "Bad"
    elif score < PASSABLE_SCORE:
        return "Passable"
    else:
        return "Excellent"
main()