import numpy as np
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D

# Function to read CSV points (expects columns "X" and "Y")
def read_points_from_csv(filename="ellipse_points.csv"):
    x_points, y_points = [], []
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            x_points.append(float(row[0]))
            y_points.append(float(row[1]))
    return np.array(x_points), np.array(y_points)

# Function to rotate 2D points by a specified angle (in degrees)
def rotate_points(x, y, angle_deg=45):
    angle_rad = np.radians(angle_deg)
    # Rotation matrix (counterclockwise)
    R = np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
                  [np.sin(angle_rad),  np.cos(angle_rad)]])
    points = np.vstack((x, y))
    rotated = R @ points
    return rotated[0, :], rotated[1, :]

# Function to map 2D label coordinates onto the curved cylinder surface
def map_points_to_cylinder(x, y, radius_x=15, radius_z=15, angle_span=np.pi):
    # Preserve vertical scaling: the y values remain unchanged.
    # For horizontal (x) values, we linearly map the range of x to an angular span.
    x_min, x_max = np.min(x), np.max(x)
    L = x_max - x_min
    # Map x to an angle (theta) in the range [0, angle_span]
    theta = ((x - x_min) / L) * angle_span

    # Use separate radii for the cylinder in the X and Z directions.
    X_mapped = radius_x * np.cos(theta)
    Z_mapped = radius_z * np.sin(theta)
    # The Y coordinate remains unchanged to preserve original vertical scaling.
    Y_mapped = y
    return X_mapped, Y_mapped, Z_mapped, theta

# Function to plot both the original (and rotated) label and the mapped label on a cylinder
def plot_label_on_cylinder(x, y, set_angle=45, radius_x=15, radius_z=15, angle_span=np.pi):
    fig = plt.figure(figsize=(16, 7))
    
    # --- Left Plot: Original and Rotated Label (2D view) ---
    ax1 = fig.add_subplot(121)
    # Plot original points
    ax1.scatter(x, y, color='red', label='Original Points')
    ax1.plot(x, y, color='red', linestyle='--', alpha=0.7)
    
    # Rotate the points by set_angle degrees
    x_rot, y_rot = rotate_points(x, y, set_angle)
    ax1.scatter(x_rot, y_rot, color='blue', label=f'Rotated Points ({set_angle}°)')
    ax1.plot(x_rot, y_rot, color='blue', linestyle='--', alpha=0.7)
    
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.set_title("Original and Rotated Label (CSV Data)")
    ax1.legend()
    
    # --- Right Plot: Rotated Label Wrapped on Cylinder (3D view) ---
    ax2 = fig.add_subplot(122, projection='3d')
    
    # Map the rotated points onto the cylinder surface.
    # Note: the vertical coordinate (y_rot) is used directly to avoid vertical stretching.
    X_mapped, Y_mapped, Z_mapped, theta = map_points_to_cylinder(x_rot, y_rot, radius_x, radius_z, angle_span)
    
    # Plot the mapped points on the cylinder
    sc = ax2.scatter(X_mapped, Y_mapped, Z_mapped, c=Y_mapped, cmap='viridis', s=50, label='Mapped Points')
    
    # Draw lines connecting the mapped points to create a continuous label appearance
    ax2.plot(X_mapped, Y_mapped, Z_mapped, color='blue', linewidth=2, label='Connected Label')
    
    # Plot a surface for the (curved) cylinder covering the angular span
    phi = np.linspace(0, angle_span, 100)
    # Use the rotated points’ vertical range for Y values on the cylinder
    Y_cyl = np.linspace(np.min(y_rot), np.max(y_rot), 100)
    PHI, Y_grid = np.meshgrid(phi, Y_cyl)
    X_cyl = radius_x * np.cos(PHI)
    Z_cyl = radius_z * np.sin(PHI)
    
    ax2.plot_surface(X_cyl, Y_grid, Z_cyl, color='gray', alpha=0.3, rstride=4, cstride=4)
    
    ax2.set_xlabel("X (Cylinder)")
    ax2.set_ylabel("Y")
    ax2.set_zlabel("Z (Cylinder)")
    ax2.set_title("Rotated Label Wrapped on Cylinder Surface")
    ax2.legend()
    fig.colorbar(sc, ax=ax2, shrink=0.5, aspect=10, label="Y")
    
    plt.tight_layout()
    plt.show()

# Main function to read CSV, rotate points, and plot the mapping.
def main():
    # Read CSV data
    x, y = read_points_from_csv('ellipse_points.csv')
    # Rotate by set_angle (e.g., 45°) and map onto cylinder without deforming vertical scaling.
    plot_label_on_cylinder(x, y, set_angle=45, radius_x=15, radius_z=15, angle_span=np.pi)

main()
