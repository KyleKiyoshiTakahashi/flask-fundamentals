from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def checkerboard():
    return render_template("chkrbrd.html")

@app.route("/<x>/<y>")
def checkerboard2(x, y):
    x = int(x)
    y = int(y)
    return render_template("chkrbrd2.html", x = x, y = y)

if __name__ == "__main__":
    app.run(debug=True)