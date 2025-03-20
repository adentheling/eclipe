import csv
import turtle
import math

# Function to read points from the CSV file
def read_points_from_csv(filename="ellipse_points.csv"):
    points = []
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            # Append each row (X, Y) to the points list as a tuple
            points.append((float(row[0]), float(row[1])))
    return points

# Function to calculate scaling factors based on the point's min and max values
def calculate_scaling_factor(points, width, height):
    min_x = min(points, key=lambda p: p[0])[0]
    max_x = max(points, key=lambda p: p[0])[0]
    min_y = min(points, key=lambda p: p[1])[1]
    max_y = max(points, key=lambda p: p[1])[1]
    
    # Calculate scaling factors based on the window size
    scale_x = (width - 40) / (max_x - min_x)  # Subtract margin
    scale_y = (height - 40) / (max_y - min_y)  # Subtract margin
    
    scale = min(scale_x, scale_y)  # Use the smaller scaling factor to ensure the ellipse fits
    return scale, min_x, max_x, min_y, max_y  # Return all necessary values

# Function to calculate the color based on distance
def calculate_color(distance, max_distance):
    # Normalize the distance to a value between 0 and 1
    normalized_distance = distance / max_distance
    # Map normalized distance to RGB values (Red → Green → Blue)
    red = max(0, 1 - normalized_distance)  # Closer = more red
    green = 0  # Green remains 0, as we want a red-to-blue gradient
    blue = min(1, normalized_distance)  # Farther = more blue
    return red, green, blue

# Function to plot the points using turtle with color gradient
def plot_points_with_turtle(points, scale, min_x, min_y, max_x, max_y, width, height):
    turtle.speed(0)  # Set turtle to the fastest speed
    turtle.penup()
    turtle.tracer(0)  # Turn off screen updates for fast drawing

    # Calculate the center of the screen
    center_x = width / 2
    center_y = height / 2

    # Calculate the width and height of the bounding box of the ellipse
    ellipse_width = (max_x - min_x) * scale
    ellipse_height = (max_y - min_y) * scale

    # Calculate the offset to center the ellipse within the window
    offset_x = center_x - ellipse_width / 2
    offset_y = center_y - ellipse_height / 2

    # Find the maximum distance from the center to calculate color scaling
    max_distance = max(math.sqrt(x**2 + y**2) for x, y in points)

    # Move to the starting position (scaled and centered)
    turtle.goto((points[0][0] - min_x) * scale + offset_x, (points[0][1] - min_y) * scale + offset_y)
    turtle.pendown()

    # Plot each point with scaling and centering, changing color based on distance
    for x, y in points:
        # Calculate distance from the origin (or center)
        distance = math.sqrt(x**2 + y**2)
        
        # Get the color based on the distance
        red, green, blue = calculate_color(distance, max_distance)
        turtle.pencolor(red, green, blue)  # Set the turtle pen color

        # Scale and center the points
        scaled_x = (x - min_x) * scale + offset_x
        scaled_y = (y - min_y) * scale + offset_y
        turtle.goto(scaled_x, scaled_y)

    turtle.hideturtle()  # Hide the turtle after drawing
    turtle.update()  # Update the screen at once

# Main function
def main():
    # Read points from the CSV file
    points = read_points_from_csv("ellipse_points.csv")

    # Set up the window size to 300x300
    window_width = 300
    window_height = 300
    turtle.setup(window_width, window_height)

    # Calculate scaling factor based on the points
    scale, min_x, max_x, min_y, max_y = calculate_scaling_factor(points, window_width, window_height)

    # Scale up if too small or down if too large
    if scale > 1:
        scale = 1  # Limit the scale so it doesn't go beyond the window
    elif scale < 0.1:
        scale = 0.1  # Ensure the scale doesn't become too small

    # Plot the points using turtle with dynamic scaling and centering
    plot_points_with_turtle(points, scale, min_x, min_y, max_x, max_y, window_width, window_height)

    # Keep the window open until manually closed
    turtle.done()

# Run the script
main()
