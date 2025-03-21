import numpy as np
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------
# 1. Read CSV Data
# -------------------------------
def read_points_from_csv(filename="ellipse_points.csv"):
    """
    Reads CSV data with header "X,Y" and returns numpy arrays for x and y.
    """
    xs, ys = [], []
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            xs.append(float(row[0]))
            ys.append(float(row[1]))
    return np.array(xs), np.array(ys)

# -------------------------------
# 2. Optional Rotation of Points
# -------------------------------
def rotate_points(x, y, theta_degrees):
    """
    Rotates the 2D points (x, y) about the origin by theta_degrees.
    Returns the rotated coordinates.
    """
    theta = np.radians(theta_degrees)  # Convert degrees to radians
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    x_rot = x * cos_t - y * sin_t
    y_rot = x * sin_t + y * cos_t
    return x_rot, y_rot

# -------------------------------
# 3. Map Flat Points onto a Cylinder (Sticker Mapping)
# -------------------------------
def map_points_to_cylinder(x, y, cylinder_radius=20):
    """
    Maps the rotated flat (x,y) points onto a cylinder of constant radius.
    
    For each point:
      - Compute the horizontal offset dx from the image center:
            dx = x - center_x, where center_x = (max(x) + min(x)) / 2.
      - Convert dx to an angle: theta = dx / cylinder_radius  (in radians).
      - Compute new coordinates on the cylinder:
            new_x = cylinder_radius * sin(theta)
            new_z = cylinder_radius * cos(theta)
      - The Y coordinate remains unchanged.
    """
    # Determine the center of the flat image in the x direction.
    center_x = (np.min(x) + np.max(x)) / 2.0
    dx = x - center_x  # Horizontal offset from the center
    theta = dx / cylinder_radius  # Angle in radians corresponding to the offset
    new_x = cylinder_radius * np.sin(theta)
    new_z = cylinder_radius * np.cos(theta)
    new_y = y.copy()  # Y remains unchanged
    return new_x, new_y, new_z

# -------------------------------
# 4. Set 3D Axes to Equal Scale
# -------------------------------
def set_axes_equal(ax):
    """
    Sets 3D plot axes to equal scale so that the cylinder is not distorted.
    This is a common workaround since matplotlib does not support equal aspect ratio
    for 3D plots directly.
    """
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()
    
    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)
    
    # The plot bounding box is a sphere in order to get equal aspect.
    plot_radius = 0.5 * max([x_range, y_range, z_range])
    
    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

# -------------------------------
# 5. Plotting the Data
# -------------------------------
def plot_mapping(original_x, original_y, rotated_x, rotated_y, mapped_x, mapped_y, mapped_z, cylinder_radius):
    """
    Creates three subplots:
      A. Original 2D points.
      B. Rotated 2D points.
      C. 3D view of the mapped (sticker) points on a cylinder.
    Also draws the cylinder (of constant radius) for reference.
    """
    fig = plt.figure(figsize=(18, 6))
    
    # Subplot A: Original 2D Points
    ax1 = fig.add_subplot(131)
    ax1.scatter(original_x, original_y, color='red', label="Original Points")
    ax1.set_title("Original 2D Points")
    ax1.set_xlabel("X")
    ax1.set_ylabel("Y")
    ax1.axis("equal")
    ax1.legend()
    
    # Subplot B: Rotated 2D Points
    ax2 = fig.add_subplot(132)
    ax2.scatter(rotated_x, rotated_y, color='blue', label="Rotated Points")
    ax2.set_title("Rotated 2D Points")
    ax2.set_xlabel("X")
    ax2.set_ylabel("Y")
    ax2.axis("equal")
    ax2.legend()
    
    # Subplot C: 3D Mapping on Cylinder
    ax3 = fig.add_subplot(133, projection='3d')
    
    # Draw the full cylinder (constant radius) for reference.
    phi = np.linspace(0, 2 * np.pi, 200)
    # Use a Y range that covers the mapped points.
    y_range = np.linspace(np.min(mapped_y) - 1, np.max(mapped_y) + 1, 50)
    PHI, Y_surf = np.meshgrid(phi, y_range)
    X_surf = cylinder_radius * np.cos(PHI)
    Z_surf = cylinder_radius * np.sin(PHI)
    ax3.plot_surface(X_surf, Y_surf, Z_surf, color='gray', alpha=0.2)
    
    # Plot the mapped (sticker) points on the cylinder.
    sc = ax3.scatter(mapped_x, mapped_y, mapped_z, c=mapped_y, cmap="viridis", s=50, label="Mapped Points")
    ax3.set_title("Sticker Mapped onto Cylinder")
    ax3.set_xlabel("X (Cylinder)")
    ax3.set_ylabel("Y (Height)")
    ax3.set_zlabel("Z (Cylinder)")
    ax3.legend()
    
    # Set equal scale for all axes in the 3D plot.
    set_axes_equal(ax3)
    
    plt.show()

# -------------------------------
# 6. Main Function
# -------------------------------
def main():
    # Load CSV data.
    original_x, original_y = read_points_from_csv("ellipse_points.csv")
    
    # User-defined parameters:
    rotation_angle_degrees = 30    # Rotation angle to apply before mapping (set to 0 for no rotation)
    cylinder_radius = 90           # Constant cylinder radius
    
    # Step 1: Optionally rotate the flat image.
    rotated_x, rotated_y = rotate_points(original_x, original_y, rotation_angle_degrees)
    
    # Step 2: Map the rotated flat image onto the cylinder.
    mapped_x, mapped_y, mapped_z = map_points_to_cylinder(rotated_x, rotated_y, cylinder_radius=cylinder_radius)
    
    # Step 3: Plot the original, rotated, and cylinder-mapped points.
    plot_mapping(original_x, original_y, rotated_x, rotated_y, mapped_x, mapped_y, mapped_z, cylinder_radius)

if __name__ == "__main__":
    main()
