import os
import glob

files = glob.glob(r'Z:\Music\Artist\**\*.mp3', recursive=True)

for item in files:
    try:
        name, extension = os.path.splitext(item)
        directory = os.path.dirname(item)
        filename = os.path.basename(name)

        if "01-" in filename:
            trimmed_name = filename.split("01-")[1] + extension
            new_path = os.path.join(directory, trimmed_name)
            print(new_path)
            os.rename(item, new_path)


    except PermissionError:
        continue