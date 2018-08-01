class Lion(object):
    def __init__(self, name, color, strength):
        self.name = name
        self.color = color
        self.strength = strength

class Tiger(object):
    def __init__(self, name, color, strength):
        self.name = name
        self.color = color
        self.strength = strength

George = Lion('George', 'Yellow', 100)
Sara = Tiger('Sara', 'Black', 100)
print(" I am a Lion, My name is ", George.name)
print(" I am a Tiger, My name is ", Sara.name)