import turtle
import math
import csv

# Define max canvas size
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
MARGIN = 50  # Margin for tick marks and labels

# Function to approximate the perimeter of an ellipse (Ramanujan’s formula)
def ellipse_perimeter(a, b):
    return math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b)))

# Function to determine spacing based on ellipse size
def compute_point_spacing(a, b):
    max_dim = max(a, b)
    return max(0.1, min(1.0, max_dim / 300))  # Larger ellipses get ~1 unit, small ones ~0.1

# Function to generate evenly spaced points along the ellipse
def generate_ellipse_points(a, b, scale):
    perimeter = ellipse_perimeter(a, b) * scale  # Scaled perimeter
    spacing = compute_point_spacing(a, b) * scale  # Adjust spacing based on size
    num_points = max(10, int(perimeter / spacing))  # Adjust points based on new spacing
    points = []

    arc_length = 0  # Track total arc length
    prev_x, prev_y = scale * a, 0  # Start at (a, 0)

    for i in range(num_points):
        t = i / num_points * 2 * math.pi  # Approximate equal spacing using angle
        x = scale * a * math.cos(t)
        y = scale * b * math.sin(t)

        # Calculate distance from the previous point
        segment_length = math.sqrt((x - prev_x) ** 2 + (y - prev_y) ** 2)
        arc_length += segment_length

        # Only add points that maintain uniform arc length
        if arc_length >= spacing:
            points.append((x, y))
            prev_x, prev_y = x, y
            arc_length = 0  # Reset arc length tracker

    return points

# Function to draw the ellipse
def draw_ellipse(a, b, scale):
    points = generate_ellipse_points(a, b, scale)
    
    # Set turtle speed to max and disable screen update for faster drawing
    turtle.speed(0)  # Maximum speed
    turtle.tracer(0)  # Disable automatic screen updates

    turtle.penup()
    turtle.goto(points[0])  # Move to first point
    turtle.pendown()

    # Draw the ellipse
    for x, y in points:
        turtle.goto(x, y)

    turtle.goto(points[0])  # Close the shape
    turtle.penup()

    turtle.update()  # Manually update the screen
    return points  # Return the calculated points

# Function to draw the axes with dynamically scaled tick marks
def draw_axes(a, b, scale):
    scaled_a = scale * a
    scaled_b = scale * b
    scale_x = scaled_a * 1.1  # Extend axis slightly beyond ellipse
    scale_y = scaled_b * 1.1
    tick_spacing_x = max(1, round(a / 10))  # Properly scale tick spacing
    tick_spacing_y = max(1, round(b / 10))
    tick_length = min(scaled_a, scaled_b) / 15  # Keep tick length proportional

    # Draw X-axis
    turtle.penup()
    turtle.goto(-scale_x, 0)
    turtle.pendown()
    turtle.goto(scale_x, 0)
    turtle.penup()

    # X-axis tick marks and labels
    for x in range(-a, a + 1, tick_spacing_x):
        scaled_x = x * scale
        if scaled_x == 0:
            continue
        turtle.goto(scaled_x, -tick_length / 2)
        turtle.pendown()
        turtle.goto(scaled_x, tick_length / 2)
        turtle.penup()
        turtle.goto(scaled_x - 5, -20)
        turtle.write(str(x), align="center", font=("Arial", 10, "normal"))

    # Draw Y-axis
    turtle.penup()
    turtle.goto(0, -scale_y)
    turtle.pendown()
    turtle.goto(0, scale_y)
    turtle.penup()

    # Y-axis tick marks and labels
    for y in range(-b, b + 1, tick_spacing_y):
        scaled_y = y * scale
        if scaled_y == 0:
            continue
        turtle.goto(-tick_length / 2, scaled_y)
        turtle.pendown()
        turtle.goto(tick_length / 2, scaled_y)
        turtle.penup()
        turtle.goto(-20, scaled_y - 5)
        turtle.write(str(y), align="right", font=("Arial", 10, "normal"))

# Function to compute the scaling factor
def compute_scaling_factor(a, b):
    max_a = CANVAS_WIDTH / 2 - MARGIN  # Half canvas width minus margin
    max_b = CANVAS_HEIGHT / 2 - MARGIN  # Half canvas height minus margin

    scale_x = max_a / a
    scale_y = max_b / b

    return min(scale_x, scale_y)  # Use the smallest scale factor to fit both axes

# Function to write points to a CSV file (Excel-compatible)
def write_points_to_csv(points, filename="ellipse_points.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=',')  # Specify delimiter as comma
        writer.writerow(["X", "Y"])  # Write headers
        for point in points:
            writer.writerow(point)  # Write each point as a row

# Main function
def main():
    a = 5  # Semi-major axis (user-defined)
    b = 10  # Semi-minor axis (user-defined)

    # Compute scaling factor
    scale = compute_scaling_factor(a, b)

    # Center the drawing
    turtle.setup(CANVAS_WIDTH, CANVAS_HEIGHT)  # Set up the window size
    turtle.speed(0)  # Maximum turtle speed
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    # Draw axes with tick marks that scale correctly
    draw_axes(a, b, scale)

    # Draw the ellipse
    points = draw_ellipse(a, b, scale)

    # Print points to console (converted back to original scale)
    print("\nEllipse Points (X, Y):")
    for x, y in points:
        print(f"({x/scale:.2f}, {y/scale:.2f})")  # Convert back to original scale

    # Write points to CSV file in Excel-compatible format
    write_points_to_csv(points)
    print(f"\nEllipse points have been written to 'ellipse_points.csv'")

    # Print total number of points AFTER listing them
    print(f"\nTotal number of points: {len(points)}")

    # Hide Turtle and display
    turtle.hideturtle()
    turtle.done()

# Run the script
main()
