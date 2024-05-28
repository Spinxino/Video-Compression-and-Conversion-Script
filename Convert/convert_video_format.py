import subprocess

def convert_video_format(input_file, output_file, output_format):
    """
    Converts a video file to a different format.

    Parameters:
    input_file (str): Path to the input video file.
    output_file (str): Path to save the converted video file.
    output_format (str): Desired video format (e.g., "mp4", "avi", "mkv").
    """
    command = [
        'ffmpeg',
        '-i', input_file,
        output_file
    ]
    subprocess.run(command, check=True)

# Example usage
input_video = "Fortnite.mp4"
output_video = "output.avi"
output_format = "avi"
convert_video_format(input_video, output_video, output_format)
