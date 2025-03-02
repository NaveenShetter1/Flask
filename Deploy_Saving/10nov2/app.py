from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def rooot():
    return 'Hi form is submitted'

@app.route('/predict', methods=['POST','GET','DELETE','put','patch'])
def predict():
    if request.method == 'POST':
        # Fetching form data
        first_name = request.form['First name']
        second_name = request.form['second name']
        number = request.form['number']

      

        # You can perform some logic here, such as storing the data or using it
        return f"Submitted Info: {first_name} {second_name}, {number}"

    return render_template('new.html')

if __name__ == "__main__":
    app.run(debug=True)
