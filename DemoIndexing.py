# DemoIndexing.py

strA = "Python is very powerful"
print(strA[0])
print(strA[1])
print(strA[0:3])
print(strA[:3])    #  약식표현

print(strA[-3:])
print(strA[-8:])

strB = "0123456789"
print(strB[0:10])

# list 연습

color = ["red", "blue", "green"]
print(color)
print(len(color))
print(color[0])

#  디버깅 중단점(break point)
for item in color:
    print(item)

color.append("white")
print(color)
color.insert(1,"pink")
print(color)
print(color.index("red"))
color += "red"
print(color.pop())
print(color.pop())
print(color.pop(1))
print(color)
color.extend(["black", "red", "white", "pink"])
print(color)
color.remove("black")
print(color)
color.sort()
print(color)
color.reverse()
print(color)
             
