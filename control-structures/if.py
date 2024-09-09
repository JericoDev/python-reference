# age = 18
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")

# score = 100
score = int(input("Enter score: "))
if score > 100:
    print("Invalid")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")