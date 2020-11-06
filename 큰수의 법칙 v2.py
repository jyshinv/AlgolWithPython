#n,m,k를 공백으로 구분하여 입력받기
n,m,k = map(int, input().split())

#n개의 수를 공백으로 구분하여 입력받기 (위의 코드를 list로 감싸주면 된다.)
data = list(map(int, input().split()))

#오름차순으로 정렬해주기
data.sort()
first = data[n-1] #가장 큰 수
second = data[n-2] #두번째로 큰 수

#가장 큰 수가 더해지는 횟수 계산 : 반복 수열*k + m이 k+1로 나누어떨어지지 않는 경우
count = int(m/(k+1))*k + m%(k+1)

#계산하기
result = 0
result += first*count   #가장 큰 수 더하기
result += second*(m-count) #두 번째로 큰 수 더하기

#결과 출력
print(result)

