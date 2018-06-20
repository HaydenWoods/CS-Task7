#Defines string with all the elements 5 characters apart
l='MMCSAaaulsccpisaaccorraerook tooe enn  d18'
#Defines prices, the starting number, the starting price which is -(the first price halved),n which replaces input
#and z which replaces print
o=[3,16,7,6.5,25];b=1;p=-1.5;n=input;z=print
#Loops through until b is not a number in which case it will quit
while b:
	#Loops through the length of every 5th element in the list
	for s in range(5):z(l[s::5],o[s]/2)
	#Adds the price at the index to the total price
	p+=o[b-1]/2;b=int(n())
#Works out the total if there is no input, does it by 1.1 
z(p*1.1if n()else p)
