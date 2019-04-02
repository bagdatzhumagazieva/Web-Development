a=int(input())
b=int(input())

if a!=0:
	s=a*b%109;
		
else: 
	s=(109+(a*b)%109)%109
	

print(s)