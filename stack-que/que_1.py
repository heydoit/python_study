# 함수
def isQueueFull():
    global SIZE, queue, front, rear
    if rear == SIZE-1:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('큐 공간 없음')
        return
    else:
        rear += 1
        queue[rear] = data

def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('공간 비어있음')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('공간 비어있음')
        return None
    return queue[front + 1]



#변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1


# 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<--입구')

enQueue('유진')
print('출구<--', queue, '<--입구')

retData = deQueue()
print('식사 손님:', retData)
print('@@@ 다음 준비하세오###', peek())
retData = deQueue()
print('식사 손님:', retData)
print('@@@ 다음 준비하세오###', peek())
