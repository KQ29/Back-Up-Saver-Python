# Back-Up-Saver-Python

## Daily Folder Backup Script

This script automates the process of copying files from a source folder to a destination folder on a daily schedule. It uses the `schedule` library to run the task at a specified time each day.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Features

- Copies a specified source folder to a destination folder daily.
- Creates a new folder for each day, named with the current date.
- Logs each copy action with timestamps for easy tracking.
- Verifies that the source folder exists and creates the destination folder if needed.

## Requirements

- Python 3.x
- Required Python packages (listed below)

## Setup

### Clone or Download the Repository

```bash
git clone <your-repo-url>
cd <your-repo-directory>
Set Up a Virtual Environment
```

On Windows:

``` bash

python -m venv youtube-downloader-env
.\youtube-downloader-env\Scripts\activate
On macOS and Linux:
```

``` bash

python -m venv youtube-downloader-env
source youtube-downloader-env/bin/activate
Install Required Libraries
```

``` bash

pip install schedule
Usage
Configure Source and Destination Directories
Open the Python script and set source_dir and destination_dir to the paths you want to use:

python
Copy code
source_dir = "path/to/your/source/folder"
destination_dir = "path/to/your/destination/folder"
Set the Scheduled Time
Edit the scheduled_time variable in the script to the time you want the backup to run daily:

python
Copy code
scheduled_time = "18:57"  # Change to your desired time in HH:MM format
Run the Script
Start the script:

bash
Copy code
python your_script_name.py
Leave the script running for it to execute the daily backups at the specified time.

Configuration
source_dir: Path to the folder you want to back up.
destination_dir: Path where the backup will be saved. Each day's backup will be stored in a folder named with the current date.
scheduled_time: Time when the script should copy the folder each day. Use HH:MM format in 24-hour time.
License
This project is licensed under the MIT License. See the LICENSE file for details.