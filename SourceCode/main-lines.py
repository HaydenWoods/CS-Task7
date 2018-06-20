i=[[["Macaroons(1)",1.50],["Macaroons(8)",8.00],["Cupcake",3.50],["Slice",3.25],["Assorted",12.50]],[]]
while 1:
	print("\n".join(map(str,[i[0][x][:2] for x in range(len(i[0]))])))
	i[1].append(i[0][int(input("Item: "))-1][1])
	print(sum([i[1][x]for x in range(len(i[1]))]))