"""
Guitar Test
Estimate: 15 minutes
Actual:   17 minutes
"""
from prac_06.guitar import Guitar
def main():
    guitar = Guitar("Gibson L-5 CES", 1992, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 2398.80)

    print(f"{guitar.name} get_age() - Expected {guitar.get_age()}. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {another_guitar.get_age()}. Got: {another_guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {guitar.is_vintage()}. Got: {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected {another_guitar.is_vintage()}. Got: {another_guitar.is_vintage()}")

main()
