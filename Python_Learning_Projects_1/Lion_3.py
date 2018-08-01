import random

class Lion(object):
    def __init__(self, name, color, strength):
        self.name = name
        self.color = color
        self.strength = strength
    
    def speak(self):
        return 'Growl !'

class Tiger(object):
    def __init__(self, name, color, strength):
        self.name = name
        self.color = color
        self.strength = strength
    def speak(self):
        return 'Be QUIET!'

George = Lion('George', 'Yellow', random.randint(1,101))
Sara = Tiger('Sara', 'Black', random.randint(1,101))
print(" I am a Lion, My name is ", George.name, George.speak(), "My Strength is : ", George.strength)
print(" I am a Tiger, My name is ", Sara.name, Sara.speak(), "My Strength is : ", Sara.strength)