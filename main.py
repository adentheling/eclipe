import math
import turtle

def get_ellipse_coordinates(a, b, scale_factor=10):
    num_points = max(100, int((a + b) * 10))  # Adjust points based on size
    angles = [i * (2 * math.pi / num_points) for i in range(num_points)]
    x_coords = [a * math.cos(angle) for angle in angles]
    y_coords = [b * math.sin(angle) for angle in angles]
    
    return list(zip(x_coords, y_coords))

def print_coordinates(coords):
    for x, y in coords:
        print(f"({x:.2f}, {y:.2f})")

def draw_ellipse_turtle(coords, a, b):
    screen = turtle.Screen()
    max_width = screen.window_width() - 50
    max_height = screen.window_height() - 50
    
    scale_x = max_width / (2 * a) if a * 10 > max_width else 10
    scale_y = max_height / (2 * b) if b * 10 > max_height else 10
    scale_factor = min(scale_x, scale_y)
    
    screen.setup(width=min(int(a * scale_factor * 2) + 100, max_width),
                 height=min(int(b * scale_factor * 2) + 100, max_height))
    
    turtle.speed(0)
    turtle.penup()
    for x, y in coords:
        turtle.goto(x * scale_factor, y * scale_factor)  # Dynamically scaled
        turtle.dot(3, "red")
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    a = float(input("Enter the semi-major axis length: "))
    b = float(input("Enter the semi-minor axis length: "))
    coordinates = get_ellipse_coordinates(a, b)
    print_coordinates(coordinates)
    draw_ellipse_turtle(coordinates, a, b)