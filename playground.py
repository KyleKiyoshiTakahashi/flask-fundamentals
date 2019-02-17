from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/play')
def play():
	return render_template("index.html")

@app.route("/play/<x>")
def play(x):
    x = int(x)
    return render_template("play.html", num = x)

@app.route("/play/<x>/<y>")
def play_2(x,y):
    x = int(x)
    return render_template("play.html", num = x, color = y)

if __name__=="__main__":
    app.run(debug=True)