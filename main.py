from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') #decorador
def hello_world():
    return render_template("index.html")

@app.route('/Register') #decorador
def news():
    return render_template("Register.html")

if __name__ == "__main__":
    app.run(debug=True)