from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check-review/")
def check_review():
    return render_template("check-review.html")

@app.route("/check-amazon-product/")
def check_amazon_product():
    return render_template("check-amazon-product.html")

@app.route("/risk/")
def risk():
    return render_template("risk.html")

@app.route("/pattern/")
def pattern():
    return render_template("pattern.html")

@app.route("/about/")
def about():
    return render_template("about.html")