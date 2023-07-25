# ifelse.py

# score = int(input("점수를 입력: "))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score <= 90:
#     grade = "B"
# elif 70 <= score <= 80:
#     grade = "C"
# elif score <= 70:
#     grade = "D"
# else:
#     grade = "Fail"

# print('등급은 ',grade)

# value = 5
# while value > 0:
#     print(value)
#     value -= 1

# lst = [100, "문자열", 3.14]
# for i in lst:
#     print(i)

# for i in range(10):
#     print(i)

# anal_yyyy = str(2023)
# anal_mm = str(01)
# anal_dd = range(0,31)
# anal_hh = str(00)
# print(list(range(0,31)))

print("---리스트 컴프---")
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])
tp = ("apple", "banana", "orange")
print([len(i) for i in tp])
d = {100:"apple", 200:"kiwi"}
print([v.upper() for v in d.values()])

for i in map(lambda x:x+10, lst):
    print(i)