

# Audio Converter

This project provides a simple audio conversion tool that allows you to convert and compress audio files into different formats suitable for various devices. The main functionality is encapsulated in the `convert_and_compress` function, which takes an input audio file and converts it to a specified format with adjustable quality settings, effectively reducing the file size for easier storage and sharing. The tool can compress audio files by up to 70%, depending on the selected format and quality settings.

<p align="center">
    <img src="image/banner.webp" alt="Banner">
</p>

## 🌟 Features

- Convert audio files between popular formats (MP4, OGG, MP3, FLAC, WAV, AIFF)
- Device-specific optimization for iPhone and Android
- Compression up to 70% with quality preservation
- Progress bar for conversion tracking
- Detailed conversion statistics

## 🔧 Requirements

- Python 3.x
- pydub
- ffmpeg
- tqdm

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/reneboygarcia/audio-converter.git](https://github.com/reneboygarcia/audio-converter.git)
   cd audio-converter
   ```

2. Install dependencies:
   ```bash
   pip install pydub tqdm
   ```

3. Install FFmpeg:
   - **Windows**: Download from [FFmpeg website](https://ffmpeg.org/download.html)
   - **Mac**: `brew install ffmpeg`
   - **Linux**: `sudo apt-get install ffmpeg`

## 💻 Usage

### Command Line
```bash
python audio_converter.py
```

### Python Script
```python
from audio_converter import convert_and_compress

# Convert audio for iPhone
convert_and_compress("input.wav", "iphone", "128k")
```

## 📱 Supported Devices & Formats

| Device/Format | Output Format | Codec         |
| ------------- | ------------- | ------------- |
| iPhone        | MP4           | AAC           |
| Android       | OGG           | Vorbis        |
| MP3           | MP3           | MP3 Lame      |
| FLAC          | FLAC          | FLAC          |
| WAV           | WAV           | PCM 16-bit LE |
| AIFF          | AIFF          | PCM 16-bit BE |

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [pydub](https://github.com/jiaaro/pydub) for audio processing
- [FFmpeg](https://ffmpeg.org/) for audio conversion
- [tqdm](https://github.com/tqdm/tqdm) for progress bars

## ⭐ Looking for an easier way?

Check out our [Google Colab Version](README_colab.md) for a no-installation solution!
```

These README files provide:
1. A beginner-friendly Colab version focusing on ease of use
2. A comprehensive GitHub README with technical details and contribution guidelines

You'll need to:
1. Create the actual Colab notebook
2. Update the repository URL
3. Add your banner image
4. Add any specific installation or usage instructions for your implementation
5. Add your license file

Would you like me to help with any of these additional items?