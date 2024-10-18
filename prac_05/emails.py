"""
Emails
Estimate: 20 minutes
Actual:   21 minutes
"""
email_name = {}
email = input("Email: ")
while email != "":
    local_part = email.split("@")[0]
    name_part = local_part.split(".")
    name = " ".join(name_part).title()
    is_correct = input(f"Is your name {name}? (Y/n)").upper()
    if is_correct != "" and is_correct != "Y":
        name = input("Name: ")
    email_name[email] = name
    email = input("Email: ")
for email, name in email_name.items():
    print(f"{name} {email}")
