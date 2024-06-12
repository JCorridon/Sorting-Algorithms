import random

def sortedList(len_list, mag_list):

    main_list = []
    number_items = len_list / mag_list
    number_items = int(round(number_items))
    for i in range(mag_list):
        for j in range(number_items):
            if len(main_list) < len_list:
                main_list.append(i)

            else:
                return main_list
            
    return main_list

def reverseList(len_list, mag_list):

    main_list = []
    number_items = len_list / mag_list
    number_items = int(round(number_items))
    for i in range(mag_list):
        for j in range(number_items):
            if len(main_list) < len_list:
                main_list.append(i)

            else:
                main_list.reverse()
                return main_list
            
    main_list.reverse()
    return main_list

def randomList(len_list, mag_list):

    main_list = []
    for i in range(len_list):
        main_list.append(random.randrange(0, mag_list))

    return main_list