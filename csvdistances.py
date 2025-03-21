import csv
import numpy as np

# Function to read CSV file and return coordinates
def read_csv(filename="sticker_coordinates.csv"):
    """
    Reads sticker coordinates from a CSV file with headers "X", "Y", "Z".
    Returns a list of (X, Y, Z) tuples.
    """
    coordinates = []
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            coordinates.append((float(row["X"]), float(row["Y"]), float(row["Z"])))
    return coordinates

# Function to calculate Euclidean distance between two points
def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

# Function to write the results into a new CSV file
def write_csv(output_filename, coordinates_with_distances):
    """
    Writes the results to a new CSV file with additional 'Distance' column.
    """
    headers = ["X", "Y", "Z", "Distance"]
    with open(output_filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(coordinates_with_distances)

def main():
    # Read the sticker coordinates from the CSV file
    coordinates = read_csv("sticker_coordinates.csv")
    
    coordinates_with_distances = []
    
    # Iterate through the coordinates and calculate distance to the next point
    for i in range(len(coordinates) - 1):
        point1 = coordinates[i]
        point2 = coordinates[i + 1]
        distance = calculate_distance(point1, point2)
        
        # Append the point coordinates and the distance to the result list
        coordinates_with_distances.append([point1[0], point1[1], point1[2], distance])
    
    # For the last point, add distance as 0 since there's no next point
    coordinates_with_distances.append([coordinates[-1][0], coordinates[-1][1], coordinates[-1][2], 0])

    # Write the results to the new CSV
    write_csv("distances_output.csv", coordinates_with_distances)

if __name__ == "__main__":
    main()
