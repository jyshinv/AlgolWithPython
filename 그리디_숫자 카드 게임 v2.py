#행 n과 열 m 입력받기
n,m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))

    min_value =  10001
    #현재 줄에서 가장 작은 수 찾기
    for j in data :
        min_value = min(min_value,j)

    #가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

