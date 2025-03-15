from PIL import Image, ImageDraw, ImageFont
import os

# Create directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

# Colors
ORANGE = (249, 115, 22)  # #f97316
DARK_BLUE = (15, 23, 42)  # #0f172a
WHITE = (255, 255, 255)
LIGHT_GRAY = (248, 250, 252)  # #f8fafc

def create_user_placeholder(filename, size=(200, 200)):
    """Create a user placeholder image with Japan Surplus branding"""
    # Create a new image with a white background
    img = Image.new('RGB', size, LIGHT_GRAY)
    draw = ImageDraw.Draw(img)
    
    # Draw a circle for the user avatar
    circle_radius = min(size) // 2 - 10
    circle_center = (size[0] // 2, size[1] // 2)
    
    # Draw the circle
    draw.ellipse(
        [
            (circle_center[0] - circle_radius, circle_center[1] - circle_radius),
            (circle_center[0] + circle_radius, circle_center[1] + circle_radius)
        ],
        fill=ORANGE
    )
    
    # Draw a person silhouette
    # Head
    head_radius = circle_radius // 3
    head_center = (circle_center[0], circle_center[1] - head_radius // 2)
    draw.ellipse(
        [
            (head_center[0] - head_radius, head_center[1] - head_radius),
            (head_center[0] + head_radius, head_center[1] + head_radius)
        ],
        fill=WHITE
    )
    
    # Body
    body_width = circle_radius
    body_height = circle_radius
    body_top = head_center[1] + head_radius
    draw.ellipse(
        [
            (circle_center[0] - body_width // 2, body_top),
            (circle_center[0] + body_width // 2, body_top + body_height)
        ],
        fill=WHITE
    )
    
    # Save the image
    img.save(f"static/images/{filename}")
    print(f"Created {filename}")

# Generate user placeholder
create_user_placeholder("user-placeholder.jpg")

print("User placeholder image has been generated in the static/images directory.") 