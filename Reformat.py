import os
import glob
import subprocess

files = glob.glob(r"Z:\Music\Artist\Sabrina Carpenter\Man's Best Friend\*.flac", recursive=True)
count = 1

for item in files:
    try:
        name, extension = os.path.splitext(item)
        directory = os.path.dirname(item)
        filename = os.path.basename(name)
        formatted_count = str(count).zfill(2)

        if formatted_count in filename:
            trimmed_name = filename.split(formatted_count + " - Sabrina Carpenter - ")[1] + extension
            new_path = os.path.join(directory, trimmed_name)

            os.rename(item, new_path)
            item = new_path

        count += 1
        print(f"count={formatted_count}, filename={filename}")

        output_file = os.path.splitext(item)[0] + ".mp3"

        command_list = [
            "ffmpeg",
            "-i", item,
            "-c:a", "libmp3lame",
            "-b:a", "96k",
            "-map_metadata", "0",
            output_file
        ]

        subprocess.run(command_list, check=True)

        print("FFmpeg command executed successfully.")

    except PermissionError:
        continue