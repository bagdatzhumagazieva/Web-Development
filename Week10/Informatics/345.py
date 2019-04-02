n=int(input())
i=1;
k=0;

while i<=n:
	x=int(input())
	if x == 0:
		k+=1;
	i+=1;

print(k)