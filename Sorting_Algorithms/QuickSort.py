
#Helper function
def swap(my_List, index1, index2):
    temp = my_List[index1]
    my_List[index1] = my_List[index2]
    my_List[index2] = temp

#Helper function
def pivot(my_List, pivot_index, end_index):
    swap_index = pivot_index #Pointers start at same position 

    for i in range(pivot_index + 1, end_index + 1):
        if my_List[i] < my_List[pivot_index]:
            swap_index += 1
            swap(my_List, swap_index, i)
    swap(my_List, pivot_index, swap_index) #Move the swap pointer to its correct position
    return swap_index

#Test
my_List = [4,6,1,7,3,2,5]
print(my_List)
print("Should print sorted pivot list followed my pivot index:", my_List, pivot(my_List, 0, len(my_List) - 1), "\n")

def quickSort(my_List, left = 0, right = len(my_List) - 1):
    #Base case: when there is only one item in the list, left and right will be the same
    if left < right: 
        pivot_index = pivot(my_List, left, right)
        quickSort(my_List, left, pivot_index - 1)
        quickSort(my_List, pivot_index + 1, right)
    return my_List

#Test
print(quickSort(my_List))
