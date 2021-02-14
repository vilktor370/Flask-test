from processing import Calculator
from flask import Flask, render_template, request
import processing
# import sys
app = Flask(__name__,template_folder='html')
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

@app.route('/', methods=['GET', 'POST'])
def calc():
    if request.method == 'GET':
        return render_template('calc.html')
    elif request.method == 'POST':
        x = request.args['x']
        y = request.args['y']
        # print(x,y)
        # c = Calculator(1,2)
        # final=f"Add: {c.add()}<br>Subtract: {c.minus()}\
        #     <br>Multiply: {c.multiply()}<br>Divide: {c.divide()}"
        # return final
        return x,y
        
if __name__=="__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)