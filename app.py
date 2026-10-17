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
    
 @app.route("/machine_master")
def machine_master():
    return render_template("machine_master.html")

@app.route("/operator_master")
def operator_master():
    return render_template("operator_master.html")
@app.route("/technician_master")
def technician_master():
    return render_template("technician_master.html
    
   @app.route("/technician_master")
def technician_master():
    return render_template("technician_master.html") 
    
@app.route("/problem_master")
def problem_master():
    return render_template("problem_master.html")

@app.route("/lpc")
def lpc():
    return render_template("lpc_form.html")

@app.route("/maintenance")
def maintenance():
    return render_template("maintenance_dashboard.html")

@app.route("/user_master")
def user_master():
    return render_template("user_master.html")
@app.route("/applicator_master")
def applicator_master():
    return render_template("applicator_master.html")

@app.route("/terminal_master")
def terminal_master():
    return render_template("terminal_master.html")
    
@app.route("/reports")
def reports():
    return render_template("reports.html")
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    # Demo Users

    if username == "admin" and password == "1234":
        return redirect("/admin")

    elif username == "lpc" and password == "1234":
        return redirect("/lpc")

    elif username == "assy" and password == "1234":
        return redirect("/assy")

    elif username == "maintenance" and password == "1234":
        return redirect("/maintenance")

    return "Invalid Login"
    
    from flask import Flask, render_template, request, redirect
    
if __name__ == "__main__":
    app.run(debug=True)
