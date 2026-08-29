import subprocess
import ipaddress


def validate_ip(ip):
    """
    Check whether the given value is a valid IPv4 address.
    """

    try:
        ipaddress.ip_address(ip)
        return True

    except ValueError:
        return False


def block_ip(ip):
    """
    Block an IP address using Windows Defender Firewall.
    """

    if not validate_ip(ip):
        return {
            "success": False,
            "message": "Invalid IP address."
        }

    rule_name = f"AI_SOC_Block_{ip.replace('.', '_')}"

    command = [
        "netsh",
        "advfirewall",
        "firewall",
        "add",
        "rule",
        f"name={rule_name}",
        "dir=in",
        "action=block",
        f"remoteip={ip}"
    ]

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=False
        )

        if result.returncode == 0:

            return {
                "success": True,
                "message": f"IP {ip} has been blocked.",
                "ip": ip,
                "rule": rule_name
            }

        return {
            "success": False,
            "message": result.stderr.strip()
                or "Unable to create firewall rule."
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }


def unblock_ip(ip):
    """
    Remove the firewall rule created by this application.
    """

    if not validate_ip(ip):
        return {
            "success": False,
            "message": "Invalid IP address."
        }

    rule_name = f"AI_SOC_Block_{ip.replace('.', '_')}"

    command = [
        "netsh",
        "advfirewall",
        "firewall",
        "delete",
        "rule",
        f"name={rule_name}"
    ]

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=False
        )

        if result.returncode == 0:

            return {
                "success": True,
                "message": f"IP {ip} has been unblocked.",
                "ip": ip
            }

        return {
            "success": False,
            "message": result.stderr.strip()
                or "Unable to remove firewall rule."
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }


def is_ip_blocked(ip):
    """
    Check whether our firewall rule exists for the IP.
    """

    if not validate_ip(ip):
        return False

    rule_name = f"AI_SOC_Block_{ip.replace('.', '_')}"

    command = [
        "netsh",
        "advfirewall",
        "firewall",
        "show",
        "rule",
        f"name={rule_name}"
    ]

    try:

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=False
        )

        return result.returncode == 0 and rule_name in result.stdout

    except Exception:
        return False