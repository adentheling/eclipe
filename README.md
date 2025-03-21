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
  - [eclipgen.py](#eclipgenpy)
  - [in to bbox.py](#in-to-bboxpy)
  - [main.py](#mainpy)
  - [out to in spiral.py](#out-to-in-spiralpy)
  - [spiral to SVG.py](#spiral-to-svgpy)
  - [spiraleclipSPACINGEQUALPOINT.py](#spiraleclipspacingequalpointpy)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Ensure you have Python 3 installed. The scripts require the following Python libraries:
- **numpy**
- **matplotlib**
- **plotly**

Install them via pip:

```bash
pip install numpy matplotlib plotly
