stmarks=[90,'A',95,80,'A',84,'A',96]
#OUTPUT:[90,95,80,84,96,A,A,A]

marks=[]
marks1=[]
for i in stmarks:
    if i!='A':
        marks.append(i)
    else:
        marks1.append(i) 
print(marks)
print(marks1)
marks.extend(marks1)
print("OUTPUT:",marks)