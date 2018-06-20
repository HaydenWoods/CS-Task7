#Import regular expressions for string editing
import re
#Import math functions
import math
#Import os functions for clearing screen
import os

#Clear the screen when called
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

#Quit the program but clear the screen first
def quitProgram(clear=True):
	if clear:
		clear()
	exit()

#Turn a normal "camelCase" title into proper casing using Regular Expressions
#Input: currencyFormat Return: Currency Format
def spaceTitle(title):
	#Finds a word in the text with any characters that are capitalised from only and then 
	#puts together group one and two, with whitespace inbetween. Adding .title() turns the first
	#character to a capital as well
	title = re.sub(r"(\w)([A-Z])", r"\1 \2", title).title()
	return title

#Stylise the title so that it has an even spacing of "=" on each side
def styliseTitle(title):
	#Turns the title into a title with all uppercase and two spaces on either side
	title = " " + title.upper() + " "
	#Gets the amount of symbols on both sides by getting the total length and taking away the title and dividing by 2
	symbolsLength = ((30 - len(title)) / 2)
	#Formats the entire title by adding a dash on either side and multiplying the equals sign by the amount on either side.
	#If it is an odd amount then it will be floored on one side and ceiling on the other for example
	#17 Length: Would be 8.5, which would result in 8 on the left and 9 on the right, still keeping it even
	title = "-" + ("="*math.floor(symbolsLength)) + title + ("="*math.ceil(symbolsLength)) + "-\n"
	return title

#Change the format of a text into currency, two decimal places
def currencyFormat(price):
	price = "$" + str('{0:.2f}'.format(price))
	return price

#Defines a class that when instantiated will hold the name and price of the item
class Item(object):
	def __init__(self, name, price):
		self.name = name
		self.price = price

#Has a list of all the items that will generally be looped through and not accessed directly
#It will only be accessed directly through user input
items = [
	Item("Macaroons(1)", "1.50"),
	Item("Macaroons(8)", "8.00"),
	Item("Cupcake", "3.50"),
	Item("Slice", "3.25"),
	Item("Assorted Box", "12.50"),
	Item("Lamington", "3.00")
]

#Defines a class for the order, this would allow later for there to be multiple orders
#This could be useful for different payment types on each order
class Order(object):
	#Run on the instantiate of the class nad will set all the variables that will be used in the class
	def __init__(self):
		self.orderItems = []
		self.total = 0.0
		self.menu()
		
	#Basic function for yes/no questions, returns True or False
	def question(self, question):
		a = input(question +"(y/n): ").strip(" ").lower()
		if a == "y":
			return True
		elif a == "n":
			return False
		else:
			self.menu("Input one of the two options")
			return False

	#Displays item menu
	def itemMenu(self):
		#Prints all the items in the items list with the appropriate styling (makes sure all lines are inline)
		names = [items[i].name for i in range(len(items))]
		longest = len(max(names, key=len))
		for i in range(len(items)):
			spaces = " " * (longest - len(items[i].name))
			start = str(i+1) + ". "
			print(start + items[i].name + spaces + " | " + currencyFormat(float(items[i].price)))

	def cartMenu(self):
		#Prints all the items in the cart with the appropriate styling appplied
		for i in range(len(self.orderItems)):
			start = str(i+1) + ". "
			print(start + str(self.orderItems[i][0]) +" - "+ currencyFormat(float(self.orderItems[i][1])) +" x "+ str(self.orderItems[i][2]) +" - "+ currencyFormat(float(self.orderItems[i][3])))

	def deleteItem(self):
		clear()
		#Checks if there is an item in the cart
		if len(self.orderItems) <= 0:
			self.menu("No items in cart")
			return

		print(styliseTitle("item cart"))
		self.cartMenu()

		#Takes an input from the user and does various checks to make sure it is valid
		itemNum = input("\nItem Number(0 to cancel): ")
		#Checks if it is equal to 0 and quits if it is
		if itemNum == "0":
			self.menu()
			return
		#Checks if it is not a number and quits if it is
		if not itemNum.isdigit():
			self.menu("Input not a number")
			return
		#Checks if it is less than or equal to 0 characters and quits if it is
		if len(itemNum) <= 0:
			self.menu("Input not greater than 0 characters")
			return
		#Checks if it is more than the length of the list or less than 0 and quits if it is
		if int(itemNum) < 0 or int(itemNum) > len(self.orderItems):
			self.menu("Input not within range") 
			return
		#Takes away one from the input to turn the real number into an index referencable against a list
		itemNum = int(itemNum)-1

		#Deletes the corresponding element from the list
		del self.orderItems[itemNum]
		self.menu()

	def addItem(self):
		clear()
		print(styliseTitle("item menu"))
		self.itemMenu()

		#Takes an input from the user and does various checks to make sure it is valid
		itemNum = input("\nItem Number(0 to cancel): ")
		#Checks if it is equal to 0 and quits if it is
		if itemNum == "0":
			self.menu()
			return
		#Checks if it is not a number and quits if it is
		if not itemNum.isdigit():
			self.menu("Input not a number")
			return
		#Checks if it is less than or equal to 0 characters and quits if it is
		if len(itemNum) <= 0:
			self.menu("Input not greater than 0 characters")
			return
		#Checks if it is more than the length of the list or less than 0 and quits if it is
		if int(itemNum) < 0 or int(itemNum) > len(items):
			self.menu("Input not within range")  
			return
		#Take one to turn the user input into an index usable against a list
		itemNum = int(itemNum)-1

		#Takes a quanitity from the user an does various checks to make sure it is valid
		quantity = input("Quantity(0 to cancel): ")
		#Checks if it is equal to 0 and quits if it is
		if quantity == "0":
			self.menu()
			return
		#Checks if it is not a number and quits if it is
		if not quantity.isdigit():
			self.menu("Input not a number")
			return
		#Checks if it is less than or equal to 0 characters and quits if it is
		if len(quantity) <= 0:
			self.menu("Input not greater than 0 characters")
			return
		#Checks if it is more than the length of the list or less than 0 and quits if it is
		if int(quantity) <= 0:
			self.menu("Input less than or equal to 0") 😡
			return
		#Turns the quantity into an integer
		quantity = int(quantity)

		#Appends the item to the order items list with the name, price, quantity and the total price
		self.orderItems.append([items[itemNum].name, items[itemNum].price, quantity, float(items[itemNum].price)*quantity])
		self.menu()

	def checkout(self):
		clear()

		print(styliseTitle("checkout"))
		self.cartMenu()

		#Checks if there is items in the cart, cant checkout unless there is
		if len(self.orderItems) <= 0:
			self.menu("No items in cart")
			return

		#Asks if you are sure you are finished with your order
		if not self.question("\nOrder Finished?"):
			self.menu()
			return

		#Sums up all the items that have been appended to the order items list
		self.total = sum([self.orderItems[i][3] for i in range(len(self.orderItems))])
		#Asks if you are going to dine in and adds the appropriate tax if so
		if self.question("Dining In?"):
			self.total = self.total * 1.1
		self.total = round(self.total, 2)

		#Prints the total cost in currency format
		print("\nTotal Order Cost: " + currencyFormat(self.total))
		quitProgram(False)


	#Displays the main menu and will print an error if one is passed to it, if not it will be its default empty string
	def menu(self, error=""):
		clear()
		print(styliseTitle("menu"))

		#Checks if the errors length is less than 1, if so dont print
		#If this wasnt done there would always be an empty line in place
		if len(error) >= 1:
			print(error + "\n")

		#Defines all the functions that can be done by referencing existing function names
		menuItems = [self.addItem, self.deleteItem, self.checkout, quitProgram]
		#Loops through the items and prints their name with the appropriate styling done through the use of the 
		#spaceTitle function.
		for i in range(len(menuItems)):
			print(str(i+1) + ". " + spaceTitle(menuItems[i].__name__))

		#Takes an input for the menu number choice and checks with various methods if it is valid
		menuNum = input("\nChoice: ")
		if menuNum == "0":
			self.menu("Input not within range")
			return
		if not menuNum.isdigit():
			self.menu("Input not a number")
			return
		if len(menuNum) <= 0:
			self.menu("Input not greater than 0 characters")
			return
		if int(menuNum) < 0 or int(menuNum) > len(menuItems):
			self.menu("Input not within range") 
			return
		menuNum = int(menuNum)-1

		#Calls the functions that is at the index the users input
		menuItems[menuNum]()

#Creates an instance of the order class
order = Order()