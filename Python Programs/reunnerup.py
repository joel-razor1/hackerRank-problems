n = int(input())
arr=input()
arr1=arr.split()
arr1_int=list(map(int,arr1))
unique=[]
for i in arr1_int:
    if i not in unique: 
        unique.append(i)
unique.remove(max(unique))
print(max(unique))


