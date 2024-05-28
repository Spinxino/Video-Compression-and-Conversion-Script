import subprocess
import os

def compress_video(input_file, output_file, bitrate="1M"):
    """
    Compresses a video file to reduce its size.

    Parameters:
    input_file (str): Path to the input video file.
    output_file (str): Path to save the compressed video file.
    bitrate (str): Desired bitrate for compression (e.g., "1M" for 1 megabit per second).
    """
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")
    
    command = [
        'ffmpeg',
        '-i', input_file,
        '-b:v', bitrate,
        '-b:a', '128k',  # Optional: Set audio bitrate to 128 kbps
        output_file
    ]
    try:
        subprocess.run(command, check=True)
        print(f"Video compressed successfully: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

# Example usage
input_video = "Fortnite.mp4"
output_video = "output_compressed.mp4"
compress_video(input_video, output_video)
