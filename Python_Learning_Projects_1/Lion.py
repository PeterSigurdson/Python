class Lion(object):

	def __init__(self, name, color, strength):
		self.name = name
		self.color = color
		self.strength = strength

class Lion(object):

	def __init__(self, name, color, strength):
		self.name = name
		self.color = color
		self.strength = strength

	
if __name__ == "__main__":
	
	boyNamesFile = open('BOYNames.txt', 'r') 
	girlNamesFile = open('GirlNames.txt', 'r') 
	
	lines = boyNamesFile.read()
	boyNames = [] 
	for line in boyNamesFile:
		boyNames.append(line)
	
	girlNames =[]
	for line in girlNamesFile:
		girlNames.append(line)

	for i in range(1,20):
		Lion(boyNames.pop(), 'b', 3)
		
	print('fini')

