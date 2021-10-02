# for row in list1:
#     for value in row:
#         print(value)



# arr1 = [2, 1, -4, -9, 0, -5, 8, 3]
# arr2 = [-4, 0, 2, 9, 6, 1]



# numbers = [
#     [2, 1, 4],
#     [3, 2, 5],
#     [9, 6, 7],
#     [1, 6, 8],
#     [3, 4, 2],
#     [7, 9, 1],
#     [5, 2, 7]
# ]


# numbers = [2, 1, -4, -9, 0, -5, 8, 3]
# 1
# [print(index) for index, _ in enumerate(numbers) if _ < 0]
# 2
# [print(qiy) for index, qiy in enumerate(numbers) if index % 2 == 0]
# 3
# [print(qiy) for index, qiy in enumerate(numbers) if index % 3 == 0]










# numbers = [2, 5, 1, 9, 0, -3, -2, -6, 4]

# 1
# numbers = [son+2 for son in numbers]
#
# print(numbers)

# 2
# [print(son) for son in numbers if son % 2]

# 3
# numbers = [son**2 if son % 2 == 0 else son - 5 for son in numbers]
#
# print(numbers)









# a = input()
# b = a.isdigit()
# print(a.count()


# a = list(input("Str: "))
# a.remove(a[int(input("Son: "))])
# print("".join(a))






# num = int(input())
#
# for a in range(1, num+1):
#     for i in range(1, num+1):
#         if a == num or a == 1 or i == 1 or i == num:
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print()






# num = int(input())
#
# for i in reversed(range(num+1)):
#     print("*"*i)






# arr = [2, 4, 6, -5, 1]
#
# if arr.count(5):
#     print("Bor")
# else:
#     arr.append(5)
# print(arr)










# numbers = [5, 1, 2, 4, 3, 5, 8, 5, 9, 1, 5]
#
# if numbers.count(5):
#     while numbers.count(5):
#         numbers.remove(5)
# else:
#     print("5 yo'q")
#
# print(numbers)




# n = 1000
# a = 1
#
# for son in range(1, n+1):
#     a *= son
#
# print(sum(list(map(int, str(a)))))


# car = {
#     "brand": "AUDI",
#     "cost": 50000,
#     "color": "black",
#     "year": 2020,
#     "speed": 200
# }
#
# for key in car:
#     if isinstance(car[key], str):
#         print(f"{key}: {car[key]}")


# d1 = {
#     'a': 100,
#     'b': 200,
#     'c': 300
# }
# d2 = {
#     'a': 300,
#     'b': 200,
#     'd': 400
# }
# d3 = d2.update(d1)
# print(d3)



# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dic4 = {}


# a = 2 ** 1000
# b = 0
#
# for i in str(a):
#     b += int(i)
#
# print(b)



# a = input()
#
# a = a[-1] + a[1:-1] + a[0]
#
# print(a)



#
# a, b = '1234', 'python'
#
# print(a[:len(a)//2] + b + a[len(a)//2:])





# a = input()
#
# print(a[:len(a) // 2] + a[:len(a) // 2 - 1:-1]) if len(a) % 4 == 0 else print(a)

#
# a = input()
#
# print(a[0].title() + a[1:-1] + a[-1].upper())




# a = "Welcome to najot talim. najot talim awesome, isn't it?"
#
# b = input()
#
# print(a.count(b))



# boy = float(input("Boy - sm: "))
# boy = boy / 100
# kilo = float(input("Kilo - kg: "))
# a = kilo/boy**2
#
# if a < 18.5:
#     print("Zaif")
# elif a >= 18 and a <= 25:
#     print("Normal")
# elif a > 25 and a <= 30:
#     print("Ortiqcha")
# else:
#     print("Semiz")




# kilometr = int(input("Kilometr: "))
# pul = int(input("1km pul: "))
#
# print(kilometr * pul)

# import math
#
# a = int(input("A: "))
# b = int(input("B: "))
#
# print(math.sqrt(a**2+b**2))


# a = int(input("Son: "))
# b = int(input("Son: "))
# c = int(input("Son: "))
#
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# elif c > b and c > a:
#     print(c)
# else:
#     print("Teng")



# a = int(input())
# a = abs(a)
#
# print("100 hamda 1000 oraliqida") if a >= 100 and a <= 1000 else print("Afsuski yo'q")

# x = int(input())
# y = int(input())
#
# print((x+y)**2)

 ###################################################################################################
# N1
# soz = input()
#
# print('Palindrome') if soz == soz[::-1] else print("Not palindrome")


# N3
# a = input()
# print(a[::-1])


# N5
# a = list(input())
# b = int(input())
# a.pop(b)
# print(''.join(a))

# N6
# a = input()
# a = a.split()
# print(''.join(a))

# N7
# a = input()
# a = a.split()
# a = ''.join(a)
# print(len(a))

# N8
# a = input()
# a = a[:len(a)//2] + a[len(a)//2:].upper()
# print(a)

# N9
# a = input()
# a = a.split()
# b = []
# for row in a:
#     b.append(row[0].upper() + row[1:-1] + row[-1].upper())
#
# print(' '.join(b))

# N10
# str1 = input()
# str2 = input()
# a = []
#
# [a.append(i) for i in str1 if i in str2]
# print(a)

# N11
# a = input()
# print(a.count("a"))

# N12
# a = input()
# a = a.lower()
# b = 0
#
# for value in "euioa":
#     b += a.count(value)
# print(b)


# N13
# a = set(input())
#
# print("".join(list(a)))


# N14
# a = input()
# [print(xar, end='') for i, xar in enumerate(a) if i % 2]


# N15
# a = list(input())
# b = input()
#
# while b in a:
#     a.remove(b)
#
# print("".join(a))

# N16
# a = input()
# a = a.split()
# for value in a:
#     if len(value) < len(a[0]):
#         a[0] = value
# print(a[0])

# N17
# a = input()
# a = a.split()
# print('.'.join(a))


# N18
# a = "112324545"
#
# print("Son") if a.isalnum() else print("Son emas")

    ##########################################################################################

# O1
# [print(row[:2]) for row in numbers]

# O2
# numbers = [value for row in numbers for value in row if not 1 in row]
# print(numbers)

# O3
# [print(int(row[0]), int(row[2])) for row in numbers]

# O4
# arr1 = [11, 22, 33, 44, 55, 66, 77]
# arr2 = [21, 18, 43, 40, 59, 31, 80]

# [print(arr1[i]) if arr1[i] > arr2[i] else print(arr2[i]) for i in range(len(arr1))]

# O5
# fruits = ["APPLE", "ORANGE", "BANANA"]

# fruits = [row.lower() for row in fruits]
# print(fruits)


# O6
# str1 = "PyNaTive"
# copy1 = [i for i in str1 if i.islower()]
# [copy1.append(i) for i in str1 if i.isupper()]
# print(''.join(copy1))

# O7
# num = [i for ind, val in enumerate(numbers) for i in val if not ind % 2]
# print(num)

# O8
# list1 = ['M', 'na', 'i', 'Ke']
# list2 = ['y', 'me', 's', 'lly']
# gap = [''.join(list1[i] + list2[i]) for i in range(len(list1))]
# print(gap)

# O9
# list1 = ["Hello", "take"]
# list2 = ["Dear", "Sir"]
#
# gap = [row + ' ' + row1 for row in list1 for row1 in list2]
# print(gap)

# O10
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
#
# [print(list1[son], list2[-1-son]) for son in range(len(list1))]

     ##############################################################################################
# P1
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

# P2
# list2 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# arr = ["h", "i", "j"]
# list2 = list2[2][1][2] + arr
# print(list2)

# P3
# arr = [2, 1, -4, -9, 0, -5, 8, 3]
#
# max_val = max(arr)
#
# while max_val in arr:
#     arr.remove(max_val)
#
# print(max(arr)) if arr else print("Hammasi teng")



# P4
# arr = [2, 5, 1, 4, 3, 2, 1, 6, 8, 5, 7, 9]
#
# result = list(set(arr))
#
# print(result)


# P5
# arr = [11, 40, 50, 5252334, 33, 50]
# result = ""
#
# for value in arr:
#     result += str(value)
#
# print(result)

  #################################################################################################
# R1
# arr = [1, 1, 3, 4, 4, 5, 6, 7]
# arr1 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
#
# arr.extend(arr1)
# print(sum(arr)/len(arr))



# R2
# arr = [1, 3, 5, 7, 9, 10]
# arr1 = [2, 4, 6, 8]
# arr.pop(-1)
#
# arr.extend(arr1)
# print(arr)



# R3
# list1 = [1, 4, 3, 9]
# a = input()
# new_arr = []
#
# for i in list1:
#     new_arr.append(a + str(i))
#
# print(new_arr)



# R4
# arr = [[1,2,3],[4,5,60],[7,8,9],[10,11,12]]
#
# for row in arr:
#     if sum(arr[0]) < sum(row):
#         arr[0] = row
#
# print(arr[0])



# R5
# arr = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# a = 0
#
# for son in arr:
#     if isinstance(son, int):
#         a += 1
# print(a)



# R6
# tup = (4, 3, 2, 2, -1, 18)
# a = 1
#
# for s in tup:
#     a *= s
#
# print(a)



# R7
# list1 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# a = ()
#
# while a in list1:
#     list1.remove(a)
#
# print(list1)


# R8
# arr = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# arr1 = {son: arr.count(son) for son in arr}
# print(arr1)



# # R8 2
# arr = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# a = []
#
# for son in arr:
#     print(arr.count(son), end="")
#     print()



# R9
# arr = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#
# arr[][1].sort()



# R10
# arr = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# arr1 = []
#
# [arr1.append(son) for son in arr if isinstance(son, int) or isinstance(son, float)]
# print(max(arr1))



# T1
# def kvadrat(num):
#     return num*num
#
# print(kvadrat(5))

# T2
# def abc(num):
#     return num*-1 if num < 0 else num
#
# print(abc(5))

# T3
# def kattasi(num1, num2):
#     return num1 if num1 > num2 else num2
#
# print(kattasi(3, 5))

# T4
# def lis_kattasi(num):
#     for value in num:
#         if num[0] < value:
#             num[0] = value
#     return num[0]
#
# list1 = [3, 6, 8, 1, 0]
# print(lis_kattasi(list1))

# T5
# def daraja(a, b):
#     return a**b
#
# print(daraja(2, 5))

# T10
# txt = "Hello, welcome to my world."
# belgi = '0'
# for row in txt:
#     print(row.index(belgi))












