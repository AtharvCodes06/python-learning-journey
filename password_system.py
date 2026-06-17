password = "atharv"
success = False
attempt = 1
while attempt <= 3:
    print(f"Attempt no : {attempt}")
    attempt += 1
    enter_password = input("ENTER YOUR PASSWORD : ")
    if enter_password == password:
        print("ACCESS GRANTED")
        success = True
        break
    else:
        print("WRONG PASSWORD")
if not success:
 print("access denied")
