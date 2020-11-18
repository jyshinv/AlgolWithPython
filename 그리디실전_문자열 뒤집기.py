#data를 입력받는다.
data = input()
case0=0 #1을 0으로 바꾸는 경우 count
case1=0 #0을 1로 바꾸는 경우 count

#첫번째 원소 처리하기
if data[0] == '1' : #1을 0으로 뒤집는 경우이므로 case0에 count
    case0 +=1
else: #0을 1로 바꾸는 경우이므로 case1 에 count
    case1 +=1


#두번째 원소부터 모든 원소를 확인한다.
for i in range(len(data)-1) : #i는 0부터 (사용자가 입력한 수-1)
    if data[i] != data[i+1] :
        if data[i] == '1' :
            case0 +=1
        else :
            case1 +=1

print(min(case0, case1))





