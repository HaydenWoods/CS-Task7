i=("Macaroons(1) 1.5","Macaroons(8) 8","Cupcake 3.5","Slice 3.25","Assorted 12.5")
t=0;n=input;x=print;z=str
while 1:
	x(*i,sep='\n')
	a=int(n())
	t+=float(i[a-1].split()[1])
	if a==0:
		x(z(t)if n() else z(t*1.1))
		break