import os
import json


class User:
    def __init__(self):
        self.name = None
        self.login = None
        self.password = None
        self.age = None
        self.file_name = "user.json"
        self.logged_in = False

    # ------------------ Main Function -------------------- #

    def entering_system(self):
        self.clear_()
        if self.logged_in is False:
            self.show_init_message()
            self.input_options = ["1", "2"]
            init_input = input("Select one of these options [1/2]: ").strip()
            while init_input not in self.input_options:
                self.clear_()
                print("Invalid input! Please select one of these option [1/2]")
                init_input = input("Select one of these options [1/2]: ").strip()

            self.clear_()
            if init_input == self.input_options[0]:
                self.register()
            else:
                self.log_in()
            self.logged_in = True
        else:
            print("You are already in the system")

    def register(self):
        input_name = input("Name: ").strip().capitalize()
        while not input_name.isalpha() or len(input_name) < 3:
            self.clear_()
            self.invalid_input_message("name")
            input_name = input("Name: ").strip().capitalize()

        input_login = input("Login: ").strip()
        while not input_login.isalnum() or self.login_exists(input_login):
            self.clear_()
            self.invalid_input_message("login")
            input_login = input("Login: ").strip()

        input_password = input("Passoword: ").strip()
        check_password = input("Confirm Password: ").strip()
        while self.string_empty(input_password) or input_password != check_password or len(input_password) < 6:
            self.clear_()
            self.invalid_input_message("password")
            input_password = input("Passoword: ").strip()
            check_password = input("Confirm Password: ").strip()

        input_age = input("Age: ").strip()
        while not input_age.isnumeric() or int(input_age) < 12 or int(input_age) > 120:
            self.clear_()
            self.invalid_input_message("age")
            input_age = input("Age: ").strip()

        self.name = input_name
        self.login = input_login
        self.password = input_password
        self.age = input_age

        self.write_to_file()

    def log_in(self):
        pass

    def log_out(self):
        pass

    def login_update(self):
        pass

    def password_update(self):
        pass

    def delete_account(self):
        pass

    # ----------------- Secondary Functions --------------- #

    def write_to_file(self):
        if self.file_empty():
            self.clear_file()

        user_dict = {
            "name": self.name,
            "login": self.login,
            "password": self.password,
            "age": int(self.age)
        }

        with open("user.json", 'a') as file:
            json.dump(user_dict, file)
            file.write(os.linesep)

    def clear_file(self) -> None:
        file = open(self.file_name, "w")
        file.write("")
        file.close()

    def login_exists(self, input_login) -> bool:
        if self.file_empty():
            return False

        people = self.get_all_users()
        for user in people:
            if input_login == user["login"]:
                return True
        return False

    def get_all_users(self):
        text = self.get_text_from_file()

        def get_all_users(self):
            text = self.get_text_from_file()

        list_of_users = text.split("\n")

        # return [json.loads(list_of_users[0]), json.loads(list_of_users[1]), json.loads(list_of_users[2])]
        result = []
        for row in list_of_users:
            zet = json.loads(row)
            result.append(zet.copy())
        return result
        # list_of_users = text.split("\n")

        # return [json.loads(list_of_users[0]), json.loads(list_of_users[1]), json.loads(list_of_users[2])]
        result = []
        for row in list_of_users:
            zet = json.loads(row)
            result.append(zet.copy())
        return result

    def file_empty(self):
        if not self.get_text_from_file().strip():
            return True
        return False

    def get_text_from_file(self) -> str:
        file = open(self.file_name)
        text = file.read()
        file.close()
        return text

    def clear_(self) -> None:
        os.system("clear")

    def string_empty(self, str_):
        return not str_.strip()

    # ------------------ Message Functions ---------------- #

    def show_init_message(self) -> None:
        print("""
        Entering the System:
        Register    [1]
        Login       [2]
        """)

    def invalid_input_message(self, input_="name"):
        if input_ == "name":
            print("Invalid input! Please try again")
        elif input_ == "login":
            print("Invalid input! Possible errors: ")
            print("User exists")
        elif input_ == "password":
            print("Invalid input. Possible errors: ")
            print("Password(s) is/are empty")
            print("Password contain at least 6 characters")
            print("Passwords don't match")
        elif input_ == "age":
            print("Invalid input! Please try again")
            print("Age must be number")
            print("Your age should be in this range: [12-120]")


user = User()
user.entering_system()