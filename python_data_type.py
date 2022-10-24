from pickletools import int4


x="123" # str
x=123 # int  
x=10.5 # float
x=[1,2,3,4] # list
x={"name":"gy", "age":"25"} # dict
x=True # bool (or False)

# print(type(x))

a=1+1
a=100-1
a=12*12
a=12/4
# print(a)

# 문자형 다루기
a="Act as thought \nit is impossible to fail" # 줄 바꾸기

a="""Act as thought 
it is impossible to fail""" # """문장""" or '''문장''' 하면 문자 그대로 나옴


a= '"Failure is simply the opportunity to begin again." he says."'
a= """ "FFailure is simply the opportunity to begin again." he says." """
a= "\"Failure is simply the opportunity to begin again.\" he says.\""
# print(a)

a= "A"
b= "B"
# print(a+b)
# print(a*10) # 곱 : 문자형끼니는 X. 문자*숫자는 가능

c = "100" # 문자열 길이 len()
# print(len(c))

# 원하는 문자열 가져오기
c= "hello python!"
# print(c[0]) #  indexing - 하나만 지정
# print(c[0:5]) # 0<= c < 5 # slicing - 범위 지정
# print(c[6:]) # 끝까지 구하고 싶을 떈 공백
# print(c[:]) # 처음부터 끝까지 가져올 때 

x = "TitanicJames"
title = x[:-5]
director  = x[-5:]
# print(title, director)

# List(리스트형)
# a=["a", "b", "c", "d", "e"]
a=["a", "b ", ["c", "d", "e"]]
# print(a[2][1]) # d

# Tuple(튜플형)
t=("a", "b", "c", "a")

# Dict(딕셔너리형)
x={"key1":"value1", "key2":"value2"} # JSON이라고도 함
# print(x["key2"]) # value2

# Set(집합형)
x=set([1,1,1,2]) # 중복 허용 X
# print(x) # [1, 2]

