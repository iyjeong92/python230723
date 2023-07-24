# DemoTupleSet.py

a = {1,2,3,3}
b = {3,4,4,5}

print(a)
print(type(a))
print(a.union(b))  #합집합
print(a.intersection(b))  #교집합
print(a.difference(b))  #차집합

print("---Tuple---")
tp = (10,20,30)
print(len(tp))
print(tp[0])
print("id:%s, code name:%s" % ("kimmm","김유신"))

# 함수정의
def cals(a,b):
    return a+b, a**b

# 함수호출
retValue = cals(3,4)
print(retValue)

print("---형식 변환---")
a = set((1,2,3))
print(a)

b = list(a)
b.append(4)

c = tuple(b)
print(c)

print("---Dict---")
color = {"apple":"red","banana":"yellow"}
print(len(color))
color["cherry"] = "red"
print(color)