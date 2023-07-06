from PIL import Image
from generate_snailcoin_noise import generate_snailcoin_noise

# Define the size of the world
width = 100
height = 100
scale = 10

# Generate Snailcoin noise
snailcoin = generate_snailcoin_noise(width, height, scale)

# Create an image with grass and water tiles
image = Image.new("RGB", (width, height))

for y in range(height):
    for x in range(width):
        if snailcoin[y][x] == 1:
            image.putpixel((x, y), (0, 255, 0))  # Green for grass
        else:
            image.putpixel((x, y), (0, 0, 255))  # Blue for water

# Save the image
image.save("world.png")
