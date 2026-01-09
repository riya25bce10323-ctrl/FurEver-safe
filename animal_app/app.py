from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

rescue_requests = []
adoption_list_data = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/rescue")
def rescue():
    return render_template("rescue.html")

@app.route("/submit", methods=["POST"])
def submit():
    rescue_requests.append({
        "animal": request.form["animal"],
        "location": request.form["location"]
    })
    return redirect(url_for("rescue_list"))

@app.route("/rescue-list")
def rescue_list():
    return render_template("rescue_list.html", rescues=rescue_requests)

@app.route("/adoption")
def adoption():
    return render_template("adoption.html")

@app.route("/adoption-submit", methods=["POST"])
def adoption_submit():
    adoption_list_data.append({
        "name": request.form["name"],
        "age": request.form["age"],
        "location": request.form["location"]
    })
    return redirect(url_for("adoption_list"))

@app.route("/adoption-list")
def adoption_list():
    return render_template("adoption_list.html", adoptions=adoption_list_data)



if __name__ == "__main__":
    app.run(debug=True)