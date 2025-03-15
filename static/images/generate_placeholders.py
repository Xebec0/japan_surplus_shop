import os
from PIL import Image, ImageDraw, ImageFont
import random

# Create directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

# Colors
ORANGE = (249, 115, 22)  # #f97316
DARK_BLUE = (15, 23, 42)  # #0f172a
WHITE = (255, 255, 255)
LIGHT_GRAY = (248, 250, 252)  # #f8fafc

def create_product_placeholder(filename, size=(600, 600), category=None):
    """Create a product placeholder image with Japan Surplus branding"""
    img = Image.new('RGB', size, LIGHT_GRAY)
    draw = ImageDraw.Draw(img)
    
    # Draw grid pattern
    grid_size = 30
    for x in range(0, size[0], grid_size):
        draw.line([(x, 0), (x, size[1])], fill=ORANGE, width=1)
    for y in range(0, size[1], grid_size):
        draw.line([(0, y), (size[0], y)], fill=ORANGE, width=1)
    
    # Draw category icon if specified
    if category:
        draw_category_icon(draw, size, category)
    
    # Draw logo
    logo_radius = min(size) // 5
    logo_position = (size[0] // 2, int(size[1] * 0.85))
    
    # Logo background
    draw.ellipse(
        [
            (logo_position[0] - logo_radius, logo_position[1] - logo_radius),
            (logo_position[0] + logo_radius, logo_position[1] + logo_radius)
        ],
        fill=(255, 255, 255, 230)
    )
    
    # Logo text
    try:
        # Try to use a nice font if available
        font = ImageFont.truetype("arial.ttf", size=logo_radius // 3)
    except IOError:
        # Fallback to default font
        font = ImageFont.load_default()
    
    draw.text(
        (logo_position[0], logo_position[1] - logo_radius // 5),
        "JAPAN",
        font=font,
        fill=ORANGE,
        anchor="mm"
    )
    
    draw.text(
        (logo_position[0], logo_position[1] + logo_radius // 5),
        "SURPLUS",
        font=font,
        fill=ORANGE,
        anchor="mm"
    )
    
    # Save the image
    img.save(f"static/images/{filename}")
    print(f"Created {filename}")

def draw_category_icon(draw, size, category):
    """Draw a category-specific icon"""
    center_x = size[0] // 2
    center_y = size[1] // 2
    icon_size = min(size) // 3
    
    if category == "electronics":
        # Draw a TV/monitor
        draw.rectangle(
            [
                (center_x - icon_size//2, center_y - icon_size//2),
                (center_x + icon_size//2, center_y + icon_size//5)
            ],
            fill=DARK_BLUE
        )
        
        # Stand
        draw.rectangle(
            [
                (center_x - icon_size//4, center_y + icon_size//5),
                (center_x + icon_size//4, center_y + icon_size//3)
            ],
            fill=DARK_BLUE
        )
        
        # Screen
        draw.rectangle(
            [
                (center_x - icon_size//2 + 10, center_y - icon_size//2 + 10),
                (center_x + icon_size//2 - 10, center_y + icon_size//5 - 10)
            ],
            fill=LIGHT_GRAY
        )
    
    elif category == "furniture":
        # Draw a chair
        # Seat
        draw.rectangle(
            [
                (center_x - icon_size//2, center_y),
                (center_x + icon_size//2, center_y + icon_size//4)
            ],
            fill=DARK_BLUE
        )
        
        # Back
        draw.rectangle(
            [
                (center_x - icon_size//2, center_y - icon_size//2),
                (center_x - icon_size//3, center_y)
            ],
            fill=DARK_BLUE
        )
        
        # Legs
        draw.rectangle(
            [
                (center_x - icon_size//2, center_y + icon_size//4),
                (center_x - icon_size//2 + 10, center_y + icon_size//2)
            ],
            fill=DARK_BLUE
        )
        
        draw.rectangle(
            [
                (center_x + icon_size//2 - 10, center_y + icon_size//4),
                (center_x + icon_size//2, center_y + icon_size//2)
            ],
            fill=DARK_BLUE
        )
    
    elif category == "kitchenware":
        # Draw a pot
        # Pot body
        draw.rectangle(
            [
                (center_x - icon_size//2, center_y - icon_size//4),
                (center_x + icon_size//2, center_y + icon_size//4)
            ],
            fill=DARK_BLUE
        )
        
        # Handles
        draw.rectangle(
            [
                (center_x - icon_size//2 - icon_size//6, center_y),
                (center_x - icon_size//2, center_y + icon_size//10)
            ],
            fill=DARK_BLUE
        )
        
        draw.rectangle(
            [
                (center_x + icon_size//2, center_y),
                (center_x + icon_size//2 + icon_size//6, center_y + icon_size//10)
            ],
            fill=DARK_BLUE
        )
        
        # Lid
        draw.arc(
            [
                (center_x - icon_size//2, center_y - icon_size//2),
                (center_x + icon_size//2, center_y - icon_size//4)
            ],
            180, 0,
            fill=DARK_BLUE,
            width=icon_size//10
        )
    
    elif category == "fashion":
        # Draw a t-shirt (simplified)
        points = [
            (center_x - icon_size//2, center_y - icon_size//3),  # Left shoulder
            (center_x - icon_size//2 - icon_size//4, center_y),  # Left sleeve
            (center_x - icon_size//2, center_y),                # Left side
            (center_x - icon_size//2, center_y + icon_size//2),  # Bottom left
            (center_x + icon_size//2, center_y + icon_size//2),  # Bottom right
            (center_x + icon_size//2, center_y),                # Right side
            (center_x + icon_size//2 + icon_size//4, center_y),  # Right sleeve
            (center_x + icon_size//2, center_y - icon_size//3),  # Right shoulder
            (center_x + icon_size//4, center_y - icon_size//2),  # Neck right
            (center_x - icon_size//4, center_y - icon_size//2),  # Neck left
        ]
        draw.polygon(points, fill=DARK_BLUE)

def create_banner_placeholder(filename, size=(1200, 400)):
    """Create a banner placeholder with Japan Surplus branding"""
    img = Image.new('RGB', size, ORANGE)
    draw = ImageDraw.Draw(img)
    
    # Draw diagonal stripes
    stripe_gap = 30
    for i in range(-size[1], size[0] + size[1], stripe_gap):
        draw.line([(i, 0), (i + size[1], size[1])], fill=(255, 255, 255, 30), width=3)
    
    # Draw text
    try:
        # Try to use a nice font if available
        title_font = ImageFont.truetype("arial.ttf", size=60)
        subtitle_font = ImageFont.truetype("arial.ttf", size=30)
    except IOError:
        # Fallback to default font
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    draw.text(
        (size[0]//2, size[1]//2 - 30),
        "JAPAN SURPLUS SHOP",
        font=title_font,
        fill=WHITE,
        anchor="mm"
    )
    
    draw.text(
        (size[0]//2, size[1]//2 + 30),
        "Quality Japanese Products at Affordable Prices",
        font=subtitle_font,
        fill=WHITE,
        anchor="mm"
    )
    
    # Save the image
    img.save(f"static/images/{filename}")
    print(f"Created {filename}")

def create_about_banner(filename, size=(1200, 600)):
    """Create an about page banner"""
    img = Image.new('RGB', size, DARK_BLUE)
    draw = ImageDraw.Draw(img)
    
    # Draw wave pattern
    wave_height = 20
    wave_length = 40
    
    for y in range(0, size[1], 60):
        points = []
        for x in range(0, size[0], 5):
            y_offset = wave_height * (0.5 + 0.5 * (x / wave_length) % 1)
            points.append((x, y + y_offset))
        
        if points:
            draw.line(points, fill=(255, 255, 255, 50), width=3)
    
    # Semi-transparent overlay
    overlay = Image.new('RGBA', size, (0, 0, 0, 128))
    img = Image.alpha_composite(img.convert('RGBA'), overlay)
    
    # Draw text
    draw = ImageDraw.Draw(img)
    
    try:
        # Try to use a nice font if available
        title_font = ImageFont.truetype("arial.ttf", size=70)
        subtitle_font = ImageFont.truetype("arial.ttf", size=30)
    except IOError:
        # Fallback to default font
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
    
    draw.text(
        (size[0]//2, size[1]//2 - 40),
        "About Us",
        font=title_font,
        fill=WHITE,
        anchor="mm"
    )
    
    draw.text(
        (size[0]//2, size[1]//2 + 40),
        "Our Story, Values & Mission",
        font=subtitle_font,
        fill=WHITE,
        anchor="mm"
    )
    
    # Save the image
    img.convert('RGB').save(f"static/images/{filename}")
    print(f"Created {filename}")

# Generate product placeholders
categories = ["electronics", "furniture", "kitchenware", "fashion"]
for i in range(1, 5):
    create_product_placeholder(
        f"product-placeholder-{i}.jpg", 
        category=categories[i-1]
    )

# Generate additional generic product placeholders
for i in range(5, 13):
    create_product_placeholder(
        f"product-placeholder-{i}.jpg",
        category=random.choice(categories)
    )

# Generate banner placeholders
create_banner_placeholder("banner-placeholder-1.jpg")
create_about_banner("about-banner.jpg")

print("All placeholder images have been generated in the static/images directory.") 