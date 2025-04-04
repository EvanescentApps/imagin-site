import os
import subprocess
import glob
import logging
from PIL import Image

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def compress_image(input_path, output_path, quality=60):
    """Compresses a JPG or JPEG image using PIL."""
    try:
        logging.info(f"Compressing image: {input_path} to {output_path} with quality {quality}")
        image = Image.open(input_path)
        image.save(output_path, "JPEG", optimize=True, quality=quality)
        logging.info(f"Successfully compressed image: {input_path} -> {output_path}")
    except FileNotFoundError:
        logging.error(f"File not found: {input_path}")
    except Exception as e:
        logging.error(f"Error compressing {input_path}: {e}")


def compress_files_in_folder(folder_path, image_quality=60, video_crf=28):
    """Compresses all JPG, JPEG, and MP4 files in a folder."""
    
    image_extensions = ['*.jpg', '*.jpeg']
    video_extension = ['*.mp4']

    logging.info(f"Starting compression in folder: {folder_path}")

    for ext in image_extensions:
        for filepath in glob.glob(os.path.join(folder_path, ext)):
            output_filepath = os.path.splitext(filepath)[0] + '_compressed' + os.path.splitext(filepath)[1]
            compress_image(filepath, output_filepath, image_quality)
    
    logging.info(f"Compression complete for folder: {folder_path}")

if __name__ == "__main__":
    # Get the directory of the current script
    folder_to_compress = os.path.dirname(os.path.abspath(__file__))
    logging.info(f"Compressing files in the same directory as the script: {folder_to_compress}")
    compress_files_in_folder(folder_to_compress)
    logging.info("Compression process finished.")