# Eclipe

Eclipe is a collection of Python scripts for generating, manipulating, and visualizing ellipses, spirals, and their transformations. This project includes tools that:

- Generate ellipse points and export them as CSV files.
- Visualize 2D and 3D representations using Turtle graphics, Matplotlib, Plotly, and SVG outputs.
- Map 2D ellipse points onto a cylinder.
- Create nested ellipses with scarf joint transitions.
- Provide interactive features (e.g., measuring distances on plots).

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Scripts Overview](#scripts-overview)
  - [3dcsvplot.py](#3dcsvplotpy)
  - [3dmodelwrappy.py](#3dmodelwrappypy)
  - [checkcsv.py](#checkcsvpy)
  - [checkcsvMATPLOT.py](#checkcsvmatplotpy)
  - [csvdistances.py](#csvdistancespy)
  - [eclipgen.py](#eclipgenpy)
  - [in to bbox.py](#in-to-bboxpy)
  - [main.py](#mainpy)
  - [out to bbox.py](#out-to-bboxpy)
  - [spiral to SVG.py](#spiral-to-svgpy)
  - [spiraleclipSPACINGEQUALPOINT.py](#spiraleclipspacingequalpointpy)
- [Usage Examples](#usage-examples)

## Prerequisites

Ensure you have Python 3 installed. The scripts require the following Python libraries:
- **numpy**
- **matplotlib**
- **plotly**

Install them via pip:

```bash
pip install numpy matplotlib plotly
```

> **Note:** The built-in `turtle` and `csv` modules are included with Python.

## Installation

Clone the repository:

```bash
git clone https://github.com/adentheling/eclipe.git
cd eclipe
```

### Highly Recommended: Use Visual Studio Code (VSCode)

We highly recommend using [Visual Studio Code (VSCode)](https://code.visualstudio.com/) to develop and run these scripts. VSCode is a powerful, lightweight code editor that supports Python development with features like IntelliSense, debugging, Git integration, and extensions for Python development.

#### Steps to Set Up VSCode:

1. **Download and Install VSCode:**
   - [Download VSCode for your platform](https://code.visualstudio.com/download)
   - Follow the installation instructions for your operating system.

2. **Install Python Extension:**
   - Open VSCode.
   - Go to the Extensions view (`Ctrl+Shift+X`), search for `Python`, and install the extension provided by Microsoft.

3. **Open the Project in VSCode:**
   - In VSCode, go to `File > Open Folder` and select the `eclipe` folder you cloned.
   
4. **Install Python in VSCode:**
   - Open the terminal in VSCode (`Ctrl+` `), then run the following command to install necessary dependencies:
     ```bash
     pip install numpy matplotlib plotly
     ```
   
5. **Run the Scripts:**
   - Open any Python script in VSCode and click the green play button (`Run`) in the top-right corner to run the script.

For more details on how to get started with VSCode, check out the [official documentation](https://code.visualstudio.com/docs/python/python-tutorial).

## Scripts Overview

### 3dcsvplot.py
- **Purpose:** Reads sticker coordinates from `sticker_coordinates.csv` and creates a 3D scatter plot (with connecting lines) using Plotly.
- **Usage:**  
  ```bash
  python 3dcsvplot.py
  ```

### 3dmodelwrappy.py
- **Purpose:** 
  - Reads ellipse points from `ellipse_points.csv`.
  - Rotates the points.
  - Maps them onto a cylinder (mimicking a 3D wrap).
  - Exports the mapped points as `sticker_coordinates.csv`.
  - Visualizes the original, rotated, and mapped points using Matplotlib (including a 3D view).
- **Usage:**  
  ```bash
  python 3dmodelwrappy.py
  ```

### checkcsv.py
- **Purpose:** Uses Turtle graphics to draw ellipse points from `ellipse_points.csv` and applies a color gradient based on each point’s distance from the origin.
- **Usage:**  
  ```bash
  python checkcsv.py
  ```

### checkcsvMATPLOT.py
- **Purpose:** Reads ellipse points from `ellipse_points.csv` and visualizes them using Matplotlib with a color gradient. It also draws lines between consecutive points and supports interactive distance measurement via mouse clicks.
- **Usage:**  
  ```bash
  python checkcsvMATPLOT.py
  ```

### csvdistances.py
- **Purpose:** 
  - Reads 3D sticker coordinates from a CSV file (e.g., `sticker_coordinates.csv`).
  - Calculates the Euclidean distance between each consecutive pair of points.
  - Appends the distance to the same row in the new CSV file.
  - Exports the new CSV with coordinates and their respective distances.
- **Usage:**  
  ```bash
  python csvdistances.py
  ```

### eclipgen.py
- **Purpose:** 
  - Generates evenly spaced points along an ellipse.
  - Draws the ellipse along with dynamically scaled axes (using Turtle).
  - Exports the generated points to `ellipse_points.csv`.
- **Usage:**  
  ```bash
  python eclipgen.py
  ```

### in to bbox.py
- **Purpose:** 
  - Generates nested ellipses with scarf joints inside a bounding ellipse.
  - Adjusts point density and applies a dynamic Y offset.
  - Exports the ellipse points to `ellipse_points.csv`.
  - Visualizes the nested ellipses using Matplotlib.
- **Usage:**  
  ```bash
  python "in to bbox.py"
  ```
  *(If your OS or shell does not allow spaces in filenames, consider renaming the file.)*

### main.py
- **Purpose:** 
  - Provides functions to calculate ellipse coordinates.
  - Prints the coordinates to the console.
  - Draws the ellipse points using plotly graphics.
- **Usage:**  
  ```bash
  python main.py
  ```
  > **Note:** This script requires user input in each code

### out to bbox.py
- **Purpose:** 
  - Generates nested ellipses starting from an outer ellipse and gradually reducing until the final transition reaches (0,0).
  - Exports the inner ellipse points (excluding the outermost ellipse) to `ellipse_points.csv`.
  - Visualizes the transition using Matplotlib.
- **Usage:**  
  ```bash
  python "out to bbox.py"
  ```

### spiral to SVG.py
- **Purpose:** 
  - Similar to the "out to in spiral" approach but designed to produce an SVG file.
  - Exports ellipse points to `ellipse_points.csv` and saves the final plot as `nested_ellipses_spiral.svg`.
- **Usage:**  
  ```bash
  python "spiral to SVG.py"
  ```

### spiraleclipSPACINGEQUALPOINT.py
- **Purpose:** 
  - Generates nested ellipses with scarf joints while enforcing equal spacing between points.
  - Exports the ellipse points (excluding the bounding ellipse) to `ellipse_points.csv`.
  - Visualizes the ellipses using Matplotlib.
- **Usage:**  
  ```bash
  python spiraleclipSPACINGEQUALPOINT.py
  ```

## Usage Examples

1. **Generating Ellipse Points and Visualizing with Turtle**  
   Run the ellipse generator to create points and see them drawn:
   ```bash
   python eclipgen.py
   ```

2. **Mapping 2D Points to a 3D Cylinder**  
   After generating `ellipse_points.csv`, map them onto a cylinder:
   ```bash
   python 3dmodelwrappy.py
   ```

3. **Visualizing with Plotly in 3D**  
   Use the exported `sticker_coordinates.csv` to create a 3D plot:
   ```bash
   python 3dcsvplot.py
   ```

4. **Interactive 2D Plot with Matplotlib**  
   Visualize the ellipse points with interactive distance measurement:
   ```bash
   python checkcsvMATPLOT.py
   ```

5. **Calculating Distances Between Points**  
   Calculate the distances between each consecutive point and save the results in a new CSV:
   ```bash
   python csvdistances.py
   ```

6. **Creating Nested Ellipses with Scarf Joints**  
   Generate and view nested ellipses, then export the points:
   - For an "in to bounding" version:  
     ```bash
     python "in to bbox.py"
     ```
   - For an "outer to inner spiral" version:  
     ```bash
     python "out to in spiral.py"
     ```
   - For generating an SVG output:  
     ```bash
     python "spiral to SVG.py"
     ```
   - For equal spacing between points in nested ellipses:  
     ```bash
     python spiraleclipSPACINGEQUALPOINT.py
     ```
