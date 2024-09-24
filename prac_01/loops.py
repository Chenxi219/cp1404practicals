for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c
stars = "*"
number_of_stars = int(input("Numbers of stars: "))
print(stars * number_of_stars)

# d
stars = "*"
number_of_stars = int(input("Numbers of stars: "))
for i in range(1, number_of_stars + 1):
    print(i * stars)