# AI SOC Assistant — UI/UX Design Document

## 1. Introduction

The AI SOC Assistant uses a simple and professional web interface designed for security analysts.

The main goal of the UI/UX design is to make security information easy to understand, investigate and navigate.

The interface uses a consistent layout across the application so that users can move between different security modules without confusion.

---

## 2. Design Goals

The main UI/UX goals are:

* Simple navigation
* Professional cybersecurity dashboard
* Clear presentation of security alerts
* Easy log upload
* Easy risk identification
* Quick access to reports
* Easy access to AI security recommendations
* Responsive design
* Consistent colors and components

---

## 3. Overall Layout

The application uses a two-part layout:

```text
┌─────────────────────────────────────────────────────────┐
│                     TOP BAR                             │
├───────────────┬─────────────────────────────────────────┤
│               │                                         │
│    SIDEBAR    │              MAIN CONTENT               │
│               │                                         │
│   Home        │                                         │
│   Dashboard   │                                         │
│   Log Analysis│                                         │
│   Alerts      │                                         │
│   Reports     │                                         │
│   AI Assistant│                                         │
│               │                                         │
└───────────────┴─────────────────────────────────────────┘
```

The sidebar provides navigation while the main content area displays the selected page.

---

## 4. Color Theme

The application uses a dark professional security-themed interface.

Main colors include:

* Dark blue background
* Dark sidebar
* Blue-gray cards
* Cyan/teal primary accent
* Violet secondary accent
* White primary text
* Muted gray text
* Red for high-risk or dangerous alerts
* Yellow for medium-risk alerts
* Green for low-risk or successful operations

The color scheme helps distinguish different types of security information.

---

## 5. Sidebar Navigation

The sidebar is available throughout the main application.

Main navigation options are:

1. Home
2. Dashboard
3. Log Analysis
4. Alerts
5. Reports
6. AI Assistant

The active page is visually highlighted.

This allows the analyst to quickly move between different modules.

---

## 6. Login Page

The Login page is the entry point for authenticated users.

The page contains:

* Username field
* Password field
* Login button
* Error message for invalid credentials

The basic flow is:

```text
User
 ↓
Login Page
 ↓
Enter Username and Password
 ↓
Credential Verification
 ↓
Dashboard
```

If incorrect credentials are entered, the user receives an error message.

---

## 7. Home Page

The Home page provides an introduction to the AI SOC Assistant.

It explains the purpose of the system and provides access to the main application.

The Home page is designed to give the user a quick understanding of the project's purpose before using the security tools.

---

## 8. Dashboard Design

The Dashboard is the main monitoring interface.

It displays security information using cards and sections.

Important dashboard components include:

* Total Alerts
* Critical Alerts
* High Risk Alerts
* Medium Risk Alerts
* Low Risk Alerts
* Threat Score
* Overall Risk
* Recent Security Events
* Quick Actions

The statistics are presented using cards so that the analyst can understand the current security situation quickly.

---

## 9. Threat Score

The Dashboard displays an overall Threat Score.

The score is shown numerically along with a progress bar.

Example:

```text
Threat Score

72 / 100

██████████████████░░░░░░
```

This gives the analyst a quick indication of the overall security risk.

---

## 10. Alerts Page

The Alerts page is used for detailed security event investigation.

The page provides:

* Search box
* Risk filter
* Quick filters
* Alert count
* Alert table
* Event details
* Source IP
* Description

The analyst can filter alerts according to:

* All
* Critical
* High
* Medium
* Low

The search feature allows the analyst to search for event names, IP addresses, descriptions and log information.

---

## 11. Alert Details Page

When an analyst selects an individual alert, the application opens the Alert Details page.

The page provides more information about the selected event.

Information may include:

* Event name
* Risk level
* Source IP
* Description
* Log information
* Security details

This page is designed for deeper investigation of suspicious events.

---

## 12. Log Analysis Page

The Log Analysis page allows the analyst to upload security log files.

The interface contains:

* File selection
* Upload button
* Upload area
* Error messages when required
* Analysis result display

The basic user flow is:

```text
Select Log File
       ↓
Upload
       ↓
Analyze Log
       ↓
Detect Security Events
       ↓
Display Results
```

The interface is kept simple so that the analyst can start an analysis quickly.

---

## 13. Analysis Result Page

After a log is successfully analyzed, the application displays the analysis results.

The page provides information such as:

* Total log lines
* Total alerts
* Critical alerts
* High alerts
* Medium alerts
* Low alerts
* Threat score
* Overall risk
* Detected security events

This page allows the analyst to understand the result immediately after uploading a log.

---

## 14. Reports Page

The Reports page presents a summarized view of the latest security analysis.

It includes:

* Total alerts
* Critical alerts
* High alerts
* Medium alerts
* Low alerts
* Threat score
* Overall risk

The Reports page is designed to provide a quick security summary that can be used for analysis and presentation.

---

## 15. AI Assistant Page

The AI Assistant page provides security recommendations based on detected events.

The interface displays:

* Security event
* Risk level
* Source IP
* Description
* Recommended security actions

For example, a brute-force event may generate recommendations such as:

* Investigate the source IP
* Block suspicious IP addresses
* Enable MFA
* Review failed login attempts

The recommendations help the analyst understand what actions could be considered after detecting an event.

---

## 16. Firewall Result Page

The Firewall Result page displays the result of an IP blocking or unblocking operation.

It can show:

* IP address
* Operation performed
* Success or failure status
* Result message

Example:

```text
Firewall Operation

IP Address: 192.168.1.10

Status: Success

Message: IP has been blocked.
```

The page provides clear feedback so that the analyst knows whether the requested operation succeeded.

---

## 17. Buttons and Interactive Elements

The application uses consistent button styles.

Primary buttons are used for important actions such as:

* Login
* Upload
* Search
* View Alerts
* Analyze Log
* Reset

Navigation links are used for moving between application pages.

Buttons include hover effects to provide visual feedback to the user.

---

## 18. Cards

Cards are used to organize important information.

Examples include:

* Statistics cards
* Threat score card
* Search and filter card
* Recent events card
* Quick action card
* Report summary card

Cards use rounded corners, borders and shadows to separate different sections visually.

---

## 19. Tables

Tables are used when multiple security events need to be displayed.

The Alerts table contains information such as:

| Field       | Purpose                 |
| ----------- | ----------------------- |
| Event       | Name of detected event  |
| Risk        | Security risk level     |
| Source IP   | Source of the activity  |
| Description | Details about the event |

Tables make it easier to compare multiple security events.

---

## 20. Risk Indicators

The application uses different visual indicators for risk levels.

```text
CRITICAL → Highest priority
HIGH     → High priority
MEDIUM   → Moderate priority
LOW      → Lower priority
```

Colors and badges help the analyst identify important alerts quickly.

---

## 21. Responsive Design

The application includes responsive CSS rules.

On smaller screens:

* Sidebar width is reduced
* Navigation text may be hidden
* Statistics cards change from multiple columns to fewer columns
* Content becomes easier to view on smaller screens
* Tables can scroll horizontally

This allows the application to remain usable on different screen sizes.

---

## 22. User Experience Principles

The application follows these UX principles:

### Consistency

Similar buttons, cards, tables and navigation elements use consistent styling.

### Visibility

Important security information such as risk level and threat score is clearly visible.

### Simplicity

The user does not need to navigate through complicated menus to perform basic operations.

### Feedback

The application provides feedback after operations such as login, upload and firewall actions.

### Error Handling

Invalid login credentials, missing files and invalid IP addresses generate appropriate error messages.

---

## 23. Accessibility Considerations

Basic accessibility considerations include:

* Clear text labels
* Readable font sizes
* High contrast between text and background
* Clearly identifiable buttons
* Logical navigation structure
* Descriptive page headings

Future versions can improve accessibility further with complete keyboard navigation and additional screen-reader support.

---

## 24. Frontend Technologies

The frontend uses:

* HTML5
* CSS3
* Jinja2 templates
* JavaScript where required

The common stylesheet is:

```text
static/css/style.css
```

Reusable navigation is maintained through:

```text
templates/components/sidebar.html
```

This reduces duplication across pages.

---

## 25. UI/UX File Structure

The frontend-related structure is:

```text
templates/
│
├── login.html
├── index.html
├── dashboard.html
├── upload.html
├── analysis.html
├── alerts.html
├── alert_details.html
├── reports.html
├── ai.html
├── firewall_result.html
│
└── components/
    └── sidebar.html

static/
│
├── css/
│   └── style.css
│
├── js/
│
└── images/
```

The `js` and `images` folders are available for JavaScript functionality and visual assets used by the application.

---

## 26. Future UI/UX Improvements

Future versions could include:

* Interactive charts
* Real-time security graphs
* Dark/light theme selection
* Advanced dashboard widgets
* Notification system
* Drag-and-drop log upload
* Better mobile navigation
* Interactive threat maps
* Exportable reports
* More advanced accessibility support

---

## 27. Conclusion

The UI/UX design of the AI SOC Assistant focuses on simplicity, consistency and security monitoring.

The sidebar provides easy navigation, dashboards provide quick security information, alerts support investigation, reports provide summaries, and the AI Assistant provides security recommendations.

The overall interface is designed to provide a professional SOC-style experience while remaining simple enough for users to understand and operate.
