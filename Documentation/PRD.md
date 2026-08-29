# Product Requirements Document (PRD)

## Project Title

# AI SOC Assistant

**AI-Based Security Operations Center Assistant**


## 1. Introduction

AI SOC Assistant is a cybersecurity web application designed to help security analysts analyze security logs, identify suspicious activities, classify security alerts according to their risk level, and provide security recommendations.

The system provides a centralized dashboard where users can upload security log files and view the results of the analysis.

The application also includes an optional firewall management feature that can be used to block or unblock suspicious IP addresses through Windows Defender Firewall with Administrator permission.



## 2. Problem Statement

Security systems generate a large amount of log data. Manually checking these logs can be time-consuming and difficult, especially when there are many security events.

A security analyst needs to quickly identify:

- Suspicious activities
- High-risk events
- Critical security alerts
- Suspicious IP addresses
- Possible attack types
- Recommended security actions

Therefore, this project provides a simple Security Operations Center (SOC) interface that helps analyze logs and present important security information in an easy-to-understand format.



## 3. Project Objective

The main objective of AI SOC Assistant is to develop a web-based security monitoring system that can:

1. Accept security log files from users.
2. Analyze uploaded log data.
3. Detect suspicious security events.
4. Classify events according to risk level.
5. Display security alerts on a dashboard.
6. Allow users to search and filter alerts.
7. Display detailed information about individual alerts.
8. Provide AI-based security recommendations.
9. Generate security reports.
10. Identify suspicious IP addresses.
11. Provide an optional IP blocking capability using Windows Defender Firewall.



## 4. Target Users

The system is mainly designed for:

- Cybersecurity students
- SOC Analyst beginners
- Security analysts
- Network security students
- Cybersecurity training environments
- Small security monitoring environments



## 5. Product Scope

The project focuses on log-based security monitoring and analysis.

The system provides:

### Core Features

- User login
- Security dashboard
- Security log upload
- Log analysis
- Threat detection
- Risk classification
- Alert management
- Alert search
- Alert filtering
- Individual alert details
- Security reports
- AI security recommendations
- Suspicious IP identification
- Optional firewall IP blocking



## 6. Major Features

### 6.1 User Authentication

The application provides a login system that allows authorized users to access the SOC dashboard.

For the project demonstration, the system uses demo credentials.



### 6.2 Security Dashboard

The dashboard provides an overview of the latest security analysis.

It displays:

- Total alerts
- Critical alerts
- High-risk alerts
- Medium-risk alerts
- Low-risk alerts
- Threat score
- Overall risk
- Recent security events

The dashboard also provides quick navigation to important security functions.



### 6.3 Security Log Upload

Users can upload supported security log files through the Log Analysis section.

The uploaded file is stored in the project upload directory and passed to the log analyzer.

The analyzer processes the file and generates security analysis results.



### 6.4 Log Analysis

The log analyzer examines uploaded security logs and identifies security-related events.

The analysis may identify events such as:

- Brute-force activity
- Port scanning
- Suspicious login activity
- Malware-related activity
- Other suspicious events



### 6.5 Risk Classification

Detected events are categorized into different risk levels:

- CRITICAL
- HIGH
- MEDIUM
- LOW

This helps the analyst prioritize important security events.



### 6.6 Alert Management

The Alerts section displays detected security events in a structured table.

Each alert can contain information such as:

- Event
- Risk level
- Source IP
- Description
- Log information

Users can investigate individual alerts by opening their details.



### 6.7 Alert Search and Filtering

The system allows users to search alerts using relevant information.

Search can be performed using:

- Event name
- Risk level
- IP address
- Description
- Log information

Users can also filter alerts by:

- All
- Critical
- High
- Medium
- Low



### 6.8 Alert Details

Users can select an individual alert to view more information.

The alert details page provides additional information about the selected security event.

This allows analysts to investigate suspicious activity more easily.



### 6.9 Threat Score

The dashboard provides a threat score from 0 to 100.

The score provides a simple indication of the overall security condition based on detected events.

A higher score indicates a greater level of detected security risk.



### 6.10 Security Reports

The Reports section provides a summarized view of the latest security analysis.

It can display:

- Total alerts
- Critical alerts
- High-risk alerts
- Medium-risk alerts
- Low-risk alerts
- Threat score
- Overall risk

This provides a quick security overview for the analyst.



### 6.11 AI Security Assistant

The AI Security Assistant provides security recommendations based on detected events.

For example:

#### Brute Force Activity

The system may recommend:

- Blocking suspicious IP addresses
- Enabling account lockout
- Enabling Multi-Factor Authentication
- Reviewing failed login attempts

#### Port Scanning

The system may recommend:

- Investigating the source IP
- Reviewing firewall rules
- Closing unnecessary ports
- Monitoring scanning activity

#### Malware Activity

The system may recommend:

- Isolating the affected system
- Running an antivirus scan
- Checking affected files
- Applying security updates

#### Login Attacks

The system may recommend:

- Resetting affected passwords
- Enabling MFA
- Checking user accounts
- Monitoring login activity



## 7. Suspicious IP Detection

The system identifies IP addresses associated with detected security events.

These IP addresses can be reviewed by the security analyst.

The IP information can help an analyst determine the possible source of suspicious activity.



## 8. Firewall Blocking Feature

The project includes an optional firewall management feature.

The system can provide a mechanism to block a suspicious IP address using Windows Defender Firewall.

The firewall module uses Windows firewall commands to create a blocking rule.

The system also provides an unblock function to remove the rule created by the application.

### Security Consideration

Firewall modification is a real system-level operation and requires Administrator privileges.

Therefore, the feature should be used carefully and only after verifying that the IP address is actually suspicious.

For the academic demonstration, the firewall functionality can be demonstrated through the source code and UI without making unnecessary changes to the host laptop.



## 9. User Interface

The application provides a centralized SOC-style interface.

The main navigation includes:

- Home
- Dashboard
- Log Analysis
- Alerts
- Reports
- AI Assistant

The interface uses a consistent design across the application.



## 10. Technology Requirements

### Programming Language

- Python

### Web Framework

- Flask

### Frontend

- HTML
- CSS

### Data Storage

- JSON

### Security / System Integration

- Windows Defender Firewall
- Windows `netsh` firewall commands

### Development Environment

- Visual Studio Code
- Windows

---

## 11. Functional Requirements

The system shall:

### FR-01
Allow a user to log into the application.

### FR-02
Allow authenticated users to access the SOC dashboard.

### FR-03
Allow users to upload security log files.

### FR-04
Analyze uploaded security logs.

### FR-05
Detect suspicious security events.

### FR-06
Classify detected events by risk level.

### FR-07
Display security statistics on the dashboard.

### FR-08
Display detected alerts.

### FR-09
Allow users to search alerts.

### FR-10
Allow users to filter alerts by risk level.

### FR-11
Allow users to view individual alert details.

### FR-12
Provide security reports.

### FR-13
Provide security recommendations through the AI Assistant.

### FR-14
Identify suspicious IP addresses.

### FR-15
Provide an optional firewall blocking function.

### FR-16
Provide an optional firewall unblocking function.

### FR-17
Allow users to log out of the application.

---

## 12. Non-Functional Requirements

### Performance

The application should process normal-sized security log files within a reasonable amount of time.

### Usability

The interface should be simple enough for a beginner security analyst to understand.

### Reliability

The application should handle invalid files and unexpected input without crashing.

### Security

Authentication should prevent unauthorized access to protected pages.

### Maintainability

The project should use a modular structure so that components can be modified independently.

### Compatibility

The application is designed primarily for Windows because the firewall integration uses Windows Defender Firewall.

---

## 13. Data Requirements

The application stores analysis information in a JSON data file.

The stored information may include:

- Filename
- Total lines
- Total alerts
- Critical alerts
- High-risk alerts
- Medium-risk alerts
- Low-risk alerts
- Threat score
- Overall risk
- Detected security events



## 14. Project Workflow

The overall workflow of the application is:

User Login
     ↓
SOC Dashboard
     ↓
Upload Security Log
     ↓
Log Analyzer
     ↓
Threat Detection
     ↓
Risk Classification
     ↓
Security Alerts
     ↓
Alert Investigation
     ↓
AI Security Recommendations
     ↓
Security Reports
     ↓
Suspicious IP Identification
     ↓
Optional Firewall Action

## Expected Benefits

The project provides the following benefits:

Reduces manual log analysis effort
Provides centralized security monitoring
Makes security alerts easier to understand
Helps prioritize high-risk events
Provides useful security recommendations
Helps identify suspicious IP addresses
Demonstrates basic SOC workflow
Demonstrates integration between cybersecurity software and Windows Firewall

## 16. Limitations

The current project has some limitations:

It is primarily designed for educational and demonstration purposes.
The log analysis depends on the supported log patterns.
It does not replace a professional SIEM platform.
The AI Assistant provides rule-based recommendations rather than a full production AI model.
Firewall blocking requires Administrator privileges.
The application currently focuses mainly on Windows environments.
Large-scale enterprise log processing is outside the current project scope.

## 17. Future Scope

Future versions of the project can include:

Machine learning-based threat detection
Real-time log monitoring
Real-time network monitoring
Integration with SIEM platforms
Email notifications
SMS or mobile notifications
Automatic incident response
IP reputation checking
Threat intelligence integration
Geo-location of suspicious IPs
Advanced firewall automation
Database integration
Role-based access control
Cloud deployment
Advanced analytics and visualization
Real-time SOC monitoring

## 18. Success Criteria

The project will be considered successful if it can:

Successfully authenticate a user.
Accept a security log file.
Analyze the uploaded log.
Detect security events.
Assign risk levels.
Display results on the dashboard.
Allow alert searching and filtering.
Display individual alert details.
Generate a security report.
Provide security recommendations.
Identify suspicious IP addresses.
Provide a controlled firewall blocking capability.

## 19. Project Outcome

The final outcome of the project is a functional web-based AI SOC Assistant that demonstrates the basic workflow of a Security Operations Center.

The application combines:

Log analysis
Threat detection
Risk classification
Alert management
Security reporting
AI-assisted recommendations
Suspicious IP identification
Optional firewall integration

The project is intended to demonstrate practical cybersecurity concepts in a simple and user-friendly application.

## 20. Conclusion

AI SOC Assistant provides a centralized platform for analyzing security logs and understanding detected security events.

The project demonstrates how Python, Flask, cybersecurity concepts, log analysis, and Windows security features can be combined to create a basic SOC monitoring solution.

The system is designed as an academic cybersecurity project and can be further extended with machine learning, real-time monitoring, threat intelligence, SIEM integration, and automated incident response.