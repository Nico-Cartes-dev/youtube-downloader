
# YouTube Downloader
YouTube downloader built with Python.

## Installing FFmpeg

To install FFmpeg on your system, follow the instructions corresponding to your operating system:

### Windows

#### Download FFmpeg:
1. Go to the official FFmpeg download page: [FFmpeg Download Page](https://ffmpeg.org/download.html).
2. In the Windows section, select a download link, for example, from gyan.dev: FFmpeg builds.
3. Download the compressed file of the full or git version (the most complete) under Release builds.

#### Extract FFmpeg:
- Extract the contents of the downloaded file to a folder, for example: 
  ```
  C:\ffmpeg
  ```

#### Add FFmpeg to PATH:
To use FFmpeg from anywhere in the command line, you need to add it to the environment variables:
1. Open the Start menu and search for "environment variables" or "Edit the system environment variables."
2. Click on "Environment Variables."
3. In the system variables, select the variable `Path` and click "Edit."
4. Click "New" and add the full path to the FFmpeg bin folder, for example:
   ```
   C:\ffmpeg\bin
   ```
5. Accept the changes and close all windows.

#### Verify the installation:
- Open the Command Prompt (cmd), and run the following command to verify that FFmpeg is installed correctly:
  ```bash
  ffmpeg -version
  ```
- You should see information about the installed FFmpeg version.

### macOS

#### Install FFmpeg with Homebrew:
If you have Homebrew installed, the easiest way to install FFmpeg is using this package manager:
- Open a terminal and run:
  ```bash
  brew install ffmpeg
  ```

#### Verify the installation:
- In the terminal, run:
  ```bash
  ffmpeg -version
  ```

### Linux (Ubuntu/Debian)

#### Install FFmpeg:
On Ubuntu or Debian-based Linux systems, you can install FFmpeg directly from the official repositories:
- Open a terminal and run:
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

#### Verify the installation:
- In the terminal, run:
  ```bash
  ffmpeg -version
  ```

## After Installation
Once FFmpeg is correctly installed on your system, the yt-dlp script will be able to automatically use it to convert downloaded audio files to MP3 format. If there are no errors when verifying the installation, your program should work smoothly when downloading and converting audio.
