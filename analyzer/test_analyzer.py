from log_analyzer import analyze_log_file


file_path = "uploads/test_security.log"


result = analyze_log_file(file_path)


print("\n==============================")
print("      AI SOC LOG ANALYZER")
print("==============================\n")


if result["success"]:

    print("Total Alerts :", result["total_alerts"])
    print("High Risk    :", result["high"])
    print("Medium Risk  :", result["medium"])
    print("Low Risk     :", result["low"])


    print("\nDetected Events:")
    print("------------------------------")


    for item in result["results"]:

        print(
            f"[{item['risk']}] "
            f"{item['event']}"
        )

        print(
            f"  {item['description']}"
        )

else:

    print("Error:", result["error"])