# class1.py
# 1) 클래스 형식 정의
class Person:
    #초기화 ㅁ서드
    def __init__(self):
        # 인스턴스 멤버변수
        self.name = "default name"
    
    def print(self):
        print("My name is {0}".format(self.name))

p1 = Person()
p2 = Person()

p1.name = "전우치"
p1.print()
p2.print()

Person.title = "new title"
p1 = (p1.title)
p2 = (p2.title)
p2 = (Person.title)
