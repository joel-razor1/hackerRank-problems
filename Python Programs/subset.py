result=[]
for i in range(int(raw_input())):
    j=int(raw_input())
    a =set(map(int, raw_input().split()))
    k=int(raw_input())
    b =set(map(int, raw_input().split()))
    result.append(a.issubset(b))

for l in range (0,len(result)):
    print(result[l])