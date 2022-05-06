# print("hello world")

# for i in range(1, 21):
#     if i % 15 == 0:
#         print("yeardream")
#     elif i % 3 == 0:
#         print("year")
#     elif i % 5 == 0:
#         print("dream")
#     else:
#         print(i)


def fibo(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    return fibo(x - 1) + fibo(x - 2)


print(fibo(3))
