MINIMUM_SCORE = 0
PASS_THRESHOLD = 50
MAXIMUM_SCORE = 100
PASSABLE_SCORE = 90

score = float(input("Enter score: "))
if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
    print("Invalid score")
elif score < PASS_THRESHOLD:
    print("Bad")
elif score < PASSABLE_SCORE:
    print("Passable")
else:
    print("Excellent")