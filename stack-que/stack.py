## 함수부

## 변수부
stack = [None,None,None,None,None]
top = -1

## 메인부

# 삽입(push)
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'

print('바닥:', stack)

#추출(pop)
data = stack[top]
stack[top] = None
top -=1
print('추출:', data)

data = stack[top]
stack[top] = None
top -=1
print('추출:', data)

data = stack[top]
stack[top] = None
top -=1
print('추출:', data)
