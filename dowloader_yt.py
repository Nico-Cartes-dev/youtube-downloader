import yt_dlp
import os

video_url = input("Enter the video URL: ")
option = input("Choose video (1) or audio (2): ").strip()
# download_path = r"choose your route"  
os.makedirs(download_path, exist_ok=True)

def audio_quality(audio_format, ydl_opts):
    if audio_format == '1':
        print('Chosen format: MP3')
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    elif audio_format == '2':
        print('Chosen format: WAV')
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
        })
    elif audio_format == '3':
        print('Chosen format: FLAC')
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'flac',
            }],
        })
    else:
        print('Invalid option, MP3 will be used by default.')
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })


try:
    ydl_opts = {
        #'ffmpeg_location': r'C:\ffmpeg\bin', change to your location
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  
    }

    if option == '1':
        print('You have chosen video.')
        ydl_opts['format'] = 'best'
    elif option == '2':
        print('You have chosen audio.')
        audio_format = input("Choose audio format (1: mp3, 2: wav, 3: flac): ").strip()
        audio_quality(audio_format, ydl_opts)
    else:
        print('Invalid option')
        exit()

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    print('Download completed.')

except Exception as e:
    print(f'Error: {e}')
