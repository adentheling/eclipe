import numpy as np
import matplotlib.pyplot as plt
import csv

# Function to generate evenly spaced points along an ellipse
def generate_ellipse_points(a, b, num_points):
    t = np.linspace(0, 2 * np.pi, num_points)  # Parameter t
    x = a * np.cos(t)  # X points of ellipse
    y = b * np.sin(t)  # Y points of ellipse
    return x, y

# Function to write points to a CSV file with adjustable point density
def write_points_to_csv(points, csv_point_reduction_factor, spacing, y_offset_percentage, filename="ellipse_points.csv"):
    total_saved_points = 0  # Track the number of points saved

    # Calculate the Y offset based on the percentage
    y_offset = y_offset_percentage * spacing / 100

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(["X", "Y"])  # Write headers

        for point in points:
            x_data, y_data = point
            for i in range(0, len(x_data), csv_point_reduction_factor):  # Save every nth point
                writer.writerow([x_data[i], y_data[i] + y_offset])  # Apply dynamic Y-axis offset
                total_saved_points += 1  # Count points saved

    print(f"\n✅ Total points saved to CSV: {total_saved_points}")

# Function to generate nested ellipses with scarf joints
def draw_nested_ellipses_with_scarf(a, b, spacing, bbox_a, bbox_b, ax, y_offset_percentage):
    num_points_per_ellipse = 2000  # Increased resolution of ellipses
    current_a, current_b = a, b
    prev_x, prev_y = generate_ellipse_points(current_a, current_b, num_points_per_ellipse)

    # Calculate the Y offset based on the percentage
    y_offset = y_offset_percentage * spacing / 100

    last_x, last_y = prev_x, prev_y
    generated_ellipses = []  # Store ellipses for CSV

    # Initialize max values for the bounds
    max_x, max_y = max(prev_x), max(prev_y)
    min_x, min_y = min(prev_x), min(prev_y)

    # Generate nested ellipses until bounding ellipse is intersected
    while True:
        current_a += spacing
        current_b += spacing
        
        # Generate the new ellipse
        x, y = generate_ellipse_points(current_a, current_b, num_points_per_ellipse)
        
        # Check if any part of the ellipse intersects the bounding ellipse
        intersects = any((px**2 / bbox_a**2 + py**2 / bbox_b**2) >= 1 for px, py in zip(x, y))
        
        if intersects:
            # Final scarf joint
            t = np.linspace(0, 1, len(last_x))
            x_scarf = (1 - t) * last_x + t * prev_x
            y_scarf = (1 - t) * last_y + t * prev_y
            ax.plot(x_scarf, y_scarf + y_offset, 'k')  # Apply Y-axis offset
            break  # Stop once intersection occurs
        
        # Plot the current ellipse with scarf joint as black line
        t = np.linspace(0, 1, len(x))
        x_scarf = (1 - t) * prev_x + t * x  # Interpolate x
        y_scarf = (1 - t) * prev_y + t * y  # Interpolate y
        ax.plot(x_scarf, y_scarf + y_offset, 'k')  # Apply Y-axis offset
        
        # Store generated ellipses for CSV
        generated_ellipses.append((x_scarf, y_scarf))
        
        # Update max and min values to track the bounding box
        max_x = max(max_x, max(x_scarf))
        min_x = min(min_x, min(x_scarf))
        max_y = max(max_y, max(y_scarf))
        min_y = min(min_y, min(y_scarf))
        
        # Update previous ellipse
        last_x, last_y = prev_x, prev_y
        prev_x, prev_y = x, y

    # Add 10mm to each end for the plot bounds
    ax.set_xlim(min_x - 10, max_x + 10)
    ax.set_ylim(min_y - 10, max_y + 10)

    return generated_ellipses

# Main function
def main():
    a = 60  # Initial semi-major axis a (in mm)
    b = 2  # Initial semi-minor axis (in mm)
    spacing = 5  # Spacing between ellipses (in mm)
    bbox_a = a * 21  # Bounding ellipse semi-major axis (in mm)
    bbox_b = b * 21  # Bounding ellipse semi-minor axis (in mm)
    csv_point_reduction_factor = 10  # Adjust how many points are saved in CSV
    y_offset_percentage = 25  # Percentage to move the diagram up (e.g., 30%)

    # Generate the ellipses and calculate the final bounding box size
    fig, ax = plt.subplots(figsize=(8, 8))  # Use a standard size for the figure
    ax.set_aspect('equal', 'box')

    # Generate ellipses
    generated_ellipses = draw_nested_ellipses_with_scarf(a, b, spacing, bbox_a, bbox_b, ax, y_offset_percentage)

    # Write points to CSV (excluding bounding ellipse)
    write_points_to_csv(generated_ellipses, csv_point_reduction_factor, spacing, y_offset_percentage)
    
    # Remove title and axes labels
    ax.set_title('')  # Remove title
    ax.set_xlabel('')  # Remove x-axis label
    ax.set_ylabel('')  # Remove y-axis label
    ax.grid(False)  # Disable grid
    ax.legend([])  # Remove legend
    ax.set_axis_off()  # Remove the axis

    # Show plot
    plt.show()

    # Save the plot as an SVG file after removing unwanted elements
    fig.savefig("nested_ellipses_spiral.svg", format='svg', bbox_inches='tight')

# Run the script
main()
