# 1. If
# pw_correct = True
# if pw_correct:
#     print("here is your money")
# else: # optional
#     print("wrong password")

# winner = 50
# if winner != 10:
#     print("if")
# elif winner < 10: # 또 다른 조건 추가할 때 elif 사용 | optional
#     print("elif")
# elif winner == 50:
#     print("elif2")
# else:
#     print("else")

# 2. And & Or
age = int(input("How old are you?"))

if age < 18:
    print("You can't drink.")
elif age >= 18 and age <= 35:
    print("You drink beer!")
elif age == 60 or age == 70:
    print("Birthday party")
else:
    print("Go ahead!")

# True and True == True
# False and True == False
# True and False == False
# False and False == False

# True or True == True
# True or False == True
# False or True == True
# False or False == False
