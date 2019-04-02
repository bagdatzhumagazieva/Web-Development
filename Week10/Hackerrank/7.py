n=int(input())

i=0;
l=1569.0
m=[]

while i<n:
	s=str(input())
	x=float(input())
	if l<=x:
		l=x;
		m.append(s);

print(m);
