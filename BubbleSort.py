
#In place

#Idea: Bubble up the largest item: swapping two values in a 
#list if the preceding value is greater than the next one. 

def bubble_sort(myList) :
    for i in range(len(myList) - 1, 0, -1):
        for j in range(i):
            if myList[j] > myList[j + 1]:
                temp = myList[j]
                myList[j] = myList[j + 1]
                myList[j + 1] = temp
    return myList


lst = [4,2,6,5,1,3]

print(bubble_sort(lst))