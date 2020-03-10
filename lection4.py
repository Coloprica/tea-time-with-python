class Human:
	def __init__(self, name, last_name):
		self.name = name
		self.last_name = last_name

	def	sayHello(self):
		print(f'Hello, my name is {self.name}')


human1 = Human("John", "Doe")
human2 = Human("Sidney", "Hill")

human1.name = 'Johny'

human1.sayHello()
		