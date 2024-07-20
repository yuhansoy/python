# 사용자로부터 숫자를 입력받아 홀수인지 짝수인지 판별하는 
# 프로그램을 작성하세요.

n=int(input('몇개를 입력?'))
a=[]

for i in range(n):
    d=int(input('수?'))
    a.append(d)

print('홀수:',end=" ")

for i in range(n):
    if a[i]%2==1:
        print(a[i],end=" ")

print()
print('짝수:',end=" ")

for i in range(n):
    if a[i]%2==0:
        print(a[i],end=" ")