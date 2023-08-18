self_num = [0] * 10000

def self_num_(num):
    num_len = len(str(num))
    result = 0
    for i in range(num_len):
        result += int(str(num)[i])
    result += num
    
    return result
for i in range(1,10000):
    if self_num_(i) < 10000:
        self_num[self_num_(i)] +=1
    

for i in range(1,10000):
    if self_num[i] ==0:
        print(i)

#####set 사용법을 알아두자
