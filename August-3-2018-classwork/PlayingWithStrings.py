class PlayingWithStrings:

	def SayHello(self, friendsname):
		message = ""
		message = "hello!!!! ", friendsname
		return message

object1 = PlayingWithStrings()
print(object1.SayHello("Peanut"))

object2 = PlayingWithStrings()
print(object2.SayHello("Bill"))