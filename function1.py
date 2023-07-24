# function1.py

# Function Define
def setValue(newValue):
    x = newValue
    print("local:", x)

# Function Call
result = setValue(5)
print(result)

# Function Define
def swap(x,y):
    return y,x

# Function Call
print(swap(3,4))


# 교집합 문자를 return
def intersect(prelist,postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

# Call
print(intersect("HAN","SPAM"))