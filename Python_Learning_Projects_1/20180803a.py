class PlayingWithStrings:

    def SayHello(self, friendsname):
        message = ""
        message = "hello!!!! ", friendsname
        return message

object1 = PlayingWithStrings()
msg1 = object1.SayHello("Peanut")
# print(msg1[0])

# handling tuples https://www.digitalocean.com/community/tutorials/understanding-tuples-in-python-3 
# print("the length of my tuple is ", len(msg1))

for index, element in enumerate(msg1):
    print (element, index)

object2 = PlayingWithStrings()
# print(object2.SayHello("Bill"))