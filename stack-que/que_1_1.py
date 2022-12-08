# 함수 원형 큐임
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear +1) % SIZE == front: #원형 큐 4번째 다음이 0 이어야 함
        return True
    else:
        return False


def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('큐 공간 없음')
        return
    else:
        rear = (rear + 1) % SIZE
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
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('공간 비어있음')
        return None
    return queue[(front + 1) % SIZE]



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

retData = deQueue()
print('식사 손님:', retData)
print('@@@ 다음 준비하세오###', peek())
retData = deQueue()
print('식사 손님:', retData)
print('@@@ 다음 준비하세오###', peek())
retData = deQueue()
print('식사 손님:', retData)
print('@@@ 다음 준비하세오###', peek())

enQueue('유진')
print('출구<--', queue, '<--입구')

enQueue('정민')
print('출구<--', queue, '<--입구')

enQueue('유유') #rear+1과 front가 같으면 꽉차거나 비어있는거로 동시에 해석 가능해서
                # 유유 는 삽입이 불가함. 중간에 하나는 비워줘야 함(그래야 오버헤드 발생x)
print('출구<--', queue, '<--입구')
