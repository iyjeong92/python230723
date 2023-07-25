# fuction2.py
# 전역변수와 지역변수
x = 1

def fuct(a):
    return a+x

# 호출
print(fuct(1))

def fuct2(a):
    x = 5
    return a+x

# 호출
print(fuct2(1))

# 기본값지정(옵션)
def times(a=1, b=20):
    return a*b

# 호출
print(times())
print(times(5))
print(times(5,6))

# 키워드 인자
def connectURL(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

# 호출
print( connectURL("cerdu.com","80"))
print( connectURL(port="8080", server="cerdu.com"))
