import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 1? 16
# What was the smallest number you could have seen, what was the largest?  samllest: 5, largest: 20

# What did you see on line 2? 9
# What was the smallest number you could have seen, what was the largest? smallest: 3, largest: 9
# Could line 2 have produced a 4?  No

# What did you see on line 3? 3.450544101099552
# What was the smallest number you could have seen, what was the largest?  smallest: 2.5, largest: 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(0, 100))
