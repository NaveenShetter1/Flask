from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return """<!DOCTYPE html>
<html>
<head>
    <title>Flask Page</title>
</head>
<body>
    <h1>Welcome to my Flask App!....Naveen shetter</h1>
</body>
</html>"""


@app.route("/reviews")
def reviews():
    return "Reviews page updated!"

if __name__ == "__main__":
    app.run(debug=True)
