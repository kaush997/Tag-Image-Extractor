import os
import shutil

# Define the source folder containing the images
source_folder = "data/project-7-at-2024-11-28-20-06-811bd479"  # Update with your image folder path

# Ensure the destination folder structure is created
os.makedirs(source_folder, exist_ok=True)

# Loop through all PNG files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".png"):
        # Split the filename using 'tag-' to isolate the tag part
        parts = filename.split("tag-")
        if len(parts) > 1:
            tag_part = parts[1].split("-")[0]  # Extract the tag (e.g., Header, Font, etc.)
            tag_part = tag_part.strip()
            print(tag_part)
            print(filename)

            # Create a folder for the tag if it doesn't exist
            tag_folder = os.path.join(source_folder, tag_part)
            os.makedirs(tag_folder, exist_ok=True)

            # Move the image to the corresponding tag folder
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(tag_folder, filename)
            shutil.move(source_path, destination_path)

print("Files have been sorted into their respective folders.")
