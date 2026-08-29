# Software Requirements Specification (SRS)

## Project Title

# AI SOC Assistant

**AI-Based Security Operations Center Assistant**



# 1. Introduction

## 1.1 Purpose

This Software Requirements Specification (SRS) document describes the functional and non-functional requirements of the AI SOC Assistant.

The purpose of this document is to define what the system should do, how users interact with the system, what technologies are required, and what constraints apply to the application.

The document can be used as a reference during development, testing, maintenance, and project evaluation.



## 1.2 Project Overview

AI SOC Assistant is a web-based cybersecurity application developed using Python and Flask.

The application allows an authorized user to upload security log files and analyze them for suspicious activities.

The system classifies detected events into different risk levels and displays the results through a Security Operations Center dashboard.

The application also provides alert investigation, security reports, AI-based recommendations, suspicious IP identification, and optional Windows Defender Firewall integration.



## 1.3 Intended Audience

This document is intended for:

- Project developers
- Project evaluators
- Cybersecurity students
- Faculty members
- Security analysts
- Future developers of the application



# 2. System Objectives

The main objectives of the system are:

1. Provide a simple SOC monitoring interface.
2. Analyze uploaded security logs.
3. Detect suspicious security activities.
4. Classify detected events according to risk.
5. Display security alerts in an organized manner.
6. Help users investigate individual alerts.
7. Provide security recommendations.
8. Generate a security summary.
9. Identify suspicious IP addresses.
10. Provide optional IP blocking through Windows Defender Firewall.



# 3. Scope of the System

## 3.1 In Scope

The following functionality is included in the current project:

- User authentication
- Dashboard
- Security log upload
- Log analysis
- Threat detection
- Risk classification
- Alert management
- Alert search
- Alert filtering
- Alert details
- Threat score
- Security reports
- AI Security Assistant
- Suspicious IP identification
- Firewall IP blocking
- Firewall IP unblocking
- Logout



## 3.2 Out of Scope

The following features are not part of the current implementation:

- Enterprise-level SIEM
- Continuous real-time network monitoring
- Large-scale distributed log processing
- Production-grade machine learning detection
- Cloud-based deployment
- Automated threat intelligence feeds
- Mobile application
- Enterprise user management

These features may be added in future versions.


# 4. User Requirements

## 4.1 User Authentication

The user must be able to:

- Open the login page.
- Enter a username.
- Enter a password.
- Log into the application using valid credentials.
- Receive an error message when invalid credentials are entered.
- Log out from the application.



## 4.2 Dashboard Requirements

After successful login, the user should be able to access the dashboard.

The dashboard should display:

- Total alerts
- Critical alerts
- High-risk alerts
- Medium-risk alerts
- Low-risk alerts
- Threat score
- Overall risk
- Recent security events

The dashboard should provide navigation to other application modules.



## 4.3 Log Upload Requirements

The user should be able to:

1. Open the Log Analysis page.
2. Select a security log file.
3. Upload the file.
4. Submit the file for analysis.
5. View the analysis result.

If no file is selected, the system should display an appropriate error message.



## 4.4 Log Analysis Requirements

The system shall process uploaded log files.

The analyzer should:

- Read the log file.
- Examine individual log entries.
- Identify supported suspicious patterns.
- Generate security events.
- Assign risk levels.
- Generate analysis statistics.



## 4.5 Risk Classification Requirements

The system shall classify detected events into:

CRITICAL
HIGH
MEDIUM
LOW

## Functional Requirements

## FR-01: Login

The system shall provide a login page.

The user shall provide:

Username
Password

The system shall validate the credentials.

## FR-02: Session Management

The system shall create a user session after successful login.

Protected pages shall only be accessible to authenticated users.

If an unauthenticated user attempts to access a protected page, the system shall redirect the user to the login page.

## FR-03: Logout

The system shall allow an authenticated user to log out.

After logout, the user's session shall be cleared.

## FR-04: Dashboard

The system shall provide a dashboard containing security statistics and recent events.

## FR-05: File Upload

The system shall allow users to upload security log files.

The uploaded files shall be stored in the configured upload directory.

## FR-06: Log Analysis

The system shall analyze uploaded log files using the log analyzer module.

## FR-07: Threat Detection

The system shall detect supported suspicious activities from the uploaded logs.

## Examples include:

Brute-force activity
Port scanning
Suspicious login activity
Malware-related activity

## FR-08: Alert Generation

The system shall generate alert records for detected security events.

An alert may contain:

Event
Risk
IP address
Description
Log information

## FR-09: Alert Display

The system shall display detected alerts in the Alerts section.

## FR-10: Alert Search

The system shall allow users to search alerts.

Search may be performed using:

Event
Risk
IP address
Description
Log information
FR-11: Alert Filtering

The system shall allow users to filter alerts by risk level.

## Available filters are:

ALL
CRITICAL
HIGH
MEDIUM
LOW

## FR-12: Alert Details

The system shall allow users to open an individual alert and view its details.

## FR-13: Threat Score

The system shall display a threat score between 0 and 100 based on the security analysis.

## FR-14: Reports

The system shall provide a Reports section containing a summary of the latest security analysis.

The report shall include:

Total alerts
Critical alerts
High alerts
Medium alerts
Low alerts
Threat score
Overall risk

## FR-15: AI Security Assistant

The system shall provide security recommendations based on detected events.

The recommendations may include actions such as:

Investigating suspicious IP addresses
Reviewing firewall rules
Enabling MFA
Resetting passwords
Running antivirus scans
Applying security updates

## FR-16: Suspicious IP Identification

The system shall display IP addresses associated with suspicious security events.

## FR-17: IP Blocking

The system shall provide an optional function to block a suspicious IP address using Windows Defender Firewall.

The firewall operation shall require appropriate Administrator privileges.

## FR-18: IP Unblocking

The system shall provide an optional function to remove the firewall rule created by the application.

## 6. Non-Functional Requirements

## 6.1 Performance

The application should process normal-sized security logs within a reasonable amount of time.

The interface should respond quickly to normal user actions.

## 6.2 Usability

The system should provide:

Simple navigation
Clear labels
Understandable security information
Consistent interface design
Easy-to-read alerts

## 6.3 Reliability

The system should handle common errors such as:

Missing files
Invalid login credentials
Invalid IP addresses
Missing analysis data
Invalid user input

The application should display meaningful error messages rather than unexpectedly terminating.

## 6.4 Security

The application should:

Restrict protected pages to authenticated users.
Validate IP addresses before firewall operations.
Require Administrator privileges for system-level firewall changes.
Avoid unnecessary modification of system security settings.

## 6.5 Maintainability

The application should use separate modules for different functions.

For example:

app.py
analyzer/
security/
templates/
static/
data/

This makes the application easier to maintain and extend.

## 6.6 Compatibility

The application is designed primarily for:

Windows operating system
Python 3.x
Flask
Modern web browsers

The firewall integration specifically depends on Windows Defender Firewall.

## 7. System Components

The major components of the application are:

## 7.1 Flask Application

app.py manages:

Routes
Sessions
Authentication
Dashboard
Alerts
Reports
AI Assistant
File uploads
Firewall operations

## 7.2 Log Analyzer

The analyzer module processes uploaded log files and generates security analysis results.

## 7.3 Firewall Manager

The firewall module manages:

IP validation
IP blocking
IP unblocking
Firewall rule checking

## 7.4 Templates

The HTML templates provide the user interface.

Examples include:

login.html
index.html
dashboard.html
upload.html
analysis.html
alerts.html
alert_details.html
reports.html
ai.html

## 7.5 Static Files

Static resources include:

CSS
JavaScript
Images

These files control the appearance and client-side behavior of the application.

## 7.6 Data Storage

Analysis information is stored in:

data/analysis_data.json

The JSON file stores analysis summaries and detected results.

## 8. Input Requirements

The main input to the system is a security log file.

The user provides:

Security Log File

The system then processes the file through the analyzer.

## 9. Output Requirements

The system should produce:

Analysis results
Security alerts
Risk classifications
Threat score
Overall risk
Security recommendations
Reports
Suspicious IP information

## 10. Error Handling Requirements

The system should handle common errors.

Missing File

If the user submits the upload form without selecting a file:

Please select a log file.
Invalid Login

If invalid credentials are entered:

Invalid username or password.
Invalid IP

If an invalid IP address is submitted:

Invalid IP address.
Analysis Failure

If the uploaded log cannot be analyzed:

Unable to analyze the uploaded file.


## 11. Security Requirements

## 11.1 Authentication

Protected pages must require a valid user session.

## 11.2 Input Validation

User inputs should be validated before processing.

IP addresses should be validated using Python's IP address validation functionality.

## 11.3 Firewall Protection

Firewall operations should only be performed after verifying the target IP address.

The application should not automatically block unknown or unverified addresses without user awareness.

## 11.4 Administrator Privileges

Windows Defender Firewall modifications require Administrator privileges.

Therefore, firewall actions should be treated as privileged operations.

## 12. Data Storage Requirements

The system uses JSON-based storage for analysis results.

Example structure:

data/
└── analysis_data.json

The stored data may contain:

filename
total_lines
total_alerts
critical
high
medium
low
threat_score
overall_risk
results

## 13. Navigation Requirements

The sidebar should provide access to the main application modules:

Home
Dashboard
Log Analysis
Alerts
Reports
AI Assistant

The user should be able to navigate directly between available modules after authentication.

## 14. User Workflow

The expected user workflow is:

Open Application
      ↓
Login
      ↓
Dashboard
      ↓
Upload Log
      ↓
Analyze Log
      ↓
View Results
      ↓
Open Alerts
      ↓
Filter/Search Alerts
      ↓
Open Alert Details
      ↓
Review AI Recommendations
      ↓
View Reports
      ↓
Review Suspicious IP
      ↓
Optional Firewall Action

## 15. Testing Requirements

The application should be tested for:

Login Testing
Valid username/password
Invalid username/password
Logout
Upload Testing
Valid log file
No file selected
Invalid file
Alert Testing
All alerts
Critical alerts
High alerts
Medium alerts
Low alerts
Search functionality
Dashboard Testing
Statistics display
Alert navigation
Recent events
Reports Testing
Report loading
Correct statistics
AI Assistant Testing
Recommendation generation
Different security events
Firewall Testing
Valid IP
Invalid IP
Block operation
Unblock operation
Administrator permission handling

## 16. System Constraints

The project has the following constraints:

Windows is required for the Windows Defender Firewall integration.
Firewall operations require Administrator privileges.
The application depends on supported log patterns.
JSON storage is intended for a small academic project rather than enterprise-scale data.
The current application is intended for educational and demonstration purposes.

## 17. Assumptions

The system assumes that:

The user has permission to analyze the uploaded logs.
The uploaded log file contains readable security information.
The application is running on a supported Windows system.
The user has appropriate privileges for firewall operations when required.
The required Python packages are installed.

## 18. Acceptance Criteria

The project shall be considered acceptable when:

A user can successfully log in.
Unauthorized users cannot access protected pages.
A security log can be uploaded.
The log can be analyzed.
Suspicious events can be detected.
Risk levels can be assigned.
Alerts can be displayed.
Alerts can be searched and filtered.
Individual alerts can be investigated.
Dashboard statistics are displayed.
Reports are generated.
AI security recommendations are displayed.
Suspicious IP addresses can be identified.
Firewall blocking functionality is available.
Firewall unblocking functionality is available.
The application handles common errors properly.

## 19. Future Requirements

Future versions may include:

Machine learning-based detection
Real-time log monitoring
Real-time network traffic analysis
Threat intelligence integration
SIEM integration
Database support
Role-based access control
Email notifications
Automated incident response
Cloud deployment
Mobile application
Advanced analytics

## 20. Conclusion

The SRS defines the requirements and expected behavior of the AI SOC Assistant.

The document establishes the functional requirements, non-functional requirements, system components, inputs, outputs, security requirements, testing requirements, and limitations of the application.

It provides a clear reference for understanding how the system should operate and what functionality the completed project should provide.