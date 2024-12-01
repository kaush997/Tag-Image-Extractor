import os
import shutil

# Define paths
base_path = "data/project-7-at-2024-11-28-20-06-811bd479/Topic"
level1_folder = os.path.join(base_path, "Topic-Level1")
level2_folder = os.path.join(base_path, "Topic-Level2")
level3_folder = os.path.join(base_path, "Topic-Level3")

# Create directories if they don't exist
os.makedirs(level1_folder, exist_ok=True)
os.makedirs(level2_folder, exist_ok=True)
os.makedirs(level3_folder, exist_ok=True)

# Loop through all files in the base path
for file_name in os.listdir(base_path):
    if file_name.endswith(".png"):
        file_path = os.path.join(base_path, file_name)

        # Check for "level1" at the end of the filename and move the file
        if "Level1" in file_name.split('-')[-2]:
            shutil.move(file_path, level1_folder)

        # Check for "level2" at the end of the filename and move the file
        elif "Level2" in file_name.split('-')[-2]:
            shutil.move(file_path, level2_folder)

        # Check for "level3" at the end of the filename and move the file
        elif "Level3" in file_name.split('-')[-2]:
            shutil.move(file_path, level3_folder)

print("Files have been successfully organized.")
