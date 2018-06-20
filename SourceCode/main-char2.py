i=("Macaroons(1) 1.5","Macaroons(8) 8","Cupcake 3.5","Slice 3.25","Assorted 12.5")
t=0
x=print
while 1:
	x(*i,sep='\n')
	a=input()
	if a.isdigit():
		t+=float(i[int(a)-1].split()[1])
	else:
		x(str(t) if "y"in a else str(t*1.1))
		break