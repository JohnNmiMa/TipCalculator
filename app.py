from flask import Flask, request, render_template

app = Flask(__name__)      

def isnumeric(numstring):
    try:
        i = float(numstring)
        return True;
    except ValueError, TypeError:
        return False;

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    fd=request.form
    error = ""

    mealcost = fd['meal_cost']
    if not isnumeric(mealcost):
        error = "Invalid data: please enter a number for the meal cost"
    tip = fd['tip_percentage']
    if not isnumeric(tip):
        error = "Invalid data: please enter a number for the tip percentage"

    return render_template('results.html', formdata=fd, error=error)

 
if __name__ == '__main__':
    app.run(debug=True)
