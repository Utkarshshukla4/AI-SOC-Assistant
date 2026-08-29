# AI SOC Assistant — System Architecture

## 1. Introduction

The AI SOC Assistant is a web-based cybersecurity application developed using Python and Flask.

The system is designed to help a security analyst analyze security logs, identify suspicious activities, classify security alerts, provide security recommendations, generate reports, and optionally interact with the Windows Defender Firewall for IP blocking.

The application follows a modular architecture so that each major function is handled by a separate component.

---

## 2. High-Level Architecture

The overall system works through the following flow:

```text
                    ┌──────────────────────┐
                    │        User          │
                    │   Security Analyst   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Web Interface     │
                    │   HTML / CSS / JS    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Flask App        │
                    │       app.py         │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
      ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
      │ Log Analyzer │  │ AI Assistant │  │   Reports    │
      │              │  │              │  │              │
      └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                    ┌──────────────────────┐
                    │   Analysis Data      │
                    │   JSON Storage       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Security / Firewall  │
                    │     Module           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Windows Defender     │
                    │      Firewall        │
                    └──────────────────────┘
```

---

## 3. Architectural Components

### 3.1 User Interface Layer

The User Interface is responsible for interaction between the security analyst and the application.

The interface is implemented using:

* HTML
* CSS
* Jinja2 templates
* Basic JavaScript where required

Main interface pages include:

* Login
* Home
* Dashboard
* Log Analysis
* Alerts
* Alert Details
* Reports
* AI Assistant
* Firewall Result

The sidebar provides navigation between the major sections.

---

## 4. Flask Application Layer

The main application controller is:

```text
app.py
```

Flask handles:

* User authentication
* Session management
* Page routing
* File uploads
* Log analysis requests
* Dashboard data
* Alert filtering
* Reports
* AI recommendations
* Firewall operations

Important routes include:

```text
/login
/logout
/
/dashboard
/upload
/alerts
/alert/<id>
/reports
/ai
/block-ip/<ip>
/unblock-ip/<ip>
```

The Flask application acts as the central controller connecting the user interface with the backend modules.

---

## 5. Log Analyzer Module

The log analyzer is located in:

```text
analyzer/
```

The main function used by the Flask application is:

```python
analyze_log_file()
```

The analyzer processes the uploaded security log and extracts useful information.

The general process is:

```text
Uploaded Log
     ↓
Read Log File
     ↓
Process Log Entries
     ↓
Identify Suspicious Events
     ↓
Classify Risk
     ↓
Calculate Threat Score
     ↓
Generate Analysis Results
```

The system can identify security-related activities such as:

* Brute-force attempts
* Port scanning
* Suspicious login activity
* Malware-related events
* Other suspicious events supported by the analyzer

---

## 6. Risk Classification

Detected events are categorized according to their risk level.

The main categories are:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

The classification is used by the Dashboard and Alerts sections.

For example:

```text
Security Event
      ↓
Risk Evaluation
      ↓
┌──────────┬────────┬────────┬──────┐
│ CRITICAL │  HIGH  │ MEDIUM │ LOW  │
└──────────┴────────┴────────┴──────┘
```

The risk level helps the analyst prioritize important security events.

---

## 7. Data Storage Layer

The project stores analysis information in:

```text
data/analysis_data.json
```

The JSON file stores information such as:

* Uploaded filename
* Total log lines
* Total alerts
* Critical alerts
* High-risk alerts
* Medium-risk alerts
* Low-risk alerts
* Threat score
* Overall risk
* Individual analysis results

A simplified structure is:

```json
{
    "analyses": [
        {
            "filename": "security.log",
            "total_alerts": 5,
            "critical": 1,
            "high": 2,
            "medium": 1,
            "low": 1,
            "threat_score": 72,
            "overall_risk": "HIGH",
            "results": []
        }
    ]
}
```

The application reads this information when displaying the Dashboard, Alerts and Reports.

---

## 8. Dashboard Module

The Dashboard provides a quick overview of the latest security analysis.

It displays:

* Total alerts
* Critical alerts
* High-risk alerts
* Medium-risk alerts
* Low-risk alerts
* Threat score
* Overall risk
* Recent security events

The Dashboard gets its information from:

```text
analysis_data.json
```

The Flask route processes the data and sends it to:

```text
dashboard.html
```

---

## 9. Alerts Module

The Alerts module provides detailed security event investigation.

The analyst can:

* View all alerts
* Filter alerts by risk
* Search for specific events
* Search by IP address
* Search descriptions
* Open individual alert details

The general flow is:

```text
Stored Analysis
      ↓
Load Alerts
      ↓
Search / Filter
      ↓
Display Results
      ↓
Open Alert Details
```

This allows the analyst to investigate suspicious activity more efficiently.

---

## 10. Reports Module

The Reports module provides a summary of the latest security analysis.

It displays information such as:

* Total alerts
* Critical alerts
* High alerts
* Medium alerts
* Low alerts
* Threat score
* Overall risk

The Reports module uses the latest analysis stored in:

```text
data/analysis_data.json
```

---

## 11. AI Security Assistant

The AI Assistant provides security recommendations based on detected events.

The current implementation uses event-based security recommendations.

For example:

### Brute Force

Possible recommendations:

* Block suspicious IP addresses
* Enable account lockout
* Enable Multi-Factor Authentication
* Review failed login attempts

### Port Scan

Possible recommendations:

* Investigate the source IP
* Review firewall rules
* Close unnecessary ports
* Monitor scanning activity

### Malware

Possible recommendations:

* Isolate the affected system
* Run an antivirus scan
* Check affected files
* Apply security updates

### Login Attack

Possible recommendations:

* Reset affected passwords
* Enable MFA
* Check user accounts
* Monitor login activity

The AI Assistant receives detected events and generates relevant security advice.

---

## 12. Firewall Security Module

The firewall functionality is located in:

```text
security/firewall_manager.py
```

The module provides functions for:

```python
block_ip()
unblock_ip()
is_ip_blocked()
```

The module communicates with the Windows Defender Firewall using the Windows:

```text
netsh advfirewall
```

command.

The flow is:

```text
Suspicious IP
      ↓
Validate IP
      ↓
Firewall Manager
      ↓
Windows Defender Firewall
      ↓
Create Firewall Rule
      ↓
IP Blocked
```

The application creates a rule with a name similar to:

```text
AI_SOC_Block_192_168_1_10
```

The firewall functionality is a system-level operation and may require Administrator privileges on Windows.

---

## 13. IP Validation

Before performing firewall operations, the application validates the IP address.

Python's:

```python
ipaddress
```

module is used for validation.

The process is:

```text
IP Address
     ↓
Validate IP
     ↓
Valid?
  ↙     ↘
Yes      No
 ↓        ↓
Firewall  Error
Operation Message
```

This helps prevent invalid IP addresses from being passed to the firewall module.

---

## 14. Authentication and Session Management

The application uses Flask sessions to control access to protected pages.

A user must log in before accessing the main application.

The authentication flow is:

```text
User
 ↓
Login Page
 ↓
Username + Password
 ↓
Credential Verification
 ↓
Valid?
 ↙     ↘
Yes      No
 ↓        ↓
Session   Error
Created   Message
 ↓
Dashboard
```

Protected routes check whether:

```python
"username" in session
```

If the user is not authenticated, the application redirects the user to the login page.

---

## 15. File Upload Architecture

The Log Analysis module allows the user to upload a security log.

The uploaded file is stored in:

```text
uploads/
```

The process is:

```text
User Selects Log
       ↓
Upload Form
       ↓
Flask /upload Route
       ↓
Save File
       ↓
Log Analyzer
       ↓
Generate Analysis
       ↓
Save Results
       ↓
Display Analysis
```

---

## 16. Project Directory Architecture

The main project structure is:

```text
AI_SOC_Assistant/
│
├── app.py
│
├── analyzer/
│   └── log_analyzer.py
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
│   └── firewall_result.html
│
├── templates/components/
│   └── sidebar.html
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
├── uploads/
│
├── PRD.md
├── SRS.md
├── Architecture.md
├── UI_UX.md
├── Documentation_Plan.md
│
└── requirements.txt
```

The `js` and `images` folders are part of the frontend structure and can contain JavaScript files and UI images used by the application.

---

## 17. End-to-End System Flow

The complete application workflow is:

```text
                    USER
                      │
                      ▼
                   LOGIN
                      │
                      ▼
                 DASHBOARD
                      │
                      ▼
               UPLOAD SECURITY LOG
                      │
                      ▼
                FLASK APPLICATION
                      │
                      ▼
                 LOG ANALYZER
                      │
                      ▼
              THREAT DETECTION
                      │
                      ▼
               RISK CLASSIFICATION
                      │
              ┌───────┼────────┐
              ▼       ▼        ▼
           ALERTS   REPORTS    AI
              │       │        │
              └───────┼────────┘
                      │
                      ▼
              SUSPICIOUS IP
                      │
                      ▼
             FIREWALL MODULE
                      │
                      ▼
          WINDOWS DEFENDER FIREWALL
```

---

## 18. Security Considerations

The application includes several security-related considerations:

* Authentication is used to protect application pages.
* Uploaded files are processed by the log analyzer.
* IP addresses are validated before firewall operations.
* Firewall rules are given application-specific names.
* Invalid IP addresses are rejected.
* Firewall operations are separated into a dedicated security module.
* Sensitive system-level operations are not performed automatically without the required privileges.

---

## 19. Limitations

The current architecture has some limitations:

1. The application uses JSON storage instead of a production database.
2. The AI Assistant currently uses rule/event-based recommendations rather than a large language model.
3. Log detection depends on the patterns supported by the analyzer.
4. Firewall operations depend on Windows Defender Firewall and appropriate system privileges.
5. The application is designed primarily as an academic cybersecurity project and is not intended to replace a production SIEM/SOC platform.

---

## 20. Future Enhancements

Future versions could include:

* Machine learning-based threat detection
* Real-time log monitoring
* Database integration
* Real-time dashboards
* Email or SMS security notifications
* Integration with SIEM platforms
* Threat intelligence APIs
* More advanced AI-based incident analysis
* Role-based access control
* Automated incident response
* Detailed PDF report generation
* Cross-platform firewall support

---

## 21. Conclusion

The AI SOC Assistant follows a modular web application architecture consisting of the user interface, Flask application layer, log analyzer, data storage, AI recommendation module and firewall security module.

The architecture allows security events to move from log collection and analysis to risk classification, alert investigation, reporting and security recommendations.

The modular design also makes it easier to extend the project in the future with machine learning, real-time monitoring, databases, threat intelligence and advanced incident response capabilities.
