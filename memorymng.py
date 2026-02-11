import copy
lst=[
    [10,20,30],
    [15,23,56]
]
#lst1=lst
#lst1[0][0]=100
#print(lst)
#print(lst1)

lst1=copy.deepcopy(lst)
lst1[0][0]=100
print(lst)
print(lst1)