from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run()