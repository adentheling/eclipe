```markdown
# Eclipe

Eclipe is a collection of Python scripts for generating, manipulating, and visualizing ellipses, spirals, and their transformations. This project includes tools that:

- Generate ellipse points and export them as CSV files.
- Visualize 2D and 3D representations using Turtle graphics, Matplotlib, Plotly, and SVG outputs.
- Map 2D ellipse points onto a cylinder.
- Create nested ellipses with scarf joint transitions.
- Provide interactive features (e.g., measuring distances on plots).

## Installation

Clone the repository:

```bash
git clone https://github.com/adentheling/eclipe.git
cd eclipe
```

## Scripts Overview

### 3dcsvplot.py
**Purpose:**  
- Reads sticker coordinates from `sticker_coordinates.csv` and creates a 3D scatter plot (with connecting lines) using Plotly.

**Usage:**

```bash
python 3dcsvplot.py
```

---

### 3dmodelwrappy.py
**Purpose:**  
- Reads ellipse points from `ellipse_points.csv`.
- Rotates the points.
- Maps them onto a cylinder (mimicking a 3D wrap).
- Exports the mapped points as `sticker_coordinates.csv`.
- Visualizes the original, rotated, and mapped points using Matplotlib (including a 3D view).

**Usage:**

```bash
python 3dmodelwrappy.py
```

---

### checkcsv.py
**Purpose:**  
- Uses Turtle graphics to draw ellipse points from `ellipse_points.csv` and applies a color gradient based on each point’s distance from the origin.

**Usage:**

```bash
python checkcsv.py
```

---

### checkcsvMATPLOT.py
**Purpose:**  
- Reads ellipse points from `ellipse_points.csv` and visualizes them using Matplotlib with a color gradient.
- Draws lines between consecutive points.
- Supports interactive distance measurement via mouse clicks.

**Usage:**

```bash
python checkcsvMATPLOT.py
```

---

### eclipgen.py
**Purpose:**  
- Generates evenly spaced points along an ellipse.
- Draws the ellipse along with dynamically scaled axes (using Turtle).
- Exports the generated points to `ellipse_points.csv`.

**Usage:**

```bash
python eclipgen.py
```

---

### in to bbox.py
**Purpose:**  
- Generates nested ellipses with scarf joints inside a bounding ellipse.
- Adjusts point density and applies a dynamic Y offset.
- Exports the ellipse points to `ellipse_points.csv`.
- Visualizes the nested ellipses using Matplotlib.

**Usage:**

```bash
python "in to bbox.py"
```

*(If your OS or shell does not allow spaces in filenames, consider renaming the file.)*

---

### main.py
**Purpose:**  
- Provides functions to calculate ellipse coordinates.
- Prints the coordinates to the console.
- Draws the ellipse points using Turtle graphics.

**Usage:**

```bash
python main.py
```

> **Note:** This script requires user input for the semi-major and semi-minor axes.

---

### out to in spiral.py
**Purpose:**  
- Generates nested ellipses starting from an outer ellipse and gradually reducing until the final transition reaches (0,0).
- Exports the inner ellipse points (excluding the outermost ellipse) to `ellipse_points.csv`.
- Visualizes the transition using Matplotlib.

**Usage:**

```bash
python "out to in spiral.py"
```

---

### spiral to SVG.py
**Purpose:**  
- Similar to the "out to in spiral" approach but designed to produce an SVG file.
- Exports ellipse points to `ellipse_points.csv` and saves the final plot as `nested_ellipses_spiral.svg`.

**Usage:**

```bash
python "spiral to SVG.py"
```

---

### spiraleclipSPACINGEQUALPOINT.py
**Purpose:**  
- Generates nested ellipses with scarf joints while enforcing equal spacing between points.
- Exports the ellipse points (excluding the bounding ellipse) to `ellipse_points.csv`.
- Visualizes the ellipses using Matplotlib.

**Usage:**

```bash
python spiraleclipSPACINGEQUALPOINT.py
```

---

