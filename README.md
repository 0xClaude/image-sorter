# Image Sorter

A Python script to recursively sort images from a source folder into a destination folder, organizing them into year-based subfolders and renaming them based on their EXIF date taken (or file modification time if EXIF is unavailable).

## Features
- Recursively scans a source folder for image files (`.jpg`, `.jpeg`, `.png`, `.tiff`, `.bmp`).
- Extracts the date taken from EXIF data using the `Pillow` library.
- Falls back to file modification time if EXIF data is missing.
- Organizes images into subfolders by year (e.g., `2023/`, `2024/`).
- Renames files with a `YYYYMMDD_HHMMSS_originalname` format.
- Handles duplicate filenames by appending a counter (e.g., `_1`, `_2`).
- Copies files to the destination (preserves originals in the source folder).
- Displays a progress bar in the terminal showing processed and remaining images.

## Requirements
- Python 3.x
- Pillow library (`pip install Pillow`)
- tqdm library (`pip install tqdm`) for progress bar

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/0xClaude/image-sorter.git
   cd image-sorter
   ```
   
2. Install the required dependencies
   ```bash
   pip install Pillow tqdm
   ```

## Usage
Run the script from the command line, providing a source folder and a destination folder as arguments:

   ```bash
   python main.py /path/to/source/folder /path/to/destination/folder
   ```

## Example

   ```bash
   python main.py ~/Pictures/Unsorted ~/Pictures/Sorted
   ```

This will:
- Scan ~/Pictures/Unsorted for images.
- Display a progress bar showing the number of images processed and remaining.
- Create year-based subfolders in ~/Pictures/Sorted (e.g., ~/Pictures/Sorted/2023/).
- Copy and rename images like photo.jpg to 20230115_143022_photo.jpg.

## Output
The script will show a progress bar in the terminal:

   ```commandline
   Processing photos from '/home/user/Pictures/Unsorted' to '/home/user/Pictures/Sorted'...
   Processing images:  45%|████▌     | 45/100 [00:02<00:03, 18.33image/s, file=photo.jpg]
   Done!
   ```

- 45/100: Shows 45 images processed out of 100 total.
- [00:02<00:03]: Elapsed time and estimated time remaining.
-18.33image/s: Processing speed.
- file=photo.jpg: Current file being processed.

## Project Structure

   ```
   image-sorter/
   ├── main.py           # The main script
   ├── .gitignore        # Git ignore file (ignores .idea/, sorted/, etc.)
   └── README.md         # This file
   ```

## Notes
- The script copies files rather than moving them to preserve your originals. To move files instead, modify the script to use os.rename() instead of file copying.
- If an image lacks EXIF data, the file modification time is used as a fallback.
- Ensure you have write permissions in the destination folder.

## Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements!

## License
This project is licensed under the MIT License.


