<p align="center">
    <img src="image/banner.webp" alt="Banner">
</p>

# Audio Converter

This project provides a simple audio conversion tool that allows you to convert and compress audio files into different formats suitable for various devices. The main functionality is encapsulated in the `convert_and_compress` function, which takes an input audio file and converts it to a specified format with adjustable quality settings, effectively reducing the file size for easier storage and sharing. The tool can compress audio files by up to 70%, depending on the selected format and quality settings.

## Features

- Convert and compress audio files to formats such as MP4, OGG, MP3, FLAC, WAV, and AIFF.
- Supports device-specific settings for optimal audio quality while minimizing file size.
- Displays original and output file sizes, along with savings in file size after conversion.

## Requirements

- Python 3.x
- `pydub` library for audio processing
- `ffmpeg` or `libav` for audio format conversion

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install pydub
   ```

3. Ensure you have `ffmpeg` or `libav` installed on your system. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html).

## Usage

To use the audio converter, modify the `input_wav_file`, `device_type`, and `bit_rate` variables in the `audio_converter.ipynb` file.
