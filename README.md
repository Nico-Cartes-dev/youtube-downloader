# youtube downloader
 youtube-dowloader with python

Installing FFmpeg
To install FFmpeg on your system, follow the instructions corresponding to your operating system:

Windows
Download FFmpeg:
Go to the official FFmpeg download page: https://ffmpeg.org/download.html.
In the Windows section, select a download link, for example, from gyan.dev: FFmpeg builds.
Download the compressed file of the full or git version (the most complete) under Release builds.
Extract FFmpeg:
Extract the contents of the downloaded file to a folder, for example: C:\ffmpeg.
Add FFmpeg to PATH:
To use FFmpeg from anywhere in the command line, you need to add it to the environment variables:

Open the Start menu and search for "environment variables" or "Edit the system environment variables."
Click on "Environment Variables."
In the system variables, select the variable Path and click "Edit."
Click "New" and add the full path to the FFmpeg bin folder, for example:
makefile
Copy code

C:\ffmpeg\bin

Accept the changes and close all windows.
Verify the installation:
Open the Command Prompt (cmd), and run the following command to verify that FFmpeg is installed correctly:
bash
Copy code
ffmpeg -version
You should see information about the installed FFmpeg version.
macOS
Install FFmpeg with Homebrew:
If you have Homebrew installed, the easiest way to install FFmpeg is using this package manager:

Open a terminal and run:
bash
Copy code
brew install ffmpeg
Verify the installation:
In the terminal, run:
bash
Copy code
ffmpeg -version
Linux (Ubuntu/Debian)
Install FFmpeg:
On Ubuntu or Debian-based Linux systems, you can install FFmpeg directly from the official repositories:

Open a terminal and run:
bash
Copy code
sudo apt update
sudo apt install ffmpeg
Verify the installation:
In the terminal, run:
bash
Copy code
ffmpeg -version
After Installation
Once FFmpeg is correctly installed on your system, the yt-dlp script will be able to automatically use it to convert downloaded audio files to MP3 format. If there are no errors when verifying the installation, your program should work smoothly when downloading and converting audio.

