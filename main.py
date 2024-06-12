import createList
import insertionSort

len_list = int(input("How long would you like for the list to be?: "))
mag_list = int(input("how large would you like the numbers to be?: "))
list_type = int(input("Enter 0 for sorted list, 1 for random list, or 2 for reverse sorted list: "))

if list_type == 0:
    print(createList.sortedList(len_list, mag_list))

elif list_type == 1:
    print(createList.randomList(len_list, mag_list))

elif list_type == 2:
    print(createList.reverseList(len_list, mag_list))

else:
    print('please enter valid choice for list type')

