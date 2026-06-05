def check_pass_status(marks):
    if not isinstance(marks, (int, float)) or marks < 0 or marks > 100:
        print("Invalid marks. Must be between 0 and 100.")
        return
        
    if marks >= 35:
        print("Result: Pass")
    if marks < 35:
        print("Result: Fail")

marks = 75
check_pass_status(marks)