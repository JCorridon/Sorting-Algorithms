import createList
import insertionSort

print('seperated by a space input the Length of List, magnitude of list, 0 for sorted 1 for random or 2 for reverse sorted list, number of runs')
string_List = input().split()
print(string_List)

len_list = int(string_List[0])
mag_list = int(string_List[1])
list_type = int(string_List[2])
num_runs = int(string_List[3])

if list_type == 0:
    for i in range(num_runs):
        A = createList.sortedList(len_list, mag_list)
        insertionSort.insertionSort(A)

elif list_type == 1:
    for i in range(num_runs):
        A = createList.randomList(len_list, mag_list)
        insertionSort.insertionSort(A)

elif list_type == 2:
    for i in range(num_runs):
        A = createList.reverseList(len_list, mag_list)
        insertionSort.insertionSort(A)

else:
    print('please enter valid choice for list type')

