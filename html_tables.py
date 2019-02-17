from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

@app.route('/users')
def users():
	for i users:
		

		print(['first_name']+{'last_name'})
    return render_template("html_tables.html")
users = (
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
);

@app.route("/<x>/<y>")
def checkerboard2(x, y):
    x = int(x)
    y = int(y)
    return render_template("chkrbrd2.html", x = x, y = y)

if __name__ == "__main__":
    app.run(debug=True)