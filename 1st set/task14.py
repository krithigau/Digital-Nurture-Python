def assign_grade(score):
    # Validate score
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        return
        
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    else:
        print("Grade: F")

score = 88
assign_grade(score)
#krithiga task 14