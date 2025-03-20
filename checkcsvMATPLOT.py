import csv
import matplotlib.pyplot as plt
import numpy as np
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

# Function to calculate the distance from the origin (0,0)
def calculate_distance_from_origin(x, y):
    return math.sqrt(x**2 + y**2)

# Function to calculate colors based on distance
def calculate_color(distance, max_distance):
    # Normalize the distance to a value between 0 and 1
    normalized_distance = distance / max_distance
    # Map normalized distance to RGB values (Red → Green → Blue)
    red = max(0, 1 - normalized_distance)  # Closer = more red
    green = 0  # Green remains 0, as we want a red-to-blue gradient
    blue = min(1, normalized_distance)  # Farther = more blue
    return red, green, blue

# Function to calculate Euclidean distance between two points
def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Function to plot points with Matplotlib
def plot_points_with_matplotlib(points):
    # Calculate the distance of each point from the origin
    distances = [calculate_distance_from_origin(x, y) for x, y in points]
    
    # Find the maximum distance to normalize the color scale
    max_distance = max(distances)
    
    # Create an array of colors based on the distance
    colors = [calculate_color(dist, max_distance) for dist in distances]
    
    # Extract x and y coordinates for plotting
    x_vals = [x for x, y in points]
    y_vals = [y for x, y in points]
    
    # Plot the points with the calculated colors
    plt.scatter(x_vals, y_vals, c=colors, s=10)  # 's' controls the size of the points
    
    # Plot lines between consecutive points (with a very thin line)
    for i in range(1, len(points)):
        plt.plot([x_vals[i-1], x_vals[i]], [y_vals[i-1], y_vals[i]], color='gray', linewidth=0.5)
    
    # Add lines on the x and y axes
    plt.axhline(0, color='black', linewidth=1)  # Horizontal line at y=0
    plt.axvline(0, color='black', linewidth=1)  # Vertical line at x=0
    
    plt.title("Points with Distance-Based Color Gradient and Connecting Lines")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.colorbar()  # Show a color bar

    # Store the clicked points
    clicked_points = []

    # Function to handle mouse click event
    def on_click(event):
        # Only capture clicks inside the plot area
        if event.inaxes:
            clicked_points.append((event.xdata, event.ydata))
            if len(clicked_points) == 2:
                # Calculate distance between two clicked points
                p1, p2 = clicked_points
                distance = calculate_euclidean_distance(p1, p2)
                # Print the distance to the console
                print(f"Distance: {distance:.2f}")
                clicked_points.clear()  # Reset after displaying the distance

    # Connect the click event to the function
    plt.gcf().canvas.mpl_connect('button_press_event', on_click)

    plt.show()

# Main function
def main():
    # Read points from the CSV file
    points = read_points_from_csv("ellipse_points.csv")
    
    # Plot the points using Matplotlib with the color gradient and lines between points
    plot_points_with_matplotlib(points)

# Run the script
main()
