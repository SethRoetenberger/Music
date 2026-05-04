import os
import glob
import subprocess

files = glob.glob(r'Z:\Music\Artist\Sabrina Carpenter\**\*.mp3', recursive=True)
#files = glob.glob(r'E:\Artist\**\*.mp3', recursive=True)

current_directory = None
count = 1

for item in files:
    try:

        directory = os.path.dirname(item)

        # Reset count when entering a new folder
        if directory != current_directory:
            current_directory = directory
            count = 1

        name, extension = os.path.splitext(item)
        directory = os.path.dirname(item)
        filename = os.path.basename(name)
        formatted_count = str(count).zfill(2)

        if formatted_count in filename:
            trimmed_name = filename.split(formatted_count + " - Sabrina Carpenter - ")[1] + extension
            new_path = os.path.join(directory, trimmed_name)
            print(new_path)
            os.rename(item, new_path)

        count += 1
        print(f"count={formatted_count}, filename={filename}")

    except PermissionError:
        continue