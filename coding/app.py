
from flask import Flask, render_template,request

app=Flask(__name__,template_folder="Template")
@app.route("/")
def index():
    return render_template("pinestay-master/index.html")

@app.route("/morning")
def mor():
    name=request.args.get("name")
    if not name:
        return render_template("fail.html")
    return render_template("morning.html",name=name) #"<h1>Good Morning, SUNNY DAN!</h1>"

