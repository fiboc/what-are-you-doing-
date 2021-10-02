import math
############################# 1 masala ############################
# num = int(input())
# [print("* "*i) for i in range(num, 0, -1)]

############################# 2 masala ############################
# mkdir --> papka ochish
# touch --> yangi file yaratish
# nano --> compleyer
# cd --> papkaga kirish
# rm --> o'chirish

############################# 3 masala ############################
# son = input()
# son = son[::-1]
# print(int(son))

############################# 4 masala ############################
# a, b = input(), input()
# print(a[:len(a)//2] + b + a[len(a)//2:])

############################# 5 masala ############################
# row = input()
# print(row.lower().strip())

############################# 6 masala ############################
# gap = input()
# gap = gap.split()
# print(' '.join(gap[::-1]))

############################# 7 masala ############################
# [print(value) for value in range(20, 100) if not value % 7]

############################# 8 masala ############################
# [print(value) for value in reversed(range(20, 100)) if not value % 7]
# or
# [print(value) for value in range(100, 20, -1) if not value % 7]

############################# 9 masala ############################
# soz = input()
# print('Palindrome') if soz == soz[::-1] else print("Not palindrome")

################################### 10 masala ############################
# def kvadrat(a):
#     a = [val**2 for val in a]
#     return a

# c = [1, 2, 3, 4, 5]

# result = kvadrat(c)

# print(result)

######################### 11 masala ##################################
# def bor_val(num1, num2):
#     num1 = [val for val in num1 if val in num2]
#     return num1
#
# a = [2, 3, 1, 5, 4]
# b = [5, 0, -2, 3]
#
# result = bor_val(a, b)
#
# print(result)

######################### 12 masala ##################################
# def no_val(num1, num2):
#     num1.extend(num2)
#     num1 = [val for val in num1 if num1.count(val) == 1]
#     return num1
#
# a = [2, 3, 1, 5, 4]
# b = [5, 0, -2, 3]
#
# result = no_val(a, b)
#
# print(result)

######################### 13 masala ##################################
# def sanoq(num):
#     b = [val if num.count(val) == 1 else num.remove(val) for val in num]
#     return len(b)
#
# a = [2, 3, 1, 4, 3, 2, 8, 9]
#
# result = sanoq(a)
# print(result)

######################### 14 masala ##################################
# *args
# xoxlagancha qiymat oladi va tuple qiymatida qabul qiladi

######################### 15 masala ##################################
# **kwargs
# xoxlagancha qiymat qabul qiladi,
# keylar bilan bersa bo'ladi,
# dictionary bo'ladi

# class Rectangle:
#     def __init__(self, eni, boyi):
#         self.eni = eni
#         self.boyi = boyi
#         self.perimetr = (eni+boyi)*2
#         self.yuzi = eni * boyi
#         self.diagonal = math.sqrt(eni*eni+boyi*boyi)
    # eni = float(input("Eni: "))
    # boyi = float(input("Boyi: "))
    #
    # print(f'Perimetr = {(eni + boyi)*2}')
    # print(f'Yuzi = {eni * boyi}')
    # print(f'Diagonal = {math.sqrt(eni*eni + boyi*boyi)}')


# clas1 = Rectangle(3, 4)

# import os
#
#
# class User:
#     def __init__(self):
#         self.name = None
#         self.login = None
#         self.password = None
#         self.init_input_options = ["1", "2"]
#
#         self.tizimga_kirish()
#
#     def tizimga_kirish(self):
#         # Tizimga kirish qismi
#         self.clear_()
#         self.init_message()
#         log_or_reg = input("[1/2]: ").strip()
#
#         while log_or_reg not in self.init_input_options:
#             # kiritilgan malumot 1 yoki 2 ekanligini tekshirish
#             self.hato_bolsa()
#             log_or_reg = input("[1/2]: ").strip()
#
#         if log_or_reg == self.init_input_options[0]:
#             self.register()
#         else:
#             self.log_in()
#
#     @staticmethod
#     def init_message():
#         # ekranga chiqish?
#         print(f"""
#         Register   [1]
#         Login      [2]
#         """)
#
#     # Scott
#     def register(self):
#         # registratsiya qismi
#         self.clear_()
#         input_name = input("Enter name: ").strip().capitalize()
#
#         while not input_name.isalpha():
#             self.hato_bolsa()
#             input_name = input("Enter name: ").strip().capitalize()
#
#         input_login = input("Enter login: ").strip().lower()
#
#         input_password = input("Enter password: ").strip().lower()
#
#     # Login qismi
#     def log_in(self):
#         input_login = input("Enter your login: ").strip().lower()
#         input_password = input("Enter your password : ").strip().lower()
#         self.clear_()
#
#         while input_login != self.login or input_password != self.password:
#             self.clear_()
#             print("Entered login or/and password is not match! Please try again! :")
#             input_login = input("Enter your login: ").strip().lower()
#             input_password = input("Enter your password: ").strip().lower()
#
#     def log_out(self):
#         pass
#
#     def hato_bolsa(self):
#         self.clear_()
#         print("Invalid input! Please try again")
#
#     def clear_(self):
#         os.system("clear")
#
# user = User()
