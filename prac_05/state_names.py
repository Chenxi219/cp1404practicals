"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        max_length = max(len(code) for code in CODE_TO_NAME.keys())
        print(f"{state_code:{max_length}} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
