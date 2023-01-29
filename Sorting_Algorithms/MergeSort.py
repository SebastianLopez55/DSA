
#Not inplace 


# Divide and conquer algorithm: divided the list into
# two sub lists that are smaller 

""" 
Helpter function: combines two sorted lists into 
one sorted list
"""
def merge(list1, list2):
    #Time complexity: N

    combined = []
    i = 0
    j = 0

    while (i < len(list1)) and (j < len(list2)):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    while (i < len(list1)):
        combined.append(list1[i])
        i += 1

    while (j < len(list2)):
        combined.append(list2[j])
        j += 1

    return combined

#Testing merge(lst1, lst2)
lst1 = [1,2,3]
lst2 = [4,5,6]
print("Merge: ", merge(lst1, lst2))


#Function that breaks lists in half

def mergeSort(myList):
    #Tiem Complexity: logN

    if len(myList) == 1:
        return myList
    
    mid_index = int(len(myList)/2)
    left = mergeSort(myList[:mid_index])
    right = mergeSort(myList[mid_index:])

    return merge(left, right)



#Test mergeSort
lst = [3,1,4,2]

print("Megesort: ", mergeSort(lst))

