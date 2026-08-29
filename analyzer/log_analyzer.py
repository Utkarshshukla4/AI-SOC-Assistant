import re
from collections import Counter


def extract_ip(line):
    """
    Extract an IPv4 address from a log line.
    """

    match = re.search(
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        line
    )

    if match:
        return match.group()

    return None


def analyze_log_file(file_path):
    """
    Analyze a security log file.
    Detect suspicious activities and calculate risk.
    """

    results = []

    try:

        # -----------------------------------------
        # Read log file
        # -----------------------------------------

        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            lines = file.readlines()


        # -----------------------------------------
        # Count failed login IPs
        # -----------------------------------------

        failed_login_ips = []


        for line in lines:

            if re.search(
                r"failed login|login failed|authentication failed",
                line,
                re.IGNORECASE
            ):

                ip = extract_ip(line)

                if ip:
                    failed_login_ips.append(ip)


        failed_ip_counter = Counter(failed_login_ips)


        # -----------------------------------------
        # Analyze every line
        # -----------------------------------------

        for line in lines:

            line = line.strip()

            if not line:
                continue


            ip = extract_ip(line)


            # =========================================
            # BRUTE FORCE DETECTION
            # =========================================

            if re.search(
                r"failed login|login failed|authentication failed",
                line,
                re.IGNORECASE
            ):

                # If same IP failed 3 or more times
                if ip and failed_ip_counter[ip] >= 3:

                    results.append({
                        "event": "Possible Brute-Force Attack",
                        "risk": "CRITICAL",
                        "ip": ip,
                        "description": (
                            f"{ip} generated "
                            f"{failed_ip_counter[ip]} failed "
                            f"login attempts."
                        )
                    })

                else:

                    results.append({
                        "event": "Failed Login Attempt",
                        "risk": "HIGH",
                        "ip": ip or "Unknown",
                        "description": line
                    })


            # =========================================
            # PORT SCANNING
            # =========================================

            elif re.search(
                r"port scan|port scanning|nmap|scan detected",
                line,
                re.IGNORECASE
            ):

                results.append({
                    "event": "Possible Port Scanning",
                    "risk": "HIGH",
                    "ip": ip or "Unknown",
                    "description": line
                })


            # =========================================
            # SUSPICIOUS CONNECTION
            # =========================================

            elif re.search(
                r"suspicious connection|"
                r"malicious connection|"
                r"blocked connection",
                line,
                re.IGNORECASE
            ):

                results.append({
                    "event": "Suspicious Network Activity",
                    "risk": "MEDIUM",
                    "ip": ip or "Unknown",
                    "description": line
                })


            # =========================================
            # MALWARE
            # =========================================

            elif re.search(
                r"malware|virus|trojan|ransomware",
                line,
                re.IGNORECASE
            ):

                results.append({
                    "event": "Possible Malware Activity",
                    "risk": "CRITICAL",
                    "ip": ip or "Unknown",
                    "description": line
                })


            # =========================================
            # UNAUTHORIZED ACCESS
            # =========================================

            elif re.search(
                r"unauthorized access|"
                r"access denied|"
                r"privilege escalation",
                line,
                re.IGNORECASE
            ):

                results.append({
                    "event": "Unauthorized Access Attempt",
                    "risk": "HIGH",
                    "ip": ip or "Unknown",
                    "description": line
                })


        # -----------------------------------------
        # Count risk levels
        # -----------------------------------------

        critical_count = 0
        high_count = 0
        medium_count = 0
        low_count = 0


        for result in results:

            if result["risk"] == "CRITICAL":
                critical_count += 1

            elif result["risk"] == "HIGH":
                high_count += 1

            elif result["risk"] == "MEDIUM":
                medium_count += 1

            else:
                low_count += 1


        # -----------------------------------------
        # Overall threat level
        # -----------------------------------------

        if critical_count > 0:

            overall_risk = "CRITICAL"

        elif high_count >= 3:

            overall_risk = "HIGH"

        elif high_count > 0 or medium_count > 0:

            overall_risk = "MEDIUM"

        else:

            overall_risk = "LOW"


        # -----------------------------------------
        # Return complete analysis
        # -----------------------------------------

        return {

            "success": True,

            "total_lines": len(lines),

            "total_alerts": len(results),

            "critical": critical_count,

            "high": high_count,

            "medium": medium_count,

            "low": low_count,

            "overall_risk": overall_risk,

            "results": results

        }


    except Exception as error:

        return {

            "success": False,

            "error": str(error),

            "results": []

        }