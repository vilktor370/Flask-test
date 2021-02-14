from processing import Calculator
from flask import Flask
import processing
# import sys
app = Flask(__name__)
# def calculating(c):
#     print(c,"Add:",c.add())
#     print(c,"Subtract:",c.minus())
#     print(c,"Multiply:",c.multiply())
#     print(c,"Divide:",c.divide())

# def main():
#     x = float(sys.argv[1])
#     y = float(sys.argv[2])
#     print("You input",sys.argv[1],sys.argv[1])
#     c = Calculator(x,y)
#     calculating(c)

@app.route('/')
def calc():
    c = Calculator(12,12)
    return str(c.add())
if __name__=="__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)