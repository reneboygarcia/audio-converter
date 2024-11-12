# Importing libraries
from pydub import AudioSegment
import tempfile
import os
from tqdm import tqdm
import time

print("Dependencies Loaded")


# Function to convert and compress an audio file
def convert_and_compress(
    input_file: str = None, device_type: str = "iphone", bit_rate: str = "128k"
) -> str:
    """
    Convert and compress an audio file to a specified format based on device type.

    Parameters:
    - input_file (str): Path to the input audio file.
    - device_type (str): Type of device for which the audio is being converted.
    - bit_rate (str): Bit rate for the output audio file (default is "128k").

    Returns:
    - str: Path to the output audio file if successful, None otherwise.
    """

    print("Starting audio conversion process...")

    # Get input file if not provided
    if not input_file:
        input_file = input("Enter the path to your audio file: ").strip()

    # Verify the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' was not found.")
        return None

    # Load the audio file
    print("Loading audio file...")
    try:
        audio = AudioSegment.from_file(input_file)
    except Exception as e:
        print(f"Error loading audio file: {e}")
        return None

    # Get original file size
    original_size = os.path.getsize(input_file)
    print(f"\nOriginal file size: {original_size / (1024 * 1024):.2f} MB")

    # Define output format and codec settings based on device type
    device_settings = {
        "iphone": {"output_format": "mp4", "codec": "aac"},
        "android": {"output_format": "ogg", "codec": "libvorbis"},
        "mp3": {"output_format": "mp3", "codec": "libmp3lame"},
        "flac": {"output_format": "flac", "codec": "flac"},
        "wav": {"output_format": "wav", "codec": "pcm_s16le"},
        "aiff": {"output_format": "aiff", "codec": "pcm_s16be"},
    }

    # Get device type if not provided
    if not device_type:
        print("\nAvailable device types:", ", ".join(device_settings.keys()))
        device_type = input("Enter the target device type: ").lower()

    # Check if the provided device type is supported
    if device_type not in device_settings:
        print("Unsupported device type")
        return None

    # Retrieve output format and codec for the specified device type
    output_format = device_settings[device_type]["output_format"]
    codec = device_settings[device_type]["codec"]

    # Create output directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(input_file), "converted_audio")
    os.makedirs(output_dir, exist_ok=True)

    # Set output file path in the new directory
    base = os.path.splitext(os.path.basename(input_file))[0]
    output_file = os.path.join(output_dir, f"{base}.{output_format}")

    print(
        f"\nConverting to {output_format.upper()} format for {device_type.title()}..."
    )
    try:
        # Export audio with progress bar
        with tqdm(total=100, desc="Converting", unit="%") as pbar:
            # Start export process
            audio.export(
                output_file,
                format=output_format,
                codec=codec,
                bitrate=bit_rate,
            )
            
            # Update progress bar to 100% since we can't track real-time progress
            pbar.update(100)

        # Calculate and display file sizes
        output_size = os.path.getsize(output_file)
        savings = original_size - output_size
        savings_percentage = (savings / original_size * 100) if original_size > 0 else 0

        print("\nConversion Summary:")
        print(f"Original Size: {original_size / (1024 * 1024):.2f} MB")
        print(f"Compressed Size: {output_size / (1024 * 1024):.2f} MB")
        print(
            f"Space Saved: {savings / (1024 * 1024):.2f} MB ({savings_percentage:.2f}%)"
        )
        print(f"\nOutput file saved as: {output_file}")

        return output_file
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        return None


if __name__ == "__main__":
    convert_and_compress()
