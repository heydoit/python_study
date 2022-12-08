a = []

def add_data(friend):
    a.append(None)
    alen = len(a)
    a[alen-1] = friend

add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(a)
add_data('모모')
print(a)

def insert_data(position, friend):
    a.append(None)
    alen = len(a) #배열의 크기
    
    for i in range(alen-1, position, -1):
        a[i] = a[i-1]
        a[i-1] = None
    
    a[position] = friend

insert_data(3, '미나')
print(a)

def delete_data(position):
    a[position] = None
    alen = len(a)

    for i in range(position+1, alen, 1):
        a[i-1] = a[i]
        a[i] = None

    del(a[alen-1])

delete_data(4)
print(a)