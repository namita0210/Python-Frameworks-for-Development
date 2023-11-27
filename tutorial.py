from flask import Flask, redirect, url_for

#Create an instance of flask class
app = Flask(__name__)

@app.route("/") # decorator which tells the application which URL should call the associated function
def home():
    return '''This is the home page'''

@app.route("/<name>") # dynamic URL
def user(name):
    return f"""Welcome {name}"""

@app.route("/admin") 
def admin():
    return redirect(url_for("user", name = "FantasticBaby")) # redirect to home page

if __name__ == "__main__":
    app.run(debug=True) # run the application in debug mode