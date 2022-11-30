import time
from flask import Flask,render_template,request     #GET vs POST
import os

app = Flask(__name__)

graph_folder = os.path.join('Plots')
app.config['Graph_folder'] = graph_folder


@app.route('/index')            # http://localhost:5000/index ---> this is the url for  addition
def welcome_screen():  # deftn of the function       ---> 5 and 6 - function body
    print('inside addition...')
    #return "Addition function invoked.."
    return render_template('sample.html')

@app.route('/calculate',methods = ["POST"])            # http://localhost:5000/calculate ---> this is the url for  addition
def calculate():  # deftn of the function       ---> 5 and 6 - function body
    result = None
    if request.method == 'POST':
        formdata = request.form
        number1 = formdata.get('num1')
        number2 = formdata.get('num2')
        operation = formdata.get('op')
        sub1 = formdata.get('calc')
        sub2 = formdata.get('plot')

        if number1.isnumeric() and number2.isnumeric():
            number1 = int(number1)
            number2 = int(number2)
            if operation == 'Add':
                result = number1 + number2
            elif operation == 'Sub':
                result = number1 - number2
            elif operation == 'Mul':
                result = number1 * number2
            elif operation == 'Div':
                result = number1 / number2
            elif operation == 'Dou Num1':
                result = 2*number1
            elif operation == 'Dou Num2':
                result = 2 * number2
        else:
            result = "Invalid Values...!"
        print('inside calculate function',formdata)
        if sub1 == 'calculate' and number1 and number2 :
            return render_template('result.html',x = "The result of required operation on numbers ({},{}) is :".format(number1,number2) + str(result))
        else:
            return render_template('plotter.html')

@app.route('/recalculate',methods = ["POST"]) # http://localhost:5000/recalculate
def recalculate():
    return render_template('sample.html')

@app.route('/plot',methods = ["POST"])      # http://localhost:5000/plot
def ploter():
    import matplotlib.pyplot as plt
    plt.switch_backend('agg')
    print('inside plotter')
    #plt.clf()
    #plt.savefig('plot.png')
    if request.method == 'POST':
        formdata = request.form
        x_vec_f = formdata.get('x_data')
        y_vec_f = formdata.get('y_data')
        x_v = list(x_vec_f.replace(',', ''))
        y_v = list(y_vec_f.replace(',', ''))
        x_vec = [eval(elements) for elements in x_v]
        y_vec = [eval(elements) for elements in y_v]
        plt.plot(x_vec, y_vec)
        plt.savefig('Static\plot.jpg', dpi=200)
        plot1 = os.path.join(app.config['Graph_folder'], 'plot.jpg')

    return render_template('grapher.html', x = "The requested graph is :")


if __name__ == '__main__':
    app.run(debug=True)




'''
def addition(num1,num2):  # deftn of the function       ---> 5 and 6 - function body
    result = num1 + num2
    return result


answer = addition(10,20)        # line --> caller -- calling to the function
print(answer)                   # ans -- return value from the function...
'''