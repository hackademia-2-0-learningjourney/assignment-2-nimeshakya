import json


def get_choice():
    print("\n1 - Sign In\n2 - Sign Up\n3 - Exit")
    while True:
        try:
            choice = int(input("> "))
            if choice == 1 or choice == 2 or choice == 3:
                return choice
            print("Enter 1, 2 or 3")
        except ValueError:
            print("Enter 1, 2 or 3")


def get_json_data():
    try:
        with open("users.json", "r+") as f:
            users_json = json.load(f)
            return users_json
    except FileNotFoundError:
        return None


def check_if_user_exists(username):
    user_exists = False
    try:
        with open("users.json") as f:
            users_data = json.load(f)
            for user in users_data["users"]:
                if user["username"] == username:
                    user_exists = True
                    break
    except FileNotFoundError:
        print("Error...")
    return user_exists


def sign_in():
    success = True
    users_data = get_json_data()
    if not users_data:
        print("No users data file exist! Please sign up to create data file with new entry!")
        return not success
    users = users_data["users"]
    curruser = {"username": input("Username: "), "password": input("Password: ")}
    loggedIn = False
    for user in users:
        if (
            user["username"] == curruser["username"]
            and user["password"] == curruser["password"]
        ):
            print("Welcome!")
            print(f"Phone number of {curruser['username']} is {user['phone']}")
            loggedIn = True
            break
    if not loggedIn:
        print("Wrong credentials! Exiting...")
        return not success

    success = loggedIn
    return success


def sign_up():
    users_data = get_json_data()
    # create a new users.json file if there is not already
    if not users_data:
        # get the users data from newly created file
        users_data = create_users_datafile()

    newUser = {
        "username": input("Username: "),
        "password": input("Password: "),
        "phone": input("Phone: "),
    }

    user_exists = check_if_user_exists(newUser['username'])
    if (user_exists):
        print(f"User {newUser['username']} already exists! Please choose another username!")
        return

    with open("users.json", "w") as f:
        users_data["users"].append(newUser)
        json.dump(users_data, f)


def create_users_datafile():
    with open("users.json", "w") as f:
        json.dump({"users": []}, f)
    with open("users.json", "r") as f:
        users_data = json.load(f)
        return users_data


def main():
    print("WELCOME TO THE GREATEST AUTH SYSTEM!")
    quit = False
    while not quit:
        opt = get_choice()
        if opt == 3:
            print("Exiting...")
            quit = True
        if opt == 1:
            # quit if not signed in
            quit = not sign_in()
        if opt == 2:
            sign_up()


if __name__ == "__main__":
    main()

