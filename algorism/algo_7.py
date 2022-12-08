## 순차 검색 중요!! 구현 중요
#함수
import random
def seqSearch(ary, fData):
    pos = -1
    size = len(ary)

    for i in range(size) :
        if ary[i] == fData :
            pos = i
            break
    return pos

#변수
dataAry = [random.randint(40,200) for _ in range(8)]
findData = random.choice(dataAry)

#메인
print('배열', dataAry)
position = seqSearch(dataAry, findData)
if position != -1:
    print(findData,'가', position, '위치에 있어요~')
else:
    print(findData,'가', position, '없습니다.')


