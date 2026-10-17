@app.route("/machine_master")
def machine_master():
    return render_template("machine_master.html")
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Login Page
@app.route("/")
def login():
    return render_template("login.html")

# Login Validation
@app.route("/login", methods=["POST"])
def user_login():

    username = request.form["username"]
    password = request.form["password"]

    # Demo Login
    if username == "admin" and password == "1234":
        return redirect("/admin")

    return "Invalid Login"

# Admin Dashboard
@app.route("/admin")
def admin():
    return render_template("admin_dashboard.html")

# LPC Form
@app.route("/lpc")
def lpc():
    return render_template("lpc_form.html")

# ASSY Form
@app.route("/assy")
def assy():
    return render_template("assy_form.html")

# Maintenance Dashboard
@app.route("/maintenance")
def maintenance():
    return render_template("maintenance_dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
