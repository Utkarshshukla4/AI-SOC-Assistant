# AI SOC Assistant

## About the Project

AI SOC Assistant is a web-based cybersecurity project developed using Python and Flask.

The project helps a security analyst upload and analyze log files, identify suspicious security events, view alerts, check security reports and receive security recommendations.

It also includes a firewall module that can be used to block or unblock suspicious IP addresses through Windows Defender Firewall.

---

## Main Features

* User login
* Security dashboard
* Log file upload and analysis
* Security alert detection
* Alert search and risk filtering
* Alert details
* Security reports
* Rule-based security recommendations
* Suspicious IP blocking and unblocking
* Windows Defender Firewall integration

---

## Technologies Used

* **Python 3.12.1** – Main programming language
* **Flask 3.0.3** – Web application backend
* **Werkzeug 3.0.4** – Flask's web server and utility components
* **HTML** – Page structure
* **CSS** – Page styling and layout
* **JSON** – Local storage of analysis results
* **Windows Defender Firewall** – IP blocking and unblocking
* **netsh** – Command used to manage Windows Firewall rules


## Project Structure

```text
AI_SOC_Assistant/
│
├── app.py
├── README.md
├── PRD.md
├── SRS.md
├── Architecture.md
├── UI_UX.md
├── Documentation_Plan.md
├── Viva_Questions.md
│
├── analyzer/
│   ├── log_analyzer.py
│   └── test_log_analyzer.py
│
├── security/
│   └── firewall_manager.py
│
├── templates/
│   ├── login.html
│   ├── index.html
│   ├── dashboard.html
│   ├── upload.html
│   ├── analysis.html
│   ├── alerts.html
│   ├── alert_details.html
│   ├── reports.html
│   ├── ai.html
│   ├── firewall_result.html
│   └── components/
│       └── sidebar.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   └── images/
│
├── data/
│   └── analysis_data.json
│
└── uploads/
```

---

## How the Project Works

The basic workflow is:

```text
Login
  ↓
Dashboard
  ↓
Upload Log File
  ↓
Log Analyzer
  ↓
Security Events
  ↓
Alerts
  ↓
Reports / AI Recommendations
```

For suspicious IP management:

```text
Suspicious IP
      ↓
Firewall Manager
      ↓
Windows Defender Firewall
      ↓
Block / Unblock IP
```

---

## Main Project Files

### `app.py`

The main Flask application. It handles login, page navigation, log uploads, alerts, reports, AI recommendations and firewall actions.

### `analyzer/log_analyzer.py`

Analyzes uploaded log files and identifies suspicious events and their risk levels.

### `analyzer/test_log_analyzer.py`

Used to test the log analysis functionality.

### `security/firewall_manager.py`

Handles IP validation and firewall operations such as blocking and unblocking IP addresses.

### `templates/`

Contains the HTML pages used by the application.

### `static/css/style.css`

Contains the common styling and visual design of the application.

### `data/analysis_data.json`

Stores the results of the latest log analyses and detected security events.

### `uploads/`

Stores log files uploaded for analysis.

---

## Running the Project

### 1. Open the project

Open the `AI_SOC_Assistant` folder in VS Code.

### 2. Install required packages

If Flask is not installed, run:

```text
pip install Flask==3.0.3 Werkzeug==3.0.4
```

### 3. Start the application

Run:

```text
python app.py
```

### 4. Open in the browser

Open the local Flask address shown in the terminal, normally:

```text
http://127.0.0.1:5000
```

---


## Sample Log Testing

Sample and test log files can be uploaded through the Log Analysis section.

The analyzer checks the contents of the log and detects security-related events. Different test log files can produce different results depending on the events and IP addresses contained in them.

The results can then be checked through:

* Dashboard
* Alerts
* Reports
* AI Assistant

---

## AI Assistant

The AI Assistant currently uses rule-based security recommendations.

It checks the detected event type and provides relevant security advice.

For example, for a brute-force event it may recommend:

* Blocking the suspicious IP example : 192.0.2.10
* Enabling MFA
* Reviewing failed login attempts
* Checking account security

---

## Firewall Feature

The firewall module can block or unblock suspicious IP addresses using Windows Defender Firewall.

The application uses the Windows `netsh` command to create and remove firewall rules.

Administrator privileges may be required when performing firewall operations.

For testing and presentation, controlled test IP addresses should be used instead of important real system or network addresses.

---

## Data Storage

The project stores analysis results locally in:

```text
data/analysis_data.json
```

Uploaded log files are stored in:

```text
uploads/
```

---

## Limitations

* The AI Assistant currently uses rule-based recommendations rather than a trained machine-learning model.
* Firewall operations may require administrator privileges.
* The project is designed as a cybersecurity academic project and demonstration tool.

---

## Project Purpose

The main purpose of this project is to provide a simple SOC-style interface where a security analyst can analyze logs, monitor alerts, review security reports, receive security recommendations and perform basic IP response actions.


## Author
Utkarsh Shukla