from flask import Flask, render_template, request, redirect, session
import os
import json

from analyzer.log_analyzer import analyze_log_file
from security.firewall_manager import (
    block_ip,
    unblock_ip,
    is_ip_blocked
)

from database import (
    init_db,
    create_user,
    verify_user,
    update_password,
    user_exists
)


app = Flask(__name__)

app.jinja_env.globals.update(
    is_ip_blocked=is_ip_blocked
)


# ==================================================
# FLASK CONFIGURATION
# ==================================================

app.secret_key = "ai_soc_secret_key"

init_db()


# ==================================================
# UPLOAD CONFIGURATION
# ==================================================

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ==================================================
# ANALYSIS DATA FILE
# ==================================================

DATA_FILE = os.path.join(
    app.root_path,
    "data",
    "analysis_data.json"
)


# ==================================================
# SAVE ANALYSIS
# ==================================================

def save_analysis(analysis, filename):

    try:

        if os.path.exists(DATA_FILE):

            with open(
                DATA_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

        else:

            data = {
                "analyses": []
            }


        record = {

            "filename": filename,

            "total_lines": analysis.get(
                "total_lines",
                0
            ),

            "total_alerts": analysis.get(
                "total_alerts",
                0
            ),

            "critical": analysis.get(
                "critical",
                0
            ),

            "high": analysis.get(
                "high",
                0
            ),

            "medium": analysis.get(
                "medium",
                0
            ),

            "low": analysis.get(
                "low",
                0
            ),

            "threat_score": analysis.get(
                "threat_score",
                0
            ),

            "overall_risk": analysis.get(
                "overall_risk",
                "LOW"
            ),

            "results": analysis.get(
                "results",
                []
            )
        }


        data.setdefault(
            "analyses",
            []
        ).append(record)


        os.makedirs(
            os.path.dirname(DATA_FILE),
            exist_ok=True
        )


        with open(
            DATA_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )


        return True


    except Exception as error:

        print(
            "Error saving analysis:",
            error
        )

        return False


# ==================================================
# HOME
# ==================================================

@app.route("/")
def home():

    if "username" not in session:

        return redirect("/login")


    return render_template(
        "index.html"
    )


# ==================================================
# LOGIN
# ==================================================

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        ).strip()

        password = request.form.get(
            "password",
            ""
        )


        if verify_user(
            username,
            password
        ):

            session["username"] = username

            # Start a fresh session
            session["fresh_session"] = True

            return redirect(
                "/dashboard"
            )


        return render_template(
            "login.html",
            error="Invalid username or password."
        )


    return render_template(
        "login.html"
    )


# ==================================================
# CREATE ACCOUNT
# ==================================================

@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    if user_exists():

        return render_template(
            "login.html",
            error="An account already exists. Please login."
        )


    if request.method == "POST":

        username = request.form.get(
            "username",
            ""
        ).strip()

        password = request.form.get(
            "password",
            ""
        )

        confirm_password = request.form.get(
            "confirm_password",
            ""
        )


        if not username:

            return render_template(
                "register.html",
                error="Username is required."
            )


        if not password:

            return render_template(
                "register.html",
                error="Password is required."
            )


        if password != confirm_password:

            return render_template(
                "register.html",
                error="Passwords do not match."
            )


        created = create_user(
            username,
            password
        )


        if created:

            return redirect(
                "/login"
            )


        return render_template(
            "register.html",
            error="Username already exists."
        )


    return render_template(
        "register.html"
    )


# ==================================================
# LOGOUT
# ==================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        "/login"
    )


# ==================================================
# CHANGE PASSWORD
# ==================================================

@app.route(
    "/change-password",
    methods=["GET", "POST"]
)
def change_password():

    if "username" not in session:

        return redirect("/login")


    username = session["username"]


    if request.method == "POST":

        current_password = request.form.get(
            "current_password",
            ""
        )

        new_password = request.form.get(
            "new_password",
            ""
        )

        confirm_password = request.form.get(
            "confirm_password",
            ""
        )


        if not verify_user(
            username,
            current_password
        ):

            return render_template(
                "change_password.html",
                error="Current password is incorrect."
            )


        if not new_password:

            return render_template(
                "change_password.html",
                error="New password is required."
            )


        if new_password != confirm_password:

            return render_template(
                "change_password.html",
                error="New passwords do not match."
            )


        if current_password == new_password:

            return render_template(
                "change_password.html",
                error="New password must be different from the current password."
            )


        updated = update_password(
            username,
            new_password
        )


        if updated:

            return render_template(
                "change_password.html",
                success="Password updated successfully."
            )


        return render_template(
            "change_password.html",
            error="Unable to update password."
        )


    return render_template(
        "change_password.html"
    )


# ==================================================
# DASHBOARD
# ==================================================

@app.route("/dashboard")
def dashboard():

    if "username" not in session:

        return redirect("/login")


    dashboard_data = {

        "total_alerts": 0,

        "critical": 0,

        "high": 0,

        "medium": 0,

        "low": 0,

        "threat_score": 0,

        "overall_risk": "LOW",

        "recent_events": [],

        "top_ips": []

    }


    # Show a clean dashboard after login
    if session.get(
        "fresh_session",
        False
    ):

        return render_template(
            "dashboard.html",
            data=dashboard_data
        )


    try:

        if os.path.exists(DATA_FILE):

            with open(
                DATA_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)


            analyses = data.get(
                "analyses",
                []
            )


            if analyses:

                latest = analyses[-1]


                dashboard_data["total_alerts"] = latest.get(
                    "total_alerts",
                    0
                )

                dashboard_data["critical"] = latest.get(
                    "critical",
                    0
                )

                dashboard_data["high"] = latest.get(
                    "high",
                    0
                )

                dashboard_data["medium"] = latest.get(
                    "medium",
                    0
                )

                dashboard_data["low"] = latest.get(
                    "low",
                    0
                )

                dashboard_data["threat_score"] = latest.get(
                    "threat_score",
                    0
                )

                dashboard_data["overall_risk"] = latest.get(
                    "overall_risk",
                    "LOW"
                )

                dashboard_data["recent_events"] = latest.get(
                    "results",
                    []
                )[-5:]


    except Exception as error:

        print(
            "Dashboard error:",
            error
        )


    return render_template(
        "dashboard.html",
        data=dashboard_data
    )


# ==================================================
# ALERTS
# ==================================================

@app.route("/alerts")
def alerts():

    if "username" not in session:

        return redirect("/login")


    search = request.args.get(
        "search",
        ""
    ).strip()


    selected_risk = request.args.get(
        "risk",
        "ALL"
    ).upper()


    alerts_list = []


    try:

        if os.path.exists(DATA_FILE):

            with open(
                DATA_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)


            analyses = data.get(
                "analyses",
                []
            )


            if analyses:

                latest = analyses[-1]


                all_results = latest.get(
                    "results",
                    []
                )


                prepared_alerts = []


                for index, alert in enumerate(
                    all_results
                ):

                    alert_copy = dict(
                        alert
                    )


                    alert_copy["original_id"] = index


                    ip = str(
                        alert_copy.get(
                            "ip",
                            ""
                        )
                    ).strip()


                    if ip:

                        try:

                            alert_copy["blocked"] = is_ip_blocked(
                                ip
                            )

                        except Exception:

                            alert_copy["blocked"] = False

                    else:

                        alert_copy["blocked"] = False


                    prepared_alerts.append(
                        alert_copy
                    )


                if selected_risk != "ALL":

                    prepared_alerts = [

                        alert

                        for alert in prepared_alerts

                        if str(
                            alert.get(
                                "risk",
                                ""
                            )
                        ).upper()
                        == selected_risk

                    ]


                if search:

                    search_text = search.lower()

                    filtered_alerts = []


                    for alert in prepared_alerts:

                        event = str(
                            alert.get(
                                "event",
                                ""
                            )
                        ).lower()


                        risk = str(
                            alert.get(
                                "risk",
                                ""
                            )
                        ).lower()


                        ip = str(
                            alert.get(
                                "ip",
                                ""
                            )
                        ).lower()


                        description = str(
                            alert.get(
                                "description",
                                ""
                            )
                        ).lower()


                        log_text = str(
                            alert.get(
                                "log",
                                ""
                            )
                        ).lower()


                        if (

                            search_text in event

                            or search_text in risk

                            or search_text in ip

                            or search_text in description

                            or search_text in log_text

                        ):

                            filtered_alerts.append(
                                alert
                            )


                    prepared_alerts = filtered_alerts


                alerts_list = prepared_alerts


    except Exception as error:

        print(
            "Alerts error:",
            error
        )


    return render_template(
        "alerts.html",
        alerts=alerts_list,
        selected_risk=selected_risk,
        search=search
    )


# ==================================================
# ALERT DETAILS
# ==================================================

@app.route(
    "/alert/<int:alert_id>"
)
def alert_details(alert_id):

    if "username" not in session:

        return redirect("/login")


    selected_alert = None


    try:

        if os.path.exists(DATA_FILE):

            with open(
                DATA_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)


            analyses = data.get(
                "analyses",
                []
            )


            if analyses:

                latest = analyses[-1]


                alerts_list = latest.get(
                    "results",
                    []
                )


                if (
                    0 <= alert_id
                    < len(alerts_list)
                ):

                    selected_alert = dict(
                        alerts_list[alert_id]
                    )


                    ip = str(
                        selected_alert.get(
                            "ip",
                            ""
                        )
                    ).strip()


                    if ip:

                        try:

                            selected_alert["blocked"] = is_ip_blocked(
                                ip
                            )

                        except Exception:

                            selected_alert["blocked"] = False


    except Exception as error:

        print(
            "Alert details error:",
            error
        )


    if selected_alert is None:

        return redirect(
            "/alerts"
        )


    return render_template(
        "alert_details.html",
        alert=selected_alert,
        alert_id=alert_id
    )


# ==================================================
# UPLOAD LOGS
# ==================================================

@app.route(
    "/upload",
    methods=["GET", "POST"]
)
def upload():

    if "username" not in session:

        return redirect("/login")


    if request.method == "POST":

        file = request.files.get(
            "logfile"
        )


        if (
            not file
            or file.filename == ""
        ):

            return render_template(
                "upload.html",
                error="Please select a log file."
            )


        os.makedirs(
            app.config["UPLOAD_FOLDER"],
            exist_ok=True
        )


        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )


        file.save(
            file_path
        )


        analysis = analyze_log_file(
            file_path
        )


        if not analysis.get(
            "success",
            False
        ):

            return render_template(
                "upload.html",
                error="Unable to analyze the uploaded file."
            )


        save_analysis(
            analysis,
            file.filename
        )


        # Analysis has now been performed
        session["fresh_session"] = False


        return render_template(
            "analysis.html",
            analysis=analysis,
            filename=file.filename
        )


    return render_template(
        "upload.html"
    )


# ==================================================
# SECURITY REPORTS
# ==================================================

@app.route("/reports")
def reports():

    if "username" not in session:

        return redirect("/login")


    report_data = {

        "total_alerts": 0,

        "critical": 0,

        "high": 0,

        "medium": 0,

        "low": 0,

        "threat_score": 0,

        "overall_risk": "LOW"

    }


    try:

        if os.path.exists(DATA_FILE):

            with open(
                DATA_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)


            analyses = data.get(
                "analyses",
                []
            )


            if analyses:

                latest = analyses[-1]


                for key in report_data:

                    if key in latest:

                        report_data[key] = latest[key]


    except Exception as error:

        print(
            "Reports error:",
            error
        )


    return render_template(
        "reports.html",
        data=report_data
    )


# ==================================================
# AI SECURITY ASSISTANT
# ==================================================

@app.route("/ai")
def ai_assistant():

    if "username" not in session:

        return redirect("/login")


    recommendations = []


    try:

        if os.path.exists(DATA_FILE):

            with open(
                DATA_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)


            analyses = data.get(
                "analyses",
                []
            )


            if analyses:

                latest = analyses[-1]


                alerts = latest.get(
                    "results",
                    []
                )


                for alert in alerts:

                    event = str(
                        alert.get(
                            "event",
                            ""
                        )
                    ).lower()


                    risk = alert.get(
                        "risk",
                        "LOW"
                    )


                    advice = []


                    if "brute" in event:

                        advice = [

                            "Block suspicious IP addresses.",

                            "Enable account lockout policy.",

                            "Enable Multi-Factor Authentication.",

                            "Review failed login attempts."

                        ]


                    elif "port" in event:

                        advice = [

                            "Investigate source IP.",

                            "Review firewall rules.",

                            "Close unnecessary ports.",

                            "Monitor scanning activity."

                        ]


                    elif "malware" in event:

                        advice = [

                            "Isolate infected system.",

                            "Run antivirus scan.",

                            "Check affected files.",

                            "Update security patches."

                        ]


                    elif "login" in event:

                        advice = [

                            "Reset affected passwords.",

                            "Enable MFA.",

                            "Check user accounts.",

                            "Monitor login activity."

                        ]


                    else:

                        advice = [

                            "Review logs carefully.",

                            "Investigate suspicious activity.",

                            "Monitor affected systems."

                        ]


                    recommendations.append({

                        "event": alert.get(
                            "event",
                            "Unknown Event"
                        ),

                        "risk": risk,

                        "ip": alert.get(
                            "ip",
                            "Unknown"
                        ),

                        "description": alert.get(
                            "description",
                            ""
                        ),

                        "advice": advice

                    })


    except Exception as error:

        print(
            "AI Assistant error:",
            error
        )


    return render_template(
        "ai.html",
        recommendations=recommendations
    )


# ==================================================
# BLOCK SUSPICIOUS IP
# ==================================================

@app.route(
    "/block-ip/<ip>"
)
def block_suspicious_ip(ip):

    if "username" not in session:

        return redirect("/login")


    try:

        result = block_ip(ip)


        return render_template(
            "firewall_result.html",

            success=result.get(
                "success",
                False
            ),

            message=result.get(
                "message",
                "Firewall operation completed."
            ),

            ip=ip
        )


    except Exception as error:

        print(
            "Block IP error:",
            error
        )


        return render_template(
            "firewall_result.html",

            success=False,

            message=f"Unable to block IP: {error}",

            ip=ip
        )


# ==================================================
# UNBLOCK SUSPICIOUS IP
# ==================================================

@app.route(
    "/unblock-ip/<ip>"
)
def unblock_suspicious_ip(ip):

    if "username" not in session:

        return redirect("/login")


    try:

        result = unblock_ip(ip)


        return render_template(
            "firewall_result.html",

            success=result.get(
                "success",
                False
            ),

            message=result.get(
                "message",
                "Firewall operation completed."
            ),

            ip=ip
        )


    except Exception as error:

        print(
            "Unblock IP error:",
            error
        )


        return render_template(
            "firewall_result.html",

            success=False,

            message=f"Unable to unblock IP: {error}",

            ip=ip
        )


# ==================================================
# START APPLICATION
# ==================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )