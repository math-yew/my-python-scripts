import webbrowser

def run(action):
	print("\n")
	if action == "name":
		name()
	elif action == "web":
		web()
	elif action == "mult":
		mult()
	else:
		other()

myName = "buddy"
		
def name():
	fname = input("What is your name? ")
	print("Hello there, " + fname)
	global myName
	myName = fname
	restart()
			
def web():
	print("What website would you like to open? ")
	website = input("URL: ")
	webbrowser.open(website)
	restart()
			
def other():
	print("That is not an option.  Try again " + myName)
	restart()
	
def mult():
	print("Let's multiply two numbers. ")
	a = input("What is the first number? ")
	b = input("What is the second number? ")
	c = int(a)*int(b)
	print(a + " x " + b + " = " + str(c))
	restart()
	
def restart():	
	print("\n")
	x = input("name, web, or mult? ")
	run(x)
	
restart()