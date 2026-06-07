"""
 Data Analysis Pipeline
• Objective: Use modules, functions, lists, file handling, and error handling together.
• Task: Process sales data from a file and calculate statistics.
"""
import statistics
def analyze_sales():
    try:
        with open("sales.txt","r") as file:
            sales=[]
            for line in file:
                sales.append(float(line.strip()))
        mean_sales = statistics.mean(sales)
        median_sales = statistics.mean(sales)
        print("sales Data:",sales)
        print("Mean:",mean_sales)
        print("Median:",median_sales)
    except FileNotFoundError:
        print("sales.txt not found")
    except ValueError:
        print("Invalid data in file")
analyze_sales()



















