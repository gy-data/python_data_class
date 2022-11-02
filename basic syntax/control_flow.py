from random import randint   # random module에서 randint function을 가져오기

# 1. If

pw_correct = True
# if pw_correct:
#     print("here is your money")
# else: # optional
#     print("wrong password")

winner = 50
# if winner != 10:
#     print("if")
# elif winner < 10: # 또 다른 조건 추가할 때 elif 사용 | optional
#     print("elif")
# elif winner == 50:
#     print("elif2")
# else:
#     print("else")

# 2. And & Or

# age = int(input("How old are you?"))
# if age < 18:
#     print("You can't drink.")
# elif age >= 18 and age <= 35:
#     print("You drink beer!")
# elif age == 60 or age == 70:
#     print("Birthday party")
# else:
#     print("Go ahead!")

# True and True == True
# False and True == False
# True and False == False
# False and False == False

# True or True == True
# True or False == True
# False or True == True
# False or False == False

# 3. Python Standard Library(https://docs.python.org/3/library/)

# user_choice = int(input("Choose number between 1 and 50."))
# pc_choice = randint(1, 50)

# if user_choice == pc_choice:
#     print("You won!")
# elif user_choice > pc_choice:
#     print("Lower!")
# elif user_choice < pc_choice:
#     print("Higher!")

# 4. While

distance = 1
# while distance < 20:   # 값이 false가 될 때까지 무한 반복
#     print("I'm running:", distance, "km")
#     distance += 1

# e.g. Python Casino
print("Welcome to Python Casino")
pc_choice = randint(1, 100)
while True:
    user_choice = int(input("Choose number (1-100):"))
    if pc_choice > user_choice:
        print("Higher!")
    elif pc_choice < user_choice:
        print("Lower!")
    else:
        print("You Won!")
        break
