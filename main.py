class Robot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return self.name + " says: Hello, I am " + self.name + " the robot!"

tom = Robot("Tom")
print(tom.greet())
jerry = Robot("Jerry")
print(jerry.greet())