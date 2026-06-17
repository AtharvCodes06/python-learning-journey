marks = int(input("ENTER THE STUDENT MARKS : "))

if marks < 0 or marks > 100:
    print("INVALID RESULT")
elif 90 <= marks <= 100:
    print("GRADE A")
elif 75 <= marks <= 89:
    print("GRADE B")
elif 50 <= marks <= 74:
    print("GRADE C")
else:
    print("FAIL!!!")
