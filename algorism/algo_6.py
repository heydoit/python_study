#기본 정렬 알고리즘

import random
def selectionSort(ary):
    n = len(ary)
    for i in range(0,n-1):
        minIdx = 0 # i

        for k in range(1,n): #i+1, n 
            if (ary[minIdx] > ary[k]):
                minIdx = k
        ary[0], ary[minIdx] = ary[minIdx], ary[0] #i

dataAry = [random.randint(40,200) for _ in range(8)]

print('정렬 전-->', dataAry)
dataAry = sorted(dataAry)
print('정렬 후-->', dataAry)


#복습
def findeindex(ary):
    mindix = 0

    for i in range(1, len(ary)):
        if ary[mindix] > ary[i]:
            mindix = i
    return mindix


import random
def binSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary) - 1
    while start <= end:
        mid = (start + end) // 2
        if ary[mid] == fData:
            pos = mid
            break
        elif ary[mid] < fData:
            start = mid + 1
        else:
            end = mid - 1
    return pos


dataAry = [random.randint(20,500) for _ in range(8)]
findData = random.choice(dataAry)
dataAry.sort()

print('배열-->', dataAry)
position = binSearch(dataAry, findData)
if position != -1:
    print(findData, '가',position,'번째 위치에 있어요')
else:
    print(findData, '가',position,'없음')
