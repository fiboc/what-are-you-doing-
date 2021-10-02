a = [99, 1, 10, 17, 67, 50, 42]

for i in a:
    if a[0] > i:
        a[0] = i

print(a[0])








  #M2
# son = float(input("1 dan 100gacha baho: "))
#
# if son >= 80 and son <= 100:
#     print("Bahoyingiz a'lo")
# elif son >= 60 and son < 80:
#     print("Bahoyingiz yaxshi")
# elif son >= 40 and son < 60:
#     print("Bahoyingiz qoniqarli")
# elif son >= 0 and son < 40:
#     print("Bahoyingiz qoniqarsiz")
# else:
#     print("Bunday baho yo'q")

  #M3
# is_raqam = int(input("Input: "))
#
# while is_raqam > 10:
#     is_raqam //= 10
# print(is_raqam)
# is_raqam = ord(str(is_raqam))
# if (is_raqam >= 48) and (is_raqam <= 57):
#     print("Raqam")
# else:
#     print("Raqam emas")
#   #M4
# harf = ord(input("Input: "))
#
# if (harf > 64) and (harf < 91) or (harf > 96) and (harf < 123):
#     print("Harf")
# else:
#     print("Harf emas")
# M5
# son = int(input("Son: "))
# print(f"{son // 10000 + son // 1000 % 10 + son // 100 % 10 + son % 100 // 10 + son % 10}")
# M6
# son = int(input("Son: "))
# son = son % 10 * 10 + son // 10
# print(son)
  #M7
# son = int(input("Son: "))
# son = son % 10 * 1000000 + son % 100 // 10 * 100000 + son % 1000 // 100 * 10000 + son // 1000 % 10 * 1000 + son // 10000 % 10 * 100 + son // 100000 % 10 * 10 + son // 1000000
# print(son)
# chota s chemto
# son = input("Son: ")
# print(son[::-1])





list1 = [2, 1, -4, -9, 0, -5, 8, 3]
list2 = [-4, 0, 2, 9, 6, 1]

list1.extend(list2)

list1.sort()







# for a in list1:
#     if a not in list2:
#         print(a)
# for b in list2:
#     if b not in list1:
#         print(b)

# list1.extend(list2)
# [print(son) for son in list1 if son.count() == 1]









# [print(value) for value in list1 if not value in list2]

























































































































