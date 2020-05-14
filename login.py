def commands():
    pword = input("Enter admin password:")
    file = open("apass.txt", "r")
    if pword in file:
        file.close()
        command = input("Command:")
        if command == ".deluser":
            user = input("Name of the user:")
            file = open("users.txt", "r")
            f_lines = file.readlines()
            file.close()
            if user + "\n" in f_lines:
                user = user + "\n"
            if user in f_lines:
                num = f_lines.index(user)
                f_lines.remove(user)
                file = open("users.txt", "w")
                file.writelines(f_lines)
                file.close()
                file = open("pass.txt", "r")
                f_lines = file.readlines()
                f_lines.remove(f_lines[num])
                file.close()
                file = open("pass.txt", "w")
                file.writelines(f_lines)
                file.close()
                print("User removed")
                login()
            else:
                print("User doesn't exist")
                login()
    else:
        print("Wrong password")
        commands()


def login():
    f_text = open("ftime.txt", "r")
    if "not" in f_text:
        f_text.close()
        users_file = open("users.txt", "r")
        users = users_file.readlines()
        file = open("pass.txt", "r")
        pwrds = file.readlines()
        user = input("Login page\nUSERNAME:")
        if user.lower() == ".commands":
            commands()
        elif user + "\n" in users or user in users:
            pwrd = input("PASSWORD:")
            if pwrd + "\n" in pwrds:
                pwrd = pwrd + "\n"
            if user + "\n" in users:
                user = user + "\n"
            if pwrds[users.index(user)] == pwrd:
                print("Access granted")
                users_file.close()
                file.close()
            else:
                print("Wrong password")
                login()
                users_file.close()
                file.close()
        else:
            ans = input("That user doesn't exist do you want to try again or register?").lower()
            if ans == "try again":
                login()
                users_file.close()
                file.close()
            elif ans == "register":
                register()
                users_file.close()
                file.close()
            else:
                print("That's not a valid answer!")
                login()
                users_file.close()
                file.close()
    else:
        f_text.close()
        f_text = open("ftime.txt", "w")
        f_text.write("not")
        admin_pass = input("ADMIN PASSWORD:")
        f_a_pass = open("apass.txt", "w")
        f_a_pass.write(admin_pass)
        f_text.close()
        f_a_pass.close()
        login()


def register():
    user = input("Registration page\nUSERNAME:")
    file = open("users.txt", "r+")
    users = file.read().splitlines()
    if user in users:
        print("That user already exists!")
        file.close()
        login()
    else:
        pwrds = open("pass.txt", "a")
        file.write("\n" + user)
        file.close()
        p1 = input("PASSWORD:")
        p2 = input("CONFIRM PASSWORD:")
        if p1 == p2:
            pwrds.write("\n" + p1)
            pwrds.close()
            login()
        else:
            print("Failed password confirmation, restarting")
            pwrds.close()
            register()

login()
