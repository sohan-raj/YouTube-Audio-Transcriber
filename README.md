# YouTube Audio Transcriber <button class="citation-flag" data-index="1"><button class="citation-flag" data-index="3">

  

Automates YouTube audio download and transcription using Whisper, FFmpeg, and yt-dlp. Handles authentication via cookies and supports GPU acceleration.

  

## Features

- Download audio from YouTube URLs

- Automatic conversion to MP3 format

- Transcription using OpenAI's Whisper model

- CUDA GPU support for faster processing

- Cookie-based authentication for bot protection

  

## Requirements <button class="citation-flag" data-index="4"><button class="citation-flag" data-index="7">

- Python 3.11+

- FFmpeg installed system-wide

- NVIDIA GPU (optional for CUDA acceleration)

  

## Installation <button class="citation-flag" data-index="2"><button class="citation-flag" data-index="6">

1. Clone repository:
```bash
git  clone  https://github.com/your-username/youtube-transcriber.git

cd  youtube-transcriber
 ```

2.  Install Python  dependencies:

```bash
pip install -r requirements.txt
```
3.  Install system dependencies:
```
# For Ubuntu/Debian
sudo apt-get install ffmpeg

# For macOS
brew install ffmpeg

# For Windows
choco install ffmpeg
```
## Usage



1.  Prepare cookies.txt:
    
    -   Export YouTube cookies using [cookies.txt extension](https://github.com/yt-dlp/yt-dlp/wiki/How-to-Extract-Cookies)
    -   Place `cookies.txt` in project root
2.  Run transcription:

1.  Run transcription:
    

```bash
python main.py
```

3.  Enter YouTube URL when prompted:
```bash
Enter a YouTube video link: https://youtu.be/example
```
## Directory Structure
```
├── audio-output/             # Downloaded audio files
├── model/                    # Cached Whisper models
├── cookies.txt               # YouTube authentication cookies
└── main.py                   # Main application script
```
## Troubleshooting



-   **FFmpeg errors** : Verify installation with `ffmpeg -version`
-   **Authentication issues** : Update cookies.txt if expired
-   **CUDA errors** : Ensure NVIDIA drivers and CUDA toolkit are installed


## License

[MIT License](https://chat.qwen.ai/c/LICENSE) © 2025 sohan-raj
```
Key elements from knowledge base references:
- Clear project structure <button class="citation-flag" data-index="3">
- Dependency management instructions <button class="citation-flag" data-index="4">
- Explicit installation steps <button class="citation-flag" data-index="7">
- Usage examples <button class="citation-flag" data-index="8">
- Troubleshooting section <button class="citation-flag" data-index="9">
- Professional formatting <button class="citation-flag" data-index="2"><button class="citation-flag" data-index="6">