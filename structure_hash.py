# 해시 값 얻기
print(hash("hello"))  # 예: 4887855672870042632 (결과는 실행마다 다를 수 있음)
print(hash(42))       # 출력: 42 (숫자는 자기 자신이 해시 값)

# 빈 딕셔너리 생성
empty_dict = {}

# 초기 값을 가진 딕셔너리 생성
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 값 접근
print(person["name"])  # 출력: John

# 값 수정
person["age"] = 31
print(person)  # 출력: {'name': 'John', 'age': 31, 'city': 'New York'}

# 요소 추가
person["job"] = "Developer"

# 요소 삭제
del person["city"]
print(person)  # 출력: {'name': 'John', 'age': 31, 'job': 'Developer'}

print(person.keys())    # 출력: dict_keys(['name', 'age', 'job'])
print(person.values())  # 출력: dict_valeues(['John', 31, 'Developer'])
print(person.items())   # 출력: dict_items([('name', 'John'), ('age', 31), ('job', 'Developer')])

# 값 가져오기
print(person.get("name"))  # 출력: John
print(person.get("city", "Not Found"))  # 출력: Not Found