

# Divide and conquer algorithm: divided the list into
# two sub lists that are smaller 


""" 

Helpter function: combines two sorted lists into 
one sorted list

"""

def merge(list1, list2):

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


lst1 = [1,2,3]
lst2 = [4,5,6]

print(merge(lst1, lst2))