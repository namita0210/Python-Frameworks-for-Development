from flask import Flask, redirect, url_for

#Create an instance of flask class
app = Flask(__name__)

@app.route("/") # decorator which tells the application which URL should call the associated function
def home():
    return '''This is the home page <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f7f7f7;
        }
        header {
            background-color: #3498db;
            color: white;
            text-align: center;
            padding: 2em 0;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2em;
        }
        h1 {
            font-size: 3em;
            margin-bottom: 0.5em;
        }
        p {
            font-size: 1.2em;
            color: #333;
            line-height: 1.6;
        }
        .cta-button {
            display: inline-block;
            padding: 1em 2em;
            background-color: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        .cta-button:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to Our Website</h1>
    </header>
    <div class="container">
        <p>Thank you for visiting our website. We provide amazing services and top-notch quality.</p>
        <a href="#" class="cta-button">Get Started</a>
    </div>
</body>
</html>
'''

@app.route("/<name>") # dynamic URL
def name(name):
    return f"""Welcome {name}"""

@app.route("/admin") # dynamic URL
def admin():
    return redirect(url_for("home")) # redirect to home page

if __name__ == "__main__":
    app.run(debug=True) # run the application in debug mode