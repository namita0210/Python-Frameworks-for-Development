from flask import Flask, redirect, url_for

#Create an instance of flask class
app = Flask(__name__)

@app.route("/") # decorator which tells the application which URL should call the associated function
def home():
    return '''This is the home page'''


if __name__ == "__main__":
    app.run(debug=True) # run the application in debug mode