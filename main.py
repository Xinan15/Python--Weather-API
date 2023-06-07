from flask import Flask, render_template

app = Flask(__name__)


# create an app variable
# domain name + /home
@app.route("/")
def home():
    return render_template("home.html")


# Now we need to connect the html pages with this website object
# use @ symbol to refer to the app variable and refer to the root method of the app object

@app.route("/api/v1/<station>/<date>")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
# by default, the app will run on port 5000,
# but we can specify the port argument here
# app.run(debug=True, port=5001)
