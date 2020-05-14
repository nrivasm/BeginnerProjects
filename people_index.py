def what_to_do():
    print("Do you want to search or add? S/A:")
    ans = input()
    if ans.upper() == "S":
        search_for_user()
    elif ans.upper() == "A":
        add_a_user()
    else:
        print("Sorry! That's not a valid input.")
        what_to_do()

def search_for_user():
    print("What is the surname of the user?")
    ans = input().lower()
    file = open(ans + ".txt", "r")
    print("\n" + file.read())
    file.close()
    what_to_do()

def add_a_user():
    print("Okay let's start!\nFirst give me the name of the user:")
    n = input().strip()
    print("Great!\nNow give me a surname:")
    s = input().strip()
    print("Now, give me an age:")
    a = input().strip()
    print("Lastly give me a birthday:")
    b = input().strip()
    print("We're done, user registered successfully!")
    file = open(s.lower() + ".txt", "w+")
    file.write("Name: " + n.title())
    file.write("\nSurname: " + s.title())
    file.write("\nAge: " + a)
    file.write("\nBirthday: " + b)
    file.lose()
    what_to_do()

what_to_do()
