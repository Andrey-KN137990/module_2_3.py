my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
A = 0
while A < len(my_list):
    if my_list[A] < 0:
        break
    if my_list[A] > 0:
        print(my_list[A])
    A += 1