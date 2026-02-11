name=input("Enter the name of the student: ")
roll=int(input("Enter the Reg number of the student: "))
n=int(input("Enter the no of the student: "))

print("SCMS School Of Engineering And Technology")
print("=============================================")
print("\t\tMark Sheet")
print("=============================================")
print("\nName: ",name)
print("Roll: ",roll)
print("No of Subjects:",n)
print("=============================================")
for i in range(n):
    sub=input("enter subject")
    mark=int(input("Enter the mark of the subject: "))
    if mark>=90 and mark<=100:
        print("Grade: A")
    elif mark>=80 and mark<90:
        print("Grade: B")
    elif mark>=70 and mark<80:
        print("Grade: C")
    elif mark>=60 and mark<70:
        print("Grade: D")
    elif mark>=50 and mark<60:
        print("Grade: E")
    else:
        print("Grade: F")

print("sub name: ",sub)
print("mark: ",mark)
print("=============================================")