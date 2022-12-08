# def add_data(friend):
#     a.append(None)
#     alen = len(a)
#     a[alen-1] = friend

# def insert_data(position, friend):
#     a.append(None)
#     alen = len(a)
#     for i in range(alen-1, position, -1):
#         a[i] = a[i-1]
#         a[i-1] = None

#     a[position] = friend

# def delete_data(position):
#     a[position] = None
#     alen = len(a)

#     for i in range(position+1, alen):
#         a[i-1] = a[i]
#         a[i] = None

#     del(a[alen-1])


# a = []

# add_data('다현')
# add_data('정연')
# add_data('쯔위')
# add_data('사나')
# add_data('지효')
# print(a)

# # insert_data(2, '솔라')
# # print(a)

# delete_data(1)
# print(a)


# 완전문
a = []

def add_data(friend):
    a.append(None)
    alen = len(a)
    a[alen-1] = friend

def insert_data(position, friend):
    a.append(None)
    alen = len(a)
    for i in range(alen-1, position, -1):
        a[i] = a[i-1]
        a[i-1] = None
        
    a[position] = friend

def delete_data(position):
    a[position] = None
    alen = len(a)
    for i in range(position+1, alen):
        a[i-1] = a[i]
        a[i] = None
    del(a[alen-1])


select = -1

if __name__ == '__main__':
    while (select != 4):
        select = int(input('선택하세요(1: 추가, 2: 삽입, 3: 삭제 4: 종료)-->'))

        if select == 1:
            data = input('추가할 데이터-->')
            add_data(data)
            print(a)
        elif select == 2:
            pos = int(input('삽입할 위치-->'))
            data = input('추가할 데이터-->')
            insert_data(pos, data)
            print(a)
        elif select == 3:
            pos = int(input('삭제할 위치-->'))
            delete_data(pos)
            print(a)
        elif select == 4:
            print(a)
            exit
        else:
            print('1~4 중 하나를 입력하세요.')
            continue


