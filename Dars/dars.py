# numbers = [1, 2, 3, 4, 5]
# number_ = [5, 4, 3, 2, 1]
#
# result = map(lambda a, b: a + b, numbers, number_)
#
# print(list(result))

def tub_son(num):
    sanoq = 0
    if num >= 2:
        for i in range(2, num // 2):
            if num % i == 0:
                sanoq += 1
    else:
        return False
    return True if sanoq == 0 else False


ages = [5, 12, 17, 18, 24, 32, 19, 0, 21, 1, -1, 2, 3]

result = filter(tub_son, ages)

print(list(result))

