"""
Create Tuple
• Objective: Use an immutable tuple with a function and basic validation.
• Task: Store fixed coordinates and display them.
"""
def display_coordinattes():
    coordinates = (10,20)
    if len(coordinates) == 2:
        x,y = coordinates
        print("X Coordinate: ",x)
        print("Y coordinate: ",y)
    else:
        print("Invalid coordinates")
display_coordinattes()