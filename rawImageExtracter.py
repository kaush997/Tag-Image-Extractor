import os
import shutil

# Paths to raw images and annotation directories
raw_data_path = 'raw_data'  # Replace with actual path
annotations_base_path = 'data/project-7-at-2024-11-28-20-06-811bd479'  # Replace with actual path


# Create a mapping for task number to image file
def task_to_image(task_number):
    doc_number = int(task_number) - 30
    return f"Doc_{doc_number}.jpg"


# Iterate over each annotation folder
for folder in os.listdir(annotations_base_path):
    folder_path = os.path.join(annotations_base_path, folder)
    if not os.path.isdir(folder_path):
        continue

    # Create the Image folder inside each annotation folder
    image_folder = os.path.join(folder_path, 'Image')
    os.makedirs(image_folder, exist_ok=True)

    # Set to track already copied images
    copied_images = set()

    # Iterate through annotation files
    for annotation_file in os.listdir(folder_path):
        if not annotation_file.startswith("task-") or not annotation_file.endswith(".png"):
            continue

        # Extract task number from the file name
        task_number = annotation_file.split('-')[1]
        image_file = task_to_image(task_number)

        if image_file in copied_images:
            continue  # Skip if already copied

        source_image_path = os.path.join(raw_data_path, image_file)
        if os.path.exists(source_image_path):
            destination_image_path = os.path.join(image_folder, image_file)
            shutil.copy(source_image_path, destination_image_path)
            copied_images.add(image_file)

print("Images have been organized successfully.")
