
# Finding the minimum value of the items being sorted, 
# and then moving it to the start of the of the list.

def selection_sort(myList):
    for i in range(len(myList) - 1):
        min_index = i
        for j in range(i + 1, len(myList)):
            if myList[j] < myList[min_index]:
                min_index = j

        if i != min_index:
            temp = myList[i]
            myList[i] = myList[min_index]
            myList[min_index] = temp
        
        return myList

lst = [4,2,6,5,1,3]

print(lst)
print(selection_sort(lst))