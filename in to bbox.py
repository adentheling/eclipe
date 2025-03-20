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

    ax.plot(prev_x, prev_y + y_offset, 'k--', label="Initial Ellipse")  # Dotted line for first ellipse
    
    last_x, last_y = prev_x, prev_y
    generated_ellipses = []  # Store ellipses for CSV

    # Plot the bounding ellipse (dotted red line)
    bbox_x, bbox_y = generate_ellipse_points(bbox_a, bbox_b, num_points_per_ellipse)
    ax.plot(bbox_x, bbox_y + y_offset, 'r--', label="Bounding Ellipse")  # Bounding ellipse in dotted red line
    
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
            ax.plot(x_scarf, y_scarf + y_offset, 'b', label="Final Scarf Joint")  # Apply Y-axis offset
            break  # Stop once intersection occurs
        
        # Plot the current ellipse with scarf joint
        t = np.linspace(0, 1, len(x))
        x_scarf = (1 - t) * prev_x + t * x  # Interpolate x
        y_scarf = (1 - t) * prev_y + t * y  # Interpolate y
        ax.plot(x_scarf, y_scarf + y_offset, label=f'a={current_a:.1f}, b={current_b:.1f}')  # Apply Y-axis offset
        
        # Store generated ellipses for CSV
        generated_ellipses.append((x_scarf, y_scarf))
        
        # Update previous ellipse
        last_x, last_y = prev_x, prev_y
        prev_x, prev_y = x, y
    
    return generated_ellipses

# Main function
def main():
    a = 60  # Initial semi-major axis a gotta be bigger than b 
    b = 2  # Initial semi-minor axis
    spacing = 5  # Spacing between ellipses
    bbox_a = a * 21  # Bounding ellipse semi-major axis
    bbox_b = b * 21  # Bounding ellipse semi-minor axis
    csv_point_reduction_factor = 10  # Adjust how many points are saved in CSV
    y_offset_percentage = 25  # Percentage to move the diagram up (e.g., 30%)

    # Set up the plot with full-screen size
    fig, ax = plt.subplots(figsize=(22, 22))  # Maximize figure size
    ax.set_xlim(-bbox_a * 1.1, bbox_a * 1.1)  # Scale dynamically based on bounding ellipse
    ax.set_ylim(-bbox_b * 1.1, bbox_b * 1.1)
    ax.set_aspect('equal', 'box')

    # Generate ellipses
    generated_ellipses = draw_nested_ellipses_with_scarf(a, b, spacing, bbox_a, bbox_b, ax, y_offset_percentage)

    # Write points to CSV (excluding bounding ellipse)
    write_points_to_csv(generated_ellipses, csv_point_reduction_factor, spacing, y_offset_percentage)
    
    # Show plot
    ax.set_title('Ellipses Expanding to Bounding Ellipse with Scarf Joints')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    plt.show()

# Run the script
main()
