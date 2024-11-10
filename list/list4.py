def reverse (list):
    result=[]
    for element in list:
        result.insert(0, element)
    return result 
list1 = [1,2,3,4,5,6]
list2 = reverse(list1)
print(list2)


list3=[1,2,3,4,5,6]
list3.reverse()
print ("revers list3 is" ,list3)
def linearsearch (lst, key):
    for i in range (0, len(lst)):
        if key == lst[i]:
            return i
        
    return -1
