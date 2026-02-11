age = int(input("Enter your age: "))

if age < 18:
    print("Not eligible for insurance")
elif age >= 18 and age <= 30:
    print("Insurance Premium: ₹2000")
elif age >= 31 and age <= 50:
    print("Insurance Premium: ₹3500")
else:
    print("Insurance Premium: ₹5000")
