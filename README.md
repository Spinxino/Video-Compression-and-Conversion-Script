# Video Compression and Conversion Script

## Overview
This repository contains Python scripts for compressing and converting video files. The scripts utilize the `ffmpeg` tool to reduce video file sizes and change formats, making it easier to share videos within file size limits.

## Features
- **Video Compression**: Reduce the size of large video files while maintaining acceptable quality.
- **Video Conversion**: Convert videos to different formats, allowing compatibility with various platforms and devices.

## Avoiding External Services
To bypass Discord's file size limit, many users resort to online video compression services. However, these services may compromise privacy and security by requiring file uploads to external servers.

## Benefits of Local Compression and Conversion
By using these scripts locally, you can:
- Maintain privacy by processing videos on your own machine.
- Avoid potential risks associated with third-party compression services.
- Customize compression settings according to your preferences.

## Getting Started

### Prerequisites
- Python 3 installed on your system.
- `ffmpeg` command-line tool installed. [Download here](https://ffmpeg.org/download.html).

### Step 1: Install `ffmpeg`
If you haven't installed `ffmpeg` yet, you can download it from the [official ffmpeg website](https://ffmpeg.org/download.html). Follow the installation instructions for your operating system.

### Step 2: Add `ffmpeg` to System PATH

**On Windows**:
1. Download the `ffmpeg` static build from the official website.
2. Extract the contents of the zip file.
3. Copy the `bin` folder's path (where `ffmpeg.exe` is located).
4. Add this path to the system PATH:
    - Right-click on `This PC` or `Computer` on the desktop or in File Explorer.
    - Click on `Properties`.
    - Click on `Advanced system settings`.
    - Click on `Environment Variables`.
    - Under `System variables`, find the `Path` variable, select it, and click `Edit`.
    - Click `New` and paste the path to the `bin` folder.
    - Click `OK` to close all dialog boxes.

### Step 3: Verify `ffmpeg` Installation
Open a command prompt and type `ffmpeg`. You should see the version information if `ffmpeg` is correctly installed.

### Step 4: Run the Script
1. Clone or download this repository to your local machine.
2. Place the video file you want to compress or convert (e.g., `input.mp4`) in the same directory as the scripts (`compress_video.py` and `convert_video.py`).

## Usage

1. Open a terminal or command prompt and navigate to the repository directory.
2. Run the following commands:

   For video compression:
   ```bash
   python compress_video.py
   ```
   For video converting
   ```bash
   python convert_video_format.py
   ```
