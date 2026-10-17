import pymysql
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# ==========================
# LOGIN
# ==========================

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "1234":
        return redirect("/admin")

    elif username == "lpc" and password == "1234":
        return redirect("/lpc")

    elif username == "assy" and password == "1234":
        return redirect("/assy")

    elif username == "maintenance" and password == "1234":
        return redirect("/maintenance")

    return "Invalid Login"


# ==========================
# DASHBOARD
# ==========================

@app.route("/admin")
def admin():
    return render_template("admin_dashboard.html")


@app.route("/maintenance")
def maintenance():
    return render_template("maintenance_dashboard.html")


# ==========================
# LPC FORM
# ==========================

@app.route("/lpc")
def lpc():
    return render_template("lpc_form.html")


@app.route("/save_lpc", methods=["POST"])
def save_lpc():

    breakdown_date = request.form.get("breakdown_date")
    machine_name = request.form.get("machine_name")
    applicator_no = request.form.get("applicator_no")
    terminal_part_no = request.form.get("terminal_part_no")
    problem_type = request.form.get("problem_type")
    description = request.form.get("description")

    return f"""
    <h2>✅ LPC Breakdown Saved Successfully</h2>

    <b>Date :</b> {breakdown_date}<br><br>
    <b>Machine :</b> {machine_name}<br><br>
    <b>Applicator :</b> {applicator_no}<br><br>
    <b>Terminal :</b> {terminal_part_no}<br><br>
    <b>Problem :</b> {problem_type}<br><br>
    <b>Description :</b> {description}<br><br>

    <a href="/lpc">New LPC Entry</a>
    """

# ==========================
# ASSY FORM
# ==========================

@app.route("/assy")
def assy():
    return render_template("assy_form.html")


# ==========================
# MASTER DATA
# ==========================

@app.route("/machine_master")
def machine_master():
    return render_template("machine_master.html")


@app.route("/operator_master")
def operator_master():
    return render_template("operator_master.html")


@app.route("/technician_master")
def technician_master():
    return render_template("technician_master.html")


@app.route("/problem_master")
def problem_master():
    return render_template("problem_master.html")


@app.route("/user_master")
def user_master():
    return render_template("user_master.html")


@app.route("/applicator_master")
def applicator_master():
    return render_template("applicator_master.html")


@app.route("/terminal_master")
def terminal_master():
    return render_template("terminal_master.html")


# ==========================
# USER SAVE
# ==========================

@app.route("/save_user", methods=["POST"])
def save_user():

    employee_id = request.form.get("employee_id")
    employee_name = request.form.get("employee_name")
    username = request.form.get("username")
    password = request.form.get("password")
    department = request.form.get("department")
    role = request.form.get("role")
    status = request.form.get("status")

    return f"""
    <h2>✅ User Saved Successfully</h2>

    Employee ID : {employee_id}<br>
    Employee Name : {employee_name}<br>
    Username : {username}<br>
    Department : {department}<br>
    Role : {role}<br>
    Status : {status}<br><br>

    <a href="/user_master">Back To User Master</a>
    """


# ==========================
# INVENTORY
# ==========================

@app.route("/spare_master")
def spare_master():
    return render_template("spare_master.html")


@app.route("/spare_issue")
def spare_issue():
    return render_template("spare_issue.html")


@app.route("/spare_receive")
def spare_receive():
    return render_template("spare_receive.html")


# ==========================
# MAINTENANCE
# ==========================

@app.route("/maintenance_action")
def maintenance_action():
    return render_template("maintenance_action.html")


@app.route("/rca")
def rca():
    return render_template("rca_form.html")


# ==========================
# REPORTS
# ==========================

@app.route("/reports")
def reports():
    return render_template("reports.html")


# ==========================
# RUN APPLICATION
# ==========================

if __name__ == "__main__":
    app.run(debug=True)
