import os
import sys
from PIL import Image
from datetime import datetime
from tqdm import tqdm


def get_exif_date(image_path):
    """Extract the date taken from image EXIF data."""
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data:
                # EXIF tag 36867 is DateTimeOriginal
                date_str = exif_data.get(36867)
                if date_str:
                    return datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
    except Exception as e:
        print(f"Error reading EXIF data from {image_path}: {e}")
    # Fallback to file modification time if no EXIF data
    return datetime.fromtimestamp(os.path.getmtime(image_path))


def count_images(source_folder):
    """Count total number of image files in source folder recursively."""
    image_extensions = ('.jpg', '.jpeg', '.png', '.tiff', '.bmp')
    total = 0
    for root, _, files in os.walk(source_folder):
        total += sum(1 for filename in files if filename.lower().endswith(image_extensions))
    return total


def process_photos(source_folder, dest_folder):
    """Process all photos from source folder and organize them in destination folder."""
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    image_extensions = ('.jpg', '.jpeg', '.png', '.tiff', '.bmp')

    total_images = count_images(source_folder)
    if total_images == 0:
        print("No images found in source folder.")
        return

    with tqdm(total=total_images, desc="Processing images", unit="image") as pbar:
        for root, _, files in os.walk(source_folder):
            for filename in files:
                if filename.lower().endswith(image_extensions):
                    source_path = os.path.join(root, filename)

                    date_taken = get_exif_date(source_path)

                    year_folder = os.path.join(dest_folder, str(date_taken.year))
                    if not os.path.exists(year_folder):
                        os.makedirs(year_folder)

                    new_filename = f"{date_taken.strftime('%Y%m%d_%H%M%S')}_{filename}"
                    dest_path = os.path.join(year_folder, new_filename)

                    counter = 1
                    base_name = new_filename.rsplit('.', 1)[0]
                    extension = new_filename.rsplit('.', 1)[1] if '.' in new_filename else ''
                    while os.path.exists(dest_path):
                        new_filename = f"{base_name}_{counter}.{extension}"
                        dest_path = os.path.join(year_folder, new_filename)
                        counter += 1

                    try:
                        with open(source_path, 'rb') as src_file:
                            with open(dest_path, 'wb') as dest_file:
                                dest_file.write(src_file.read())
                        # Update progress bar with custom message
                        pbar.set_postfix(file=filename, refresh=True)
                        pbar.update(1)
                    except Exception as e:
                        print(f"Error processing {filename}: {e}")
                        pbar.update(1)  # Still update progress on error


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <source_folder> <destination_folder>")
        sys.exit(1)

    source_folder = sys.argv[1]
    dest_folder = sys.argv[2]

    if not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' does not exist")
        sys.exit(1)

    print(f"Processing photos from '{source_folder}' to '{dest_folder}'...")
    process_photos(source_folder, dest_folder)
    print("Done!")


if __name__ == "__main__":
    main()