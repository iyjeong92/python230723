# DemoDict.py

device = {"apple":5, "Samsung":10, "window":30}

# 검색
print(device["apple"])

# 입력
device["Mac"] = 15
print(device)

# 수정
device["iphone"] = 6
print(device)

# 삭제
del device["apple"]
print(device)

for item in device.items():
    print(item)

for key in device.keys():
    print(key)

# 이름 + 전화번호 맵핑(Dict)
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print(phone.values())
print("kim" in phone)
print("kang" not in phone)
# 파이썬은 항상 참조를 전달한다.
p = phone
print(p)
print(phone)
print(id(phone), id(p))

print("---논리식---")
isRight = True
print(type(isRight))
print("1은 2보다 작다", 1 < 2)
print("1은 2랑 다르다", 1 != 2)
print("1과 2는 같다", 1 == 2)
print(True and True and True)
print(True and True and False)
print(True or False or False)



3123 % 1600