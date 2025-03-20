import numpy as np
import matplotlib.pyplot as plt
import csv

# Define max canvas size
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
MARGIN = 50  # Margin for tick marks and labels

# Function to generate evenly spaced points along an ellipse
def generate_ellipse_points(a, b, num_points):
    t = np.linspace(0, 2 * np.pi, num_points)  # Parameter t
    x = a * np.cos(t)  # X points of ellipse
    y = b * np.sin(t)  # Y points of ellipse
    return x, y

# Function to compute the scaling factor
def compute_scaling_factor(a, b):
    max_a = CANVAS_WIDTH / 2 - MARGIN  # Half canvas width minus margin
    max_b = CANVAS_HEIGHT / 2 - MARGIN  # Half canvas height minus margin
    scale_x = max_a / a
    scale_y = max_b / b
    return min(scale_x, scale_y)  # Use the smallest scale factor to fit both axes

# Function to write points to a CSV file (excluding the outermost ellipse)
def write_points_to_csv(points, filename="ellipse_points.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=',')  # Specify delimiter as comma
        writer.writerow(["X", "Y"])  # Write headers
        for point in points[1:]:  # Skip the first (outermost) ellipse
            for x, y in zip(point[0], point[1]):  # Iterate over x, y points
                writer.writerow([x, y])  # Write each point

# Function to generate and draw nested ellipses with scarf joints, ending at (0,0)
def draw_nested_ellipses_with_scarf(a, b, spacing, ax):
    current_a, current_b = a, b
    points_list = []
    prev_x, prev_y = generate_ellipse_points(current_a, current_b, 500)  # Initial ellipse points

    # Draw the outermost ellipse as a dotted line
    ax.plot(prev_x, prev_y, 'k--', label="Outermost Ellipse")  # Dotted line for outer ellipse

    # Continue generating ellipses until one axis goes negative
    while current_a > 0 and current_b > 0:
        # Reduce semi-axes
        current_a -= spacing
        current_b -= spacing
        if current_a <= 0 or current_b <= 0:
            break  # Stop when one axis becomes negative

        # Generate points for the current ellipse
        x, y = generate_ellipse_points(current_a, current_b, 500)
        points_list.append((x, y))

        # Add scarf joint: interpolate between the previous and current ellipse
        t = np.linspace(0, 1, len(x))
        x_scarf = (1 - t) * prev_x + t * x  # Interpolate x
        y_scarf = (1 - t) * prev_y + t * y  # Interpolate y

        # Plot the current ellipse with the scarf joint transition
        ax.plot(x_scarf, y_scarf, label=f'a={current_a:.1f}, b={current_b:.1f}')

        # Set the current ellipse as the previous ellipse for the next iteration
        prev_x, prev_y = x, y

    # **Ensure the last ellipse ends at (0,0) smoothly**
    t_final = np.linspace(0, 1, len(prev_x))
    x_final = (1 - t_final) * prev_x  # Gradually shrink X to 0
    y_final = (1 - t_final) * prev_y  # Gradually shrink Y to 0

    # Plot the final transition to (0,0)
    ax.plot(x_final, y_final, 'r', label="Final Transition to (0,0)")
    points_list.append((x_final, y_final))  # Add to CSV data

    return points_list  # Return ellipse points (excluding outermost)

# Main function
def main():
    a = 50  # Semi-major axis (user-defined)
    b = 100  # Semi-minor axis (user-defined)
    spacing = 5  # Spacing between each nested ellipse

    # Compute scaling factor
    scale = compute_scaling_factor(a, b)

    # Set up the plot
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-CANVAS_WIDTH / 2, CANVAS_WIDTH / 2)
    ax.set_ylim(-CANVAS_HEIGHT / 2, CANVAS_HEIGHT / 2)
    ax.set_aspect('equal', 'box')

    # Draw nested ellipses inside the large ellipse with scarf joint transition
    nested_points = draw_nested_ellipses_with_scarf(a, b, spacing, ax)

    # Write points to CSV (excluding the outermost ellipse)
    write_points_to_csv(nested_points)
    print(f"\nNested ellipse points with scarf joint have been written to 'ellipse_points.csv'")

    # Print total number of points AFTER listing them
    total_points = sum(len(x) for x, y in nested_points[1:])  # Exclude outermost
    print(f"\nTotal number of points (excluding outermost ellipse): {total_points}")

    # Show plot
    ax.set_title('Nested Ellipses with Scarf Joint (Final at 0,0)')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    plt.show()

# Run the script
main()
