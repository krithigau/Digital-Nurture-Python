def calculate_rectangle_area(length, width):
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        print("Invalid dimensions Krithi..")
        return
    if length < 0 or width < 0:
        print("Dimensions must be positive.")
        return
        
    return length * width

print(f"Area of rectangle (5x3): {calculate_rectangle_area(5, 3)}")