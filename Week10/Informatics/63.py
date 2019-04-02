n=int(input())
a=list(map(int, input().split()))

i=0;
k=0

while i<n:
	if i%2==0:
		print(a[i],end=' ');
	i+=1;
# print(k);4