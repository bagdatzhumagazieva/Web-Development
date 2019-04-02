n=int(input())
a=list(map(int, input().split()))

i=1;
k=0

while i<n:
	if a[i-1]<a[i]:
		k+=1;
	i+=1;
print(k)