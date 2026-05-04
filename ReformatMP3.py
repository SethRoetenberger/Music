import os 
import glob 
import subprocess 
import shlex 

files = glob.glob(r'Z:\Music\Artist\Borns\**\*.mp3', recursive=True) 
count = 1 

for item in files: 
    try: 
        name, extension = os.path.splitext(item) 
        directory = os.path.dirname(item) 
        filename = os.path.basename(name) 
        formatted_count = str(count).zfill(2) 

        if formatted_count + " - Halsey - " in filename: 
            trimmed_name = filename.split(formatted_count + " - Halsey - ")[1] + extension 
            new_path = os.path.join(directory, trimmed_name) 
            print(new_path) 
            os.rename(item, new_path) 
        count += 1 
        print(f"count={formatted_count}, filename={filename}") 
        
        temp_file = item + ".tmp.mp3"

        command_list = [ "ffmpeg", "-i", item, "-c", "copy", "-map_metadata", "0", temp_file ] 
        
        subprocess.run(command_list, check=True) 
        os.replace(temp_file, item) 
        print("FFmpeg command executed successfully.") 
        
    except PermissionError: 
        continue