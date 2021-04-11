num = int(input("자연수를 입력: "))
result = 0

for i in range(num+1):
    if i % 2 == 0:
        result += i

print(result)