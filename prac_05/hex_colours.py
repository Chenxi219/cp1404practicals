COLOUR_TO_HEX = {"AliceBlue": "#f0f8ff", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "Apricot":
    "#fbceb1", "Aqua": "#00ffff", "Asparagus": "#87a96b", "Beaver": "#9f8170", "Beige": "#f5f5dc", "Bistre": "#3d2b1f"}
colour_name = input("Enter a colour name: ").strip().lower()
while colour_name != "":
    try:
        hex_code = COLOUR_TO_HEX[colour_name.title()]
        print(f"{colour_name.title()} is {hex_code}")
    except KeyError:
        print("Invalid color name")
    colour_name = input("Enter a colour name: ").strip().lower()