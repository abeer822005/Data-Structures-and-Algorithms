list1=[2,3,5,2,33,21]
i=0
while i <  len(list1):
    print (list1[i])
    i+= 1

list2=[x for x in range (0,5)]
print (list2)
list3=[0.5 * x for x in list2]
print (list3)
list4 = [x for x in list3 if x< 1.5]
print(list4)
list5=["green","red","blue"]
list6=["red","blue","green"]
print (list6==list5)
print (list6!=list5)
print (list6>=list5)
print (list6>list5)
print (list6<list5)
print (list6<=list5)
items1="Welcome to the SCME".split()
print (items1)
items2="34#13#78#45".split ("#")
print(items2)
print (items1==items2)
print (items1>=items2)
print (items1!=items2)
print (items1<=items2)
print (items1>items2)
print (items1<items2)