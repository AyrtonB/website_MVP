from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", img_url='../static/img/pipeline.jpg')

@app.route("/map")
def map():
    return render_template("map.html", img_url='../static/img/boiling_bubbles.jpg')

@app.route("/trends")
def trends():
    return render_template("trends.html", img_url='../static/img/boiling_bubbles.jpg')



if __name__ == "__main__":
    app.run(debug=True)
