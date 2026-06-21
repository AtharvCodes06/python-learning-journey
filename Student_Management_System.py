# !!!!! STUDENT MANAGEMENT PROGRAM !!!!!

students = []

total = int(input("ENTER TOTAL NUMBERS OF STUDENT ? : "))
for i in range(total):
    student= input("ENTER STUDENT NAME : ")
    students.append(student)

for student in students:
    print(student)

# FOUND A STUDENT NAME IS IN LIST OR NOT.

search_name = input("ENTER THE NAME OF STUDENT THAT YOU WANT TO SEARCH : ")

if search_name in students :
    print("FOUND")
else:
    print("NOT FOUND")

print("THANK YOU!!!")
