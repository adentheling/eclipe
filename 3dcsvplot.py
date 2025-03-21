import csv
import plotly.graph_objects as go

def read_csv(filename="sticker_coordinates.csv"):
    """
    Reads sticker coordinates from a CSV file with headers "X", "Y", "Z".
    Returns three lists: x_vals, y_vals, z_vals.
    """
    x_vals, y_vals, z_vals = [], [], []
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            x_vals.append(float(row["X"]))
            y_vals.append(float(row["Y"]))
            z_vals.append(float(row["Z"]))
    return x_vals, y_vals, z_vals

def main():
    # Read the sticker coordinates from the CSV file.
    x, y, z = read_csv("sticker_coordinates.csv")
    
    # Create a 3D scatter plot with lines connecting the points.
    fig = go.Figure(data=[go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='lines+markers',      # Show both markers and a line connecting them
        line=dict(color='blue', width=3),
        marker=dict(size=5, color='red')
    )])
    
    # Update the layout for clarity.
    fig.update_layout(
        title="3D Sticker Coordinates",
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z",
            aspectmode='data'  # This makes all axes have the same scale.
        )
    )
    
    # Display the figure in your default web browser.
    fig.show()

if __name__ == "__main__":
    main()
