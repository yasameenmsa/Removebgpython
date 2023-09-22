import os
import sys
from rembg import remove

def remove_background(input_path, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # List all the PNG files in the input directory
    png_files = [f for f in os.listdir(input_path) if f.lower().endswith(".png")]

    for png_file in png_files:
        input_file_path = os.path.join(input_path, png_file)
        output_file_path = os.path.join(output_dir, png_file)

        # Remove the background and save the result
        with open(input_file_path, "rb") as input_file, open(output_file_path, "wb") as output_file:
            output_file.write(remove(input_file.read()))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_background.py input_path output_dir")
        sys.exit(1)

    input_path = sys.argv[1]
    output_dir = sys.argv[2]

    remove_background(input_path, output_dir)
    print("Background removal completed. Images saved to", output_dir)
