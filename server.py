from flask import Flask,render_template
app = Flask(__name__)

@app.route("/") # Revisit decorators if you unclear of this syntax
def index():
    return render_template('index.html')

@app.route("/lastname")
def show():
    return '<h1>Faruk Rahman</h1>'

@app.route ('/user/<username>')
def show_name(username):
    username = username.upper()
    return render_template('index.html',username=username)

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
   app.run(debug=True)