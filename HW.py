my_list = [42, 69, 332, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while a < len(my_list):

    if my_list[a] > -1:
        if my_list[a] != 0:
            print(my_list[a])
        a = a + 1
        continue
    else:
        break
print('---------')
