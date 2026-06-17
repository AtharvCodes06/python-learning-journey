print("!!!!! WELCOME TO NUMBER GUESSING GAME !!!!!")
print("Guess a number between 1 and 10")

secret_no = 8
Attempt = 1
while Attempt <= 3:
   print(f"Attempt no: {Attempt}")
   Attempt += 1
   guess = int(input("ENTER YOUR GUESS NO : "))
   if guess == secret_no:
      print("YOU WON!!!")
      break
   else:
      print("FAIL!!!!")
