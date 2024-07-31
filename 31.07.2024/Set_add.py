n=int(input())
k=[]
for i in range(n):
    k.append(input())
s=set()
for i in k:
    if i not in s:
        s.add(i)
print(len(s))
