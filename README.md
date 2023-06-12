# YouTube Downloader

This is a YouTube downloader application implemented in Python using the CustomTkinter library. It allows you to download videos from YouTube in either MP4 or MP3 format.

## Features

- Fetches and displays the thumbnail and title of a YouTube video by entering its URL.
- Provides options to download the video in MP4 format or extract the audio as an MP3 file.
- Shows the download progress with a progress bar and percentage.
- Notifies the user of successful downloads or errors.

## Requirements

- Python 3.x
- CustomTkinter library
- pytube library
- pydub library
- Pillow library

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/dimilidi/pytube
   ```

2. Install the required libraries:

   ```shell
   pip install customtkinter pytube pydub Pillow
   ```

## Usage

1. Run the `youtube_downloader.py` file:

   ```shell
   python youtube_downloader.py
   ```

2. Enter a valid YouTube URL in the provided input field and click the "Go" button.
3. The thumbnail image and title of the video will be displayed.
4. Select the desired format (MP4 or MP3) using the radio buttons.
5. Click the "Download" button to start the download.
6. The progress bar will show the download progress, and the percentage will be updated accordingly.
7. Once the download is complete, a success message will be displayed.

## Screenshots
<img src = "pytube.jpg" width = 400>


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

