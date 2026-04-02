from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<P>Hello, world!</p>"

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "만나서 반가워요"


@app.route("/user/<userId>")
def profile(userId):
    return f"{userId}\' profile"


if __name__ == '__main__':
    app.run(debug = True)
