# V1
# class Bosh:
#     pass

# V2
# class Bosh_func:
#     def __init__(self):
#         pass

# V3
# class Car:
#     def __init__(self, nimadir):
#         pass

# V4
# class Show:
#     def show(self):
#         print('"salom"')

# V5
# class Animal:
#     def __init__(self, param1, param2):
#         self.param1 = param1
#         self.param2 = param2

# V6
# class Param_med:
#     def __init__(self, par1, par2, par3, par4, par5, par6, par7):
#         pass
#     def med2(self):
#         pass
#     def med3(self):
#         pass
#     def med4(self):
#         pass
#     def med5(self):
#         pass

# V7
# class Car:
#     def __init__(self, name, speed, year):
#         pass
#     def start(self):
#         pass
#     def stop(self):
#         pass
#     def turn_right(self):
#         pass
#     def turn_back(self):
#         pass
#
# car1 = Car("BMW", 2020, 300)
# car2 = Car('Porsche', 2019, 270)
# car3 = Car("Audi", 2021, 290)
# car4 = Car("Mustang", 2018, 240)
# car5 = Car("Lexus", 2020, 260)

# V8
# class Talaba:
#     def __init__(self, ism, familiya, baho):
#         self.name = ism
#         self.surname = familiya
#         self.baho = baho
#
# talaba1 = Talaba("Eshmat", "nimadir", 5)
# talaba2 = Talaba("Toshmat", "nimadir", 4)
# talaba3 = Talaba("G'ishmat", "nimadir", 3)
#
# hamma = [talaba1, talaba2, talaba3]
# min = talaba1.baho
#
# for person in hamma:
#     if person.baho < min:
#         min = person.baho
#
# print([person.name for person in hamma if min == person.baho])

# V9
# class Human:
#     def __init__(self, name, age, profession, height, weight, single):
#         self.name = name
#         self.age = age
#         self.profession = profession
#         self.height = height
#         self.weight = weight
#         self.single = single
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def get_profession(self):
#         return self.profession
#
#     def get_height(self):
#         return self.height
#
#     def get_(self):
#         return self.name
#
#     def get_weight(self):
#         return self.weight
#
#     def get_single(self):
#         return self.single

# V10
# class Bino:
#     def __init__(self, balandligi, rangi):
#         self.height = balandligi
#         self.color = rangi
#
# bino1 = Bino(45, "qora")
# bino2 = Bino(56, 'oq')
# bino3 = Bino(34, "ko'k")
#
# hamma_bino = [bino1, bino2, bino3]
#
# for bino in hamma_bino:
#     if bino.height > 50:
#         print(bino.color)

# V11
# class Human:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def full_name(self):
#         return str(self.first_name + self.last_name)

# V12
# class Nootbook:
#     def __init__(self, firma, model, CPU, DDR, price):
#         self.firma = firma
#         self.model = model
#         self.CPU = CPU
#         self.DDR = DDR
#         self.price = price
#
#         self.info_notebook()
#
#     def info_notebook(self):
#         print(f"""
#     Firmasi: {self.firma}, modeli: {self.model}, CPUsi: {self.CPU} DDRi: {self.DDR} price: {self.price}
#     """)
#
# nootbook1 = Nootbook("acer", 'acer', 'bilmadim', 'bilmadim', 'bilmadim')

# V13
# class Ochirish:
#     def __init__(self, my_list):
#         self.my_list = my_list
#
#     def delete_ast_item(self):
#         if self.my_list:
#             self.my_list.pop()
#             return self.my_list
#
# list1 = [1, 2, 3, 4, 5]
#
# lis = Ochirish(list1)
#
# if list1:
#     print(lis.delete_ast_item())

# V14
# class First_del:
#     def __init__(self, numbers):
#         self.numbers = numbers
#
#     def delete_first_items(self):
#         if self.numbers:
#             self.numbers.pop(0)
#             return self.numbers
#
# list1 = [1, 2, 3, 4, 5]
#
# nimadir = First_del(list1)
#
# print(nimadir.delete_first_items())

# V15
