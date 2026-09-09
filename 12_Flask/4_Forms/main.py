from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello():
    if request.method == "POST":
        with open("new.txt", "a") as f:
            f.write(f"{request.form['name']} and {request.form['email']}\n")
        return render_template("index.html")
    else:
        return render_template("index.html")
        
app.run(debug=True)