# HeRo: Hebe Huang and Roshani Shrestha
# SoftDev pd2
# TEDxSoftDev: Mathematica (One-pager python file)
# 2022-05-16
# time spent: ??? hours

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def page():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()