def isQueueFull():
    global SIZE, queue, front, rear
    if rear != SIZE- 1:
        return False
    if rear == SIZE -1 and front == -1:
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1        
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('큐가 꽉 찼습니다.')
        return None
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐가 비었습니다.')
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('큐가 비었습니다.')
        return None
    return queue[front +1]

SIZE = 5
front = rear = -1
queue = [None for _ in range(SIZE)]

if __name__ == '__main__':
    select = input('삽입(I)/추출(E)/확인(V)/삭제(X) 중 하나를 선택 ==> ')

    while select != 'X' and select != 'x':
        if select == 'I' or select == 'i':
            data = input('입력할 데이터==> ')
            enQueue(data)
            print('큐 상태: ', queue)

        if select == 'E' or select == 'e':
            data = deQueue()
            print('추출된 데이터===>', data)
            print('큐 상태: ', queue)

        if select == 'V' or select == 'v':
            data = peek()
            print('확인된 데이터: ', data)
            print('큐 상태 : ', queue)
        else:
            print('다시 입력해주세요.')

        select = input('삽입(I)/추출(E)/확인(V)/삭제(X) 중 하나를 선택 ==> ')
    
    print('프로그램 종료')

        

        


