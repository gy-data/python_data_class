# 1. Methods
# Method : 데이터 뒤에 결합/연결된 function(내부에 있는 function)
name = "gy"
print(name.endswith("y"))  # = True


# 2. Data Structures

# 2-1. List
days_of_weekday = ["Mon", "Tue", "Wed", "Thu", "Fri"]  # <= list : 0부터 시작
# 마음대로 변경 가능(생성, 수정, 삭제, ...)
# 사용할 수 있는 method의 수가 많음
print(days_of_weekday[:3])
even = [2, 4, 6, 8]
print(even[2:])

# 2-2. Tuple
days = ("Mon", "Tue", "Wed")  # <= tuple : 0부터 시작
# 불변성을 가짐(튜플 안의 값을 변경할 수 없음)
# 사용할 수 있는 method의 수가 적음
print(days[-1])  # 맨 뒤는 -1 (list도 가능)

# 2-3. Dictionary
# key - value (키 - 값)
player = {
    'name': 'gy',
    'age': 15,
    'alive': True,
    'fav_food': ["🍲", "🌮"]
}  # <= dict
print(player['fav_food'])  # = player.get("fav_food")
player.pop('age')  # 키 삭제
player['xp'] = 1500  # 추가
player['fav_food'].append("🍕")  # Dict 안의 list에 값 추가
