#1. 다음 코드의 결괏값은 무엇일까?(If문)

#2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자.(while문)
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

#3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
i = 0
while True:
    i +=1
    if