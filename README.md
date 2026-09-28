
# AI SOC Assistant

## About the Project

AI SOC Assistant is a web-based cybersecurity project developed using **Python and Flask**.

The project provides a simple Security Operations Center (SOC) interface where a security analyst can:

* Create an account and log in securely
* Upload and analyze security log files
* Detect suspicious security events
* View and filter security alerts
* Check detailed alert information
* Generate security reports
* Get rule-based security recommendations
* Block or unblock suspicious IP addresses
* Manage account passwords

The project also integrates with **Windows Defender Firewall** for basic IP blocking and unblocking.

---

## Main Features

* User registration and login
* Password hashing using Werkzeug
* Password strength validation during registration
* Change password functionality
* Session-based authentication
* Security dashboard
* Log file upload and analysis
* Security event detection
* Alert search and risk filtering
* Alert details
* Security reports
* Rule-based AI security recommendations
* Suspicious IP blocking and unblocking
* Windows Defender Firewall integration
* Fresh dashboard after login
* Local SQLite database for user accounts
* JSON-based storage for analysis results

---

## Technologies Used

* **Python 3.12.1** – Main programming language
* **Flask 3.0.3** – Web application framework
* **Werkzeug 3.0.4** – Password hashing and Flask utilities
* **SQLite** – Local database for user accounts
* **HTML** – Web page structure
* **CSS** – User interface styling
* **Jinja2** – Dynamic HTML templates
* **JSON** – Storage of log analysis results
* **Windows Defender Firewall** – IP blocking and unblocking
* **netsh** – Windows command used for firewall management

---

## Project Structure

```text
AI-SOC-Assistant/
│
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── analyzer/
│   ├── log_analyzer.py
│   └── test_analyzer.py
│
├── security/
│   └── firewall_manager.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── change_password.html
│   ├── index.html
│   ├── dashboard.html
│   ├── upload.html
│   ├── analysis.html
│   ├── alerts.html
│   ├── alert_details.html
│   ├── reports.html
│   ├── ai.html
│   ├── firewall_result.html
│   │
│   └── components/
│       └── sidebar.html
│
├── static/
│   └── css/
│       └── style.css
│
├── Documentation/
│   ├── Architecture.md
│   ├── Documentation_Plan.md
│   ├── PRD.md
│   ├── SRS.md
│   └── UI_UX.md
│
├── data/
│   ├── users.db
│   └── analysis_data.json
│
└── uploads/
```

> `users.db` and `analysis_data.json` are local files and are excluded from GitHub using `.gitignore`.

---
## Project Architecture

<img width="1536" height="1024" alt="architecture" src="https://github.com/user-attachments/assets/aaaffbf1-84c5-4d79-aeb9-8c78b616c84b" />

## How the Project Works

The basic workflow is:

```text
Create Account
      ↓
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

## Authentication System

The project includes a local user authentication system.

### Create Account

A new user can create an account from the registration page.

The registration system checks:

* Username
* Password
* Confirm password
* Password strength
* Required fields
* Password confirmation
* Duplicate username

Passwords are stored as **hashed passwords**, not plain text.

### Login

Users log in using the credentials created during registration.

The application verifies the username and password using the SQLite database.

### Change Password

Logged-in users can change their password from:

```text
Change Password
```

The system verifies:

* Current password
* New password
* Confirm new password
* New password is different from the old password

### Logout

The logout option clears the current Flask session and returns the user to the login page.

---

## Main Project Files

### `app.py`

The main Flask application.

It handles:

* Login
* Registration
* Logout
* Change password
* Dashboard
* Log uploads
* Alerts
* Alert details
* Reports
* AI Assistant
* Firewall actions

### `database.py`

Handles the SQLite user database.

It provides functions for:

* Creating the database
* Creating users
* Checking users
* Verifying login credentials
* Updating passwords

Passwords are protected using Werkzeug password hashing.

### `analyzer/log_analyzer.py`

Analyzes uploaded log files and identifies suspicious security events and their risk levels.

### `analyzer/test_analyzer.py`

Contains tests for the log analyzer functionality.

### `security/firewall_manager.py`

Handles firewall-related operations such as:

* IP validation
* Blocking IP addresses
* Unblocking IP addresses
* Checking whether an IP is blocked

### `templates/`

Contains the HTML pages used by the Flask application.

### `templates/components/sidebar.html`

Contains the common sidebar navigation, including:

* Home
* Dashboard
* Log Analysis
* Alerts
* Reports
* AI Assistant
* Change Password
* Logout

### `static/css/style.css`

Contains the common styling and visual design of the application.

### `data/users.db`

SQLite database containing registered user account information.

Passwords are stored in hashed form.

### `data/analysis_data.json`

Stores the results of log analysis.

### `uploads/`

Stores log files uploaded by the user for analysis.

---

## Running the Project

### 1. Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/Utkarshshukla4/AI-SOC-Assistant.git
```

Then open the project folder in VS Code.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Start the Application

```bash
python app.py
```

### 5. Open the Application

Open:

```text
http://127.0.0.1:5000
```

The application will open on the login page.

---

## First-Time Setup

When someone downloads and runs the project for the first time, they can create their own account using:

```text
Create Account
```

After creating an account:

```text
Create Account
      ↓
Login
      ↓
Dashboard
```

The project does **not require a shared demo username and password**.

This allows each person running their own local copy of the project to create their own account.

---

## Sample Log Testing

A security log file can be uploaded through:

```text
Dashboard → Log Analysis
```

The analyzer processes the uploaded file and identifies security-related events.

The results can then be viewed through:

* Dashboard
* Alerts
* Alert Details
* Reports
* AI Assistant

Different log files can produce different results depending on their contents.

---

## Dashboard

The dashboard provides an overview of the latest analysis.

It displays:

* Total alerts
* Critical alerts
* High-risk alerts
* Medium-risk alerts
* Low-risk alerts
* Threat score
* Overall risk
* Recent security events

After a new login, the dashboard starts with a clean state. Once a new log is uploaded and analyzed, the new analysis becomes available throughout the application.

---

## Alerts

The Alerts section allows the analyst to review detected security events.

Alerts can be:

* Viewed
* Searched
* Filtered by risk level
* Opened for detailed information

Available risk levels include:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

---

## AI Assistant

The AI Assistant currently uses **rule-based security recommendations**.

It checks detected event types and provides relevant security advice.

For example, a brute-force event may result in recommendations such as:

* Block the suspicious IP
* Enable account lockout
* Enable MFA
* Review failed login attempts

The current implementation is rule-based and does not use an external AI API or trained machine-learning model.

---

## Firewall Feature

The firewall module can block or unblock suspicious IP addresses using **Windows Defender Firewall**.

The application uses the Windows `netsh` command to manage firewall rules.

Firewall operations may require **Administrator privileges**.

For testing and demonstration, use controlled test IP addresses rather than important real system or network addresses.

---

## Data Storage

The project uses two main types of local storage.

### User Database

```text
data/users.db
```

This SQLite database stores registered users and their hashed passwords.

### Analysis Data

```text
data/analysis_data.json
```

This file stores the results of log analysis.

### Uploaded Logs

```text
uploads/
```

Uploaded log files are stored locally for analysis.

These local data files are excluded from GitHub through `.gitignore`.

---

## Security Considerations

The project includes several basic security practices:

* Password hashing
* Session-based authentication
* Login protection for application pages
* Password confirmation
* Password strength validation
* Input validation
* SQLite parameterized queries
* Local firewall integration

However, this project is primarily designed as an academic and demonstration application rather than a production SOC platform.

---

## Limitations

* The AI Assistant currently uses rule-based recommendations.
* The log analyzer supports the log formats implemented in the project.
* Firewall operations may require administrator privileges.
* User accounts are stored locally in SQLite.
* Analysis results are stored locally in JSON.
* The project is designed primarily for Windows because of its Windows Defender Firewall integration.
* The application is intended for academic learning, demonstration and portfolio purposes.

---

## Documentation

Additional project documentation is available in the `Documentation` folder:

```text
Documentation/
├── Architecture.md
├── Documentation_Plan.md
├── PRD.md
├── SRS.md
└── UI_UX.md
```

These documents describe the project's requirements, architecture, planning and interface design.

---

## Project Purpose

The main purpose of AI SOC Assistant is to demonstrate how a simple SOC-style security application can combine:

* Web development
* Log analysis
* Security monitoring
* User authentication
* Alert management
* Security recommendations
* Firewall response

The project was developed as a cybersecurity academic and portfolio project.

---

## Author

**Utkarsh Shukla**
