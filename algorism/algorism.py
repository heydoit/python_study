#함수 선언부
#전역 변수부
a = ['다현','정연','쯔위','사나','지효']
#메인 코드부
print(a)

a.append(None)
a[5] = '모모'
print(a)

a.append(None)
a[6] = a[5]
a[5] = None
a[5] = a[4]
a[4] = None
a[4] = a[3]
a[3] = '미나'
print(a)

a[4] = None
a[4] = a[5]
a[5] = None
a[5] = a[6]
a[6] = None

del(a[6])
print(a)