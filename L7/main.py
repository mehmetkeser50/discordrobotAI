from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/index")
def index1():
    return render_template("index.html")
@app.route("/index2")
def index2():
    return render_template("index2.html")
@app.route("/index3")
def index3():
    return render_template("index3.html")
@app.route("/index4")
def index4():
    return render_template("index4.html")
@app.route("/index5")
def index5():
    return render_template("index5.html")
@app.route("/index6")
def index6():
    return render_template("index6.html")
@app.route("/index7")
def index7():
    return render_template("index7.html")
@app.route("/index8")
def index8():
    return render_template("index8.html")





if __name__ =="__main__":
    app.run(debug= True)
   
    