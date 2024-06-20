import createList
import sortAlgorithms
import time

print('''seperated by a space input 
      the Length of List, 
      magnitude of list, 
      0 for sorted 1 for random or 2 for reverse sorted list, 
      sorting type number of runs''')
string_List = input().split()
print("""Now input the type of sort: 
      selection,
      insertion,
      bubble,
      merge,
      quick""")
sort_type = input()

len_list = int(string_List[0])
mag_list = int(string_List[1])
list_type = int(string_List[2])
num_runs = int(string_List[3])

if list_type == 0:
    list_of_lists = []
    for i in range(num_runs):
        A = createList.sortedList(len_list, mag_list)
        list_of_lists.append(A)

elif list_type == 1:
    list_of_lists = []
    for i in range(num_runs):
        A = createList.randomList(len_list, mag_list)
        list_of_lists.append(A)

elif list_type == 2:
    list_of_lists = []
    for i in range(num_runs):
        A = createList.reverseList(len_list, mag_list)
        list_of_lists.append(A)

else:
    print('please enter valid choice for list type')

if sort_type == "selection":
    for key in list_of_lists:
        start_time = time.time()
        sortAlgorithms.selectionSort(key)
        print("--- %s seconds ---" % (time.time() - start_time))

elif sort_type == "insertion":
    for key in list_of_lists:
        start_time = time.time()
        sortAlgorithms.insertionSort(key)
        print("--- %s seconds ---" % (time.time() - start_time))

elif sort_type == "bubble":
    for key in list_of_lists:
        start_time = time.time()
        sortAlgorithms.bubbleSort(key)
        print("--- %s seconds ---" % (time.time() - start_time))

elif sort_type == "merge":
    for key in list_of_lists:
        start_time = time.time()
        sortAlgorithms.mergeSort(key)
        print("--- %s seconds ---" % (time.time() - start_time))

elif sort_type == "quick":
    for key in list_of_lists:
        start_time = time.time()
        sortAlgorithms.quickSort(key, 0, len_list - 1)
        print("--- %s seconds ---" % (time.time() - start_time))

else:
    print("Please make sure your spelling is correct")