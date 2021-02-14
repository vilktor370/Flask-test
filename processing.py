import sys
class Calculator:
    x = 0
    y = 0 
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
    def add(self):
        return self.x + self.y

    def minus(self):
        return self.x - self.y

    def multiply(self): 
        return self.x * self.y

    def divide(self): 
        return self.x / self.y
