unit=int(input("Enter the number of units consumed: "))
bill=0
if unit<=100:
    bill=unit*1.5
elif unit>100 and unit<=200:
    bill=(100*1.5)+((unit-100)*2.5)
elif unit>200:
    bill=(100*1.5)+(100*2.5)+((unit-200)*3)
print("Total bill is: ",bill)