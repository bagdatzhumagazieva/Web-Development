n=int(input())
a=list(map(int, input().split()))

i=1;
k=0

while i<n:
	if a[i-1]*a[i]>0: 
		k+=1;
	i+=1;
	
if k>0:	
	print("YES");
else:
	print("NO");