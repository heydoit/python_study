# def findMinIndex(ary):
#     minIdx = 0
#     for i in range(1, len(ary)):
#         if (ary[minIdx] > ary[i]):
#             minIdx = i

#     testAry = [55, 88, 33, 77]

#     minPos = findMinIndex(testAry)
#     print('최솟값-->', testAry[minPos])


    #######외우기#####
import random
def findMinIndex(ary):
    minIdx = 0

    for i in range(1, len(ary)):
        if (ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx

before = [random.randint(40,200) for _ in range(8)]
after = []

print('정렬 전-->', before)
for _ in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])
print('정렬 후-->', after)

######

import random
def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = 0

        for k in range(1, n):
            if ary[minIdx] > ary[k]:
                minIdx = k

        ary[0], ary[minIdx] = ary[minIdx], ary[0]

dataAry = [random.randint(40,200) for _ in range(8)]

print('정렬 전-->', dataAry)
dataAry = sorted(dataAry)
print('정렬 후-->', dataAry)