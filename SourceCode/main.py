import re
import math
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def quitProgram(clear=True):
	if clear:
		clear()
	exit()

def spaceTitle(title):
	title = re.sub(r"(\w)([A-Z])", r"\1 \2", title).title()
	return title

def styliseTitle(title):
	title = " " + title.upper() + " "
	symbolsLength = ((30 - len(title)) / 2)
	title = "-" + ("="*math.floor(symbolsLength)) + title + ("="*math.ceil(symbolsLength)) + "-\n"
	return title

def currencyFormat(price):
	price = "$" + str('{0:.2f}'.format(price))
	return price

class Item(object):
	def __init__(self, name, price):
		self.name = name
		self.price = price

items = [
	Item("Macaroons(1)", "1.50"),
	Item("Macaroons(8)", "8.00"),
	Item("Cupcake", "3.50"),
	Item("Slice", "3.25"),
	Item("Assorted Box", "12.50"),
	Item("Lamington", "3.00")
]

class Order(object):
	def __init__(self):
		self.orderItems = []
		self.total = 0.0
		self.menu()	

	def question(self, question):
		a = input(question +"(y/n): ").strip(" ").lower()
		if a == "y":
			return True
		elif a == "n":
			return False
		else:
			self.menu("Input one of the two options")
			return False

	def itemMenu(self):
		names = [items[i].name for i in range(len(items))]
		longest = len(max(names, key=len))
		for i in range(len(items)):
			spaces = " " * (longest - len(items[i].name))
			start = str(i+1) + ". "
			print(start + items[i].name + spaces + " | " + currencyFormat(float(items[i].price)))

	def cartMenu(self):
		for i in range(len(self.orderItems)):
			start = str(i+1) + ". "
			print(start + str(self.orderItems[i][0]) +" - "+ currencyFormat(float(self.orderItems[i][1])) +" x "+ str(self.orderItems[i][2]) +" - "+ currencyFormat(float(self.orderItems[i][3])))

	def deleteItem(self):
		clear()
		if len(self.orderItems) <= 0:
			self.menu("No items in cart")
			return

		print(styliseTitle("item cart"))
		self.cartMenu()

		itemNum = input("\nItem Number(0 to cancel): ")
		if itemNum == "0":
			self.menu()
			return
		if not itemNum.isdigit():
			self.menu("Input not a number")
			return
		if len(itemNum) <= 0:
			self.menu("Input not greater than 0 characters")
			return
		if int(itemNum) < 0 or int(itemNum) > len(self.orderItems):
			self.menu("Input not within range") 
			return
		itemNum = int(itemNum)-1

		del self.orderItems[itemNum]
		self.menu()

	def addItem(self):
		clear()
		print(styliseTitle("item menu"))
		self.itemMenu()

		itemNum = input("\nItem Number(0 to cancel): ")
		if itemNum == "0":
			self.menu()
			return
		if not itemNum.isdigit():
			self.menu("Input not a number")
			return
		if len(itemNum) <= 0:
			self.menu("Input not greater than 0 characters")
			return
		if int(itemNum) < 0 or int(itemNum) > len(items):
			self.menu("Input not within range")  
			return
		itemNum = int(itemNum)-1

		quantity = input("Quantity(0 to cancel): ")
		if quantity == "0":
			self.menu()
			return
		if not quantity.isdigit():
			self.menu("Input not a number")
			return
		if len(quantity) <= 0:
			self.menu("Input not greater than 0 characters")
			return
		if int(quantity) <= 0:
			self.menu("Input less than or equal to 0")  
			return
		quantity = int(quantity)

		self.orderItems.append([items[itemNum].name, items[itemNum].price, quantity, float(items[itemNum].price)*quantity])
		self.menu()

	def checkout(self):
		clear()

		print(styliseTitle("checkout"))
		self.cartMenu()

		if len(self.orderItems) <= 0:
			self.menu("No items in cart")
			return

		if not self.question("\nOrder Finished?"):
			self.menu()
			return

		self.total = sum([self.orderItems[i][3] for i in range(len(self.orderItems))])
		if self.question("Dining In?"):
			self.total = self.total * 1.1
		self.total = round(self.total, 2)

		print("\nTotal Order Cost: " + currencyFormat(self.total))
		quitProgram(False)

	def menu(self, error=""):
		clear()
		print(styliseTitle("menu"))

		if len(error) >= 1:
			print(error + "\n")

		menuItems = [self.addItem, self.deleteItem, self.checkout, quitProgram]
		for i in range(len(menuItems)):
			print(str(i+1) + ". " + spaceTitle(menuItems[i].__name__))

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
		menuItems[menuNum]()

order = Order()