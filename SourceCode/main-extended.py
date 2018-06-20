import re
import math
import os
import speech_recognition as sr

r = sr.Recognizer()
r.pause_threshold = 0.5
r.non_speaking_duration = 0.4
r.energy_threshold = 700

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def quitProgram(a=True):
	if a:
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

def listen():
	mic = sr.Microphone()
	with mic as source:
		r.adjust_for_ambient_noise(source, duration=0.4)
		audio = r.listen(source)
	return r.recognize_google(audio)

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

	def text2int(self, textnum, numwords={}):
	    if not numwords:
	      units = [
	        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
	        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
	        "sixteen", "seventeen", "eighteen", "nineteen",
	      ]

	      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

	      scales = ["hundred", "thousand", "million", "billion", "trillion"]

	      numwords["and"] = (1, 0)
	      for idx, word in enumerate(units):    numwords[word] = (1, idx)
	      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
	      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

	    current = result = 0
	    for word in textnum.split():
	        if word not in numwords:
	        	self.menu("Word not legible")

	        scale, increment = numwords[word]
	        current = current * scale + increment
	        if scale > 100:
	            result += current
	            current = 0

	    return result + current

	def question(self, question):
		print(question +"(y/n): ")
		a = listen()
		print(a)
		if a == "yes":
			return True
		elif a == "no":
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

		print("Item Number (0 to cancel): ")
		itemNum = listen()
		
		if not itemNum.isdigit():
			itemNum = self.text2int(itemNum)
		else:
			itemNum = int(itemNum)

		if (itemNum == 0):
			self.menu()
		if itemNum < 0 or itemNum > len(items):
			self.menu("Input not within range") 
			return

		print(itemNum)
		itemNum = itemNum-1

		del self.orderItems[itemNum]
		self.menu()

	def addItem(self):
		clear()
		print(styliseTitle("item menu"))
		self.itemMenu()

		print("Item Number (0 to cancel): ")
		itemNum = listen()

		if not itemNum.isdigit():
			itemNum = self.text2int(itemNum)
		else:
			itemNum = int(itemNum)

		if (itemNum == 0):
			self.menu()
		if itemNum < 0 or itemNum > len(items):
			self.menu("Input not within range") 
			return

		print(itemNum)
		itemNum = itemNum-1

		print("Quantity (0 to cancel): ")
		quantity = listen()

		if not quantity.isdigit():
			quantity = self.text2int(quantity)
		else:
			quantity = int(quantity)

		if (itemNum == 0):
			self.menu()
		if quantity < 0:
			self.menu("Input not within range") 
			return

		print(quantity)

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

		menuNum = listen()
		if not menuNum.isdigit():
			menuNum = self.text2int(menuNum)
		else:
			menuNum = int(menuNum)

		if menuNum < 0 or menuNum > len(menuItems):
			self.menu("Input not within range") 
			return
		menuNum = int(menuNum)-1
		menuItems[menuNum]()

order = Order()