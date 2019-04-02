n=int(input())
a=list(map(int, input().split()))

# i=1;
# a=[]
ind=1;
# while i<=n:
# 	x=int(input(),end=' ')
# 	a.append(x);
# 	i+=1;



k=0
while ind<n-1:
	if a[ind-1] < a[ind] and a[ind+1]<a[ind]:
 		k+=1

	ind +=1

print(k)