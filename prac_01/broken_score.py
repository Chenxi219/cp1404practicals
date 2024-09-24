"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
MINIMUM_SCORE = 0
PASS_THRESHOLD = 50
MAXIMUM_SCORE = 100

score = float(input("Enter score: "))
if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
    print("Invalid score")
elif score < PASS_THRESHOLD:
    print("Bad")
elif score < 90:
    print("Passable")
else:
    print("Excellent")