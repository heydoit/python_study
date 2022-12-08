# #재귀 호출

# def openBox():
#     global count
#     print('상자를 열어요')
#     count -= 1
#     if count == 0:
#         print('*** 선물 넣기***')
#         return
#     openBox()
#     print('상자를 닫아요')
#     return

# count = 10
# openBox()


# #숫자 합계

# def addNumber(num):
#     if num == 1:
#         return 1
#     return num + addNumber(num - 1)

# print(addNumber(100))

# ##팩토리얼

# def factValue(num):
#     if num == 1:
#         return 1
#     return num * factValue(num - 1)
# print(factValue(10))

# #팩토리얼 해답
# factValue = 1
# for n in range(10,0,-1):
#     factValue *= n
# print(factValue)



# #우주발사
# import time
# def space(num):
#     if num == 0:
#         time.sleep(1)
#         print('발사')
#     else:
#         print(num)
#         time.sleep(1)
#         return space(num -1)
# space(5)


#별모양 출력하기

def star(num):
    if num > 0 :
        star(num-1)
        print('★'*num)

star(5)