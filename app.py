from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/admin")
def admin():
    return render_template("admin_dashboard.html")

@app.route("/lpc")
def lpc():
    return render_template("lpc_form.html")

@app.route("/assy")
def assy():
    return render_template("assy_form.html")

@app.route("/maintenance")
def maintenance():
    return render_template("maintenance_dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
