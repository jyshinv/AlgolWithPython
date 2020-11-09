#나중에 이해하기...
#v1은 n의 범위가 10만 이하이므로, 이처럼 일일이 1씩 빼도 문제를 해결할 수 있다.
#하지만 n이 100억 이상의 큰 수가 되는 경우를 가정했을 때에서 빠르게 동작하려면, n이 k의 배ㅜㅅ가 되도록
#효율적으로 한 번에 빼는 방식으로 소스코드를 작성할 수 있다.

#n,k를 공백으로 구분하여 입력받기
n,k = map(int, input().split())
result = 0

while True :
    #(n==k로 나누어떨어지는 수)가 될때까지 1씩 빼기
    target = (n//k)*k
    result += (n-target)
    n = target

    #n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n<k :
        break

    #k로 나누기
    result +=1
    n//=k

#마지막으로 남은 수에 대하여 1씩 빼기
result +=1
print(result)