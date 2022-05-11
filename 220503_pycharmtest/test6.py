#06 리스트 정렬과 리스트 뒤집기 [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어 보자
a=[1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)

#07. ['Life', 'is','too','short']리스트를 Life is too short 문자열로 만들어 출력해 보자.
a = ['Life','is','too','short']
result= " ".join(a)
print(result)

#07-2.
a = ['Life','is','too','short']
print(a[0]+" "+a[1]+" "+a[2]+" "+a[3])

result = " ".join(a)
print(result)

a= "Life is too short"
print(a.split())

#08 (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
t1 = (1,2,3)
t2 = (4,)
print(t1 + t2)
