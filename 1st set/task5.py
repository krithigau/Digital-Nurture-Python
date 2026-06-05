#KRITHIGA U task5
def display_coordinates(coords):
    # Validate that coordinates are a tuple/list of exactly two numbers
    if not isinstance(coords, (tuple, list)) or len(coords) != 2:
        print("Invalid coordinates. Provide an (x, y) pair.")
        return
    if not all(isinstance(i, (int, float)) for i in coords):
        print("Coordinates must be numbers.")
        return
    x, y = coords
    print(f"X-Coordinate: {x} | Y-Coordinate: {y}")

display_coordinates((150, 200))