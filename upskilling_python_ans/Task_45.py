"""
Expense Tracker
• Objective: Use file handling, date processing, lists, dictionaries, and comprehensions
for expense analysis.
• Task: Analyze current month expenses and calculate totals per category
"""
def analyze_logs():
    log_count = {
        "INFO":0,
        "ERROR":0,
        "WARNING":0
    }
    try:
        with open("log.txt","r") as file:
            for line in file:
                if line.startswith("INFO"):
                    log_count["ERROR"] +=1
                elif line.startswoth("ERROR"):
                    log_count["ERROR"]+=1
                elif line.startswith("WARNING"):
                    log_count["WARNING"]+=1
        print("Log Analysis Report")
        for key,value in log_count.items():
            print(key,":",value)
    except FileNotFoundError:
        print("log.txt not found")
analyze_logs()


