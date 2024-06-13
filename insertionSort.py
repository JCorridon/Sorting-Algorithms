import time

def insertionSort(list):

    # Keep track of run time
    start_time = time.time()

    # Find the smallest number in the list
    for i in range(len(list) - 1):
        min_num = i

        for j in range(i+1, len(list)):
            if list[min_num] > list[j]:
                min_num = j
        
        list[i], list[min_num] = list[min_num], list[i]
    
    print("--- %s seconds ---" % (time.time() - start_time))
    return list
