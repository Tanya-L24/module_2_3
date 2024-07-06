my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0

#Нужно выписывать из этого списка только положительные числа до тех пор,
#пока не встретите отрицательное или не закончится список (выход за границу)

while len(my_list) > index:
    if my_list[index] < 0:
        break
    elif my_list[index] > 0:
        print(my_list[index])
    index += 1




