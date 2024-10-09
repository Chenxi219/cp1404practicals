import random
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

def main():
    numbers_of_picks = int(input("How many quick picks? "))
    generate_quick_picks(numbers_of_picks)

def generate_quick_picks(numbers_of_picks):
    for i in range(numbers_of_picks):
        quick_picks =[]
        for j in range(NUMBERS_PER_PICK):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join(f"{number:2}" for number in quick_picks))

main()