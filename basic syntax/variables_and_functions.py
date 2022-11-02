# 1. Variables
my_age = 88  # snake case
myAge = 88  # camel case
# 88my_age = 88 <- 불가능
# 변수의 형태 - 시작은 항상 문자
a = 1
b = 5
c = a+b  # = 5
c = 1  # = 1
# print(c)  # = 1 <= 파이썬은 위에서 아래로 읽기 때문

# 2. Booleans and Strings - data types
my_name = False  # bool -> True or False
# my_age = "12" # str(문자열) -> 텍스트를 인식시켜주기 위해서 "" 사용
# my_age =12 # int
# print(my_name)

# 3. Function
def say_hello():  # declare function
    print("hello how r u?")
# say_hello() # call function

# 4. Indentation
def say_bye():  # : 아랫줄은 반드시 들여쓰기 해야 함
    print("bye bye")  # 들여쓰기로 영역(scope) 지정
# say_bye()

# 5. Parameters
# parameter(매개변수) : 함수에 입력되어 전달된 값을 받는 변수
# argument(인수) : 함수를 호출할 때 전달하는 입력값

def say_hello(user_name):  # user_name = parameter(매개변수)
    print("Hello ", user_name, ", how r u?")
# say_hello("gy")  # gy(실제로 전달한 데이터) = argument(인수)

# Multiple Parameters
def say_hi(user_name, user_age, country):  
    print("hello", user_name)
    print("you are", user_age)
    print("you are from", country)
# say_hi("gy", 12, "korea")

# Default Parameters
def say_hello1(user_name="anonymous"):  
    # 인수를 빈 값으로 보냈을 경우를 대비해 default parameter 값을 정해줌
    print("hello", user_name)
# say_hello1("gy")
# say_hello1()

def plus(a=0, b=0):
    print(a+b)
def minus(a=0, b=0):
    print(a-b)
def multiplication(a=0, b=0):
    print(a*b)
def division(a=0, b=0):
    print(a/b)
def power_of(a=0):
    print(a*a)

# 6. return values
def tax_calc(money):
    return money * 0.35 # to exit a function and send out a value
def pay_tax(tax):
    print("thanks for paying", tax)

# pay_tax(tax_calc(150000000))

# return recap
my_name = "gy"
my_age = 12
my_color_eyes = "black"
# print(f"Hello I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color.") # Hello I'm gy, I have 12 years in the earth, black is my eye color.

def make_juice(fruit):
    return f"{fruit}+🥤"

def add_ice(juice):
    return f"{juice}+🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🍬"

juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

# print(perfect_juice)  # 🍎+🥤+🧊+🍬



