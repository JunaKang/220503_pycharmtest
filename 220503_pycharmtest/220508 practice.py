"%10s" % "hi"
"%0.4f" % 3.42134234
"I eat {0} apples". format(3)

number = 10
day = "three"
"I ate {0} apples. so I was sick {1} days.".format(number,day)
print('I ate 10 apples. so I was sick for three days.')

a=[1, 2, 3]
print(a[0]+a[2])

a = [1, 2, 3]
a[2] = 4
print(a)

a = [1, 2, 3]
del a[1]
print(a)

a = [1, 2, 3]
a.append(4)
print(a)



s2 = set("Hello")
print(s2)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)

a= True
b= False
print(type(a))

1 == 1
print(True)

2 > 1
print(True)

a = [1, 2, 3, 4]
while a:
    print(a.pop())

if []:
    print("참")
else:
    print("거짓")

bool('python')
print(True)

money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

x = 3
y = 2
if x > y:
    print("True")
else:
    print("False")

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['paper','handphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")

treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)