
# name
# login
# password
# age
# single
import os
import platform
import json
import getpass


class User:
    def __init__(self):
        self.name = None
        self.login = None
        self.password = None
        self.age = None
        self.single = True
        self.min_age = 12
        self.max_age = 150
        self.file_name = "user.txt"
        self.user_logged_in = False

        self.tizimga_kirish()

    def tizimga_kirish(self) -> None:
        self.init_message()
        if self.user_wants_register():
            self.register()
        else:
            self.log_in()

    @staticmethod
    def init_message() -> None:
        print("""
        Tizimga kirish:
        Register    [1]
        Login       [2]
        """)

    def user_wants_register(self) -> bool:
        init_input = input("[1/2]: ").strip()
        input_options = ["1", "2"]
        while init_input not in input_options:
            self.clear_everything()
            print("Invalid input. Please select one of the options below")
            init_input = input("[1/2]: ").strip()
        return True if init_input == "1" else False

    def register(self) -> None:
        self.clear_everything()
        input_name = input("Name: ").strip().capitalize()
        while not input_name.isalpha():
            self.clear_everything()
            print("Invalid input. Name should only contain alphabet characters")
            input_name = input("Name: ").strip().capitalize()

        input_login = input("Login: ").strip().lower()
        while not input_login.isalnum() or self.login_exists(input_login):
            self.clear_everything()
            print("Invalid input. Possible errors:")
            print("- Login is empty")
            print("- Login should contain only alphanumeric characters")
            print("- This user exists")
            input_login = input("Login: ").strip().lower()

        input_password = getpass.getpass("Password (hidden): ").strip()
        check_password = getpass.getpass("Confirm Password (hidden): ").strip()
        while self.is_str_empty(input_password) or input_password != check_password:
            self.clear_everything()
            print("Invalid input. Possible errors:")
            print("- One of the inputs is empty")
            print("- Passwords don't match")
            input_password = getpass.getpass("Password (hidden): ").strip()
            check_password = getpass.getpass("Confirm Password (hidden): ").strip()

        input_age = input("Age: ").strip()
        while not input_age.isnumeric() or self.min_age > int(input_age) or int(input_age) > self.max_age:
            self.clear_everything()
            print("Invalid age. Possible errors:")
            print("- Age should be number")
            print(f"- Age should be below 12")
            print(f"- Age should be above 150")
            input_age = input("Age: ").strip()

        self.clear_everything()
        single_options = ["y", "yes", "n", "no"]
        input_single = input("Are you single? [y/n]: ").strip().lower()
        while input_single not in single_options:
            self.clear_everything()
            print("Invalid input. Please select one of the options below: ")
            print(single_options)
            input_single = input("Are you single? [y/n]: ").strip().lower()

        self.name = input_name
        self.login = input_login
        self.password = input_password
        self.age = input_age
        if input_single in single_options[2:]:
            self.single = False
        self.write_to_file()
        self.user_logged_in = True

    def log_in(self):
        """sdfsdfsdf"""
        self.user_logged_in = True

    def log_out(self):
        self.__init__()

    def update_login(self):
        pass

    def update_password(self):
        pass

    def delete_account(self):
        pass

    @staticmethod
    def clear_everything():
        if platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == "Windows":
            os.system("cls")
        else:
            print("What system is that???")
            exit()

    @staticmethod
    def is_str_empty(yozuv: str) -> bool:
        return not yozuv

    def write_to_file(self) -> None:
        file = open(self.file_name, 'a')
        user_info = {
            "name": self.name,
            "login": self.login,
            "password": self.password,
            "age": self.age,
            "single": int(self.single)
        }
        user_info = json.dumps(user_info)
        file.write(user_info + "\n")
        file.close()

    def get_all_users(self) -> list:
        users_ = []
        file = open(self.file_name)
        text = file.read()
        text = text.strip()
        rows = text.split("\n")
        for i in range(len(rows)):
            users_.append(json.loads(rows[i]))

        return users_

    def login_exists(self, current_login):
        if self.file_empty():
            return False
        users_ = self.get_all_users()
        for i in range(len(users_)):
            if current_login == users_[i]["login"]:
                return True
        return False

    def file_empty(self):
        file = open(self.file_name)
        text = file.read()
        text = text.strip()
        file.close()
        return self.is_str_empty(text)

user1 = User()