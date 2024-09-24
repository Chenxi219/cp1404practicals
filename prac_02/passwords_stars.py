def get_password():
    global min_length
    min_length = 5


get_password()

def main():
    password = input("Enter a password: ")
    determine_password(password)
    print('*' * len(password))

def determine_password(password):
    while len(password) <= min_length:
        print("Password must more than five")
        password = input("Enter a password: ")
    return password
main()