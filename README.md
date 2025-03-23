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

## Requirements

- Python 3.x
- Pillow library (`pip install Pillow`)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/0xClaude/image-sorter.git
   ```
   
2. Install the required dependency:
   ```bash
   pip install Pillow
   ```

## Usage

Run the script from the command line, providing a source folder and a destination folder as arguments:

   ```bash
   python3 main.py /path/to/source/folder /path/to/destination/folder
   ``` 

## Example

   ```bash
   python3 main.py ~/Pictures/Unsorted ~/Pictures/Sorted
   ```

This will:
- Scan ~/Pictures/Unsorted for images.
- Create year-based subfolders in ~/Pictures/Sorted (e.g., ~/Pictures/Sorted/2023/).
- Copy and rename images like photo.jpg to 20230115_143022_photo.jpg.

## Output

The script will print progress messages:
```commandline
Processing photos from '/home/user/Pictures/Unsorted' to '/home/user/Pictures/Sorted'...
Processed: photo.jpg -> /home/user/Pictures/Sorted/2023/20230115_143022_photo.jpg
Done!
```

## Project structure

```commandline
image-sorter/
├── main.py           # The main script
├── .gitignore        # Git ignore file (ignores .idea/, sorted/, etc.)
└── README.md         # This file
```

## Notes

The script copies files rather than moving them to preserve your originals. To move files instead, modify the script to use os.rename() instead of file copying.

If an image lacks EXIF data, the file modification time is used as a fallback.

Ensure you have write permissions in the destination folder.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements!

## License
This project is licensed under the MIT License.

