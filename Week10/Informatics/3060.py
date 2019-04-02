n=int(input())
k=0;

while n!=0:
	k+=n%2
	n//=2;

if k==1:
	print("YES")
else:
	print("NO")