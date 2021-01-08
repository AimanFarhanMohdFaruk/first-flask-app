from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<name>")
def index(name):
    signed_in = True
    name = name.upper()
    return render_template('index.html', name=name, signed_in=signed_in)

if __name__ == '__main__':
    app.run()