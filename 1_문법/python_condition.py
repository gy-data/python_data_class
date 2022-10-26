# if 조건문
# number = int(input())
# if number < 5:
#     print("숫자가 5보다 작습니다.")
# elif 5<number<10:
#     print("5보다 크고 10보다 작습니다.")
# else:
#     print("10보다 큽니다.")

# money = int(input())
# if money>=70000:
#     print("비행기 타기")
# elif 50000<=money<70000:
#     print("기차 타기")
# elif 30000<=money<50000:
#     print("버스 타기")
# else:                    # else는 필수가 아님. 없으면 그냥 넘어감.
#     print("걸어가기")


# for 반복문
# for i in range(10):     # i=변수. range(10)='0 <= x < 10'
#     print("Hello world")

# for list in [1,2,3,4,5]:
#     print(list)

# countries = ["kor", "usa", "china"]
# for country in countries:
#     if country == "kor":
#         print("한글로 분석해주세요.")
#     elif country == "usa":
#         print("영어로 분석해주세요.")
#     else:
#         print("중국어로 분석해주세요.")


# while 반복문
# a = 0
# while a < 5:
#     a += 1
#     print(a)
# # 잘 사용하지 않음. 무한반복이 필요할 때 사용하는 경우가 있음

# # Q. 1부터 5까지 더하는 프로그램을 만들어보시오.
# total = 0
# for i in range(1, 6):
#     total += i
#     print(total)


# 제어문 - continue
for i in range(10):
    if 3 <= i <= 5:
        continue  # 반복문의 코드 처음으로 돌아간다
    print(i)

# 제어문 - break
for i in range(10):
    if 3 <= i <= 5:
        break  # 반복문을 멈추세요.
    print(i)
