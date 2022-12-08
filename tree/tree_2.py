# 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


# 전역
memory = []
root = None
nameAry = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

# 메인

node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name
    
    current = root
    while True:
        if name < current.data :
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

    memory.append(node)
print('이진 탐색 트리 완료')


class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


memory = []
root = None
nameAry = ['유진','정민','하루','나라','둥이']

node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
    node=TreeNode


# 복습
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

memory = []
root = None
nameAry = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스']

node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name
    current = root

    while True:
        if(name < current.data):
            if(current.left == None):
                current.left = node
                break
            current = current.left

        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
    memory.append(node)

print('이진 탐색 완료')

findName = '바마무'

current = root
while True:
    if (findName == current.data):
        print(findName, '뮤비가 나옵니다.')
        break
    elif (findName < current.data) :
        if (current.left == None):
            print(findName, '없어요')
            break
        current = current.left
    else:
        if (current.right == None) :
            print(findName, '없어요')
            break
        current = current.right
        