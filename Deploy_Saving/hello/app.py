from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    print("Home route was accessed!")  # Debug message
    return """<!DOCTYPE html>
<html>
<head>
    <title>Flask Page</title>
</head>
<body>
    <h1>Hello Naveen shetter</h1>
</body>
</html>"""

@app.route('/home2')
def home2():
    return render_template('home1.html')


@app.route("/reviews")
def reviews():
    return "Reviews page updated!"


@app.route("/ratings")
def ratings():
    return "Ratings page updated!"
    
@app.route('/products')
def products():
    return "Product page"



if __name__ == '__main__':
    app.run(debug=True)
