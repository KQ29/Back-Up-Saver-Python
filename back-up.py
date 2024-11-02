import os
import shutil
import datetime
import schedule
import time

# Paths to the source and destination folders
source_dir = ""
destination_dir = ""

# Check if folders exist
if not os.path.exists(source_dir):
    raise Exception(f"Source folder '{source_dir}' not found.")
if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)  # Creates the folder if it doesn't exist

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"[{datetime.datetime.now()}] Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"[{datetime.datetime.now()}] Folder already exists in: {dest}")
    except Exception as e:
        print(f"[{datetime.datetime.now()}] Error during copy: {e}")

# Set the scheduled time for copying
scheduled_time = "20:50"
schedule.every().day.at(scheduled_time).do(lambda: copy_folder_to_directory(source_dir, destination_dir))

print(f"Scheduled to copy every day at {scheduled_time}.")

while True:
    schedule.run_pending()
    time.sleep(60)
