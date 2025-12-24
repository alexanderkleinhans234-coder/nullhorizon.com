from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # /demo/ch
def index():
    return render_template("index.html")

@app.route("/demo/hn")
def demo_hn():
    return render_template("demo-hn.html")

if __name__ == "__main__":
    app.run(debug=True)
