username = input("Enter your username (cannot contain: spaces; digits; must be less than 12 characters): ")

if len(username) >= 12:
    print("Your username is too long. Please try again.")
elif not username.isalpha() :
    print("Only letters are allowed. Please try again.")
else:
    print(f"Welcome {username}!")
