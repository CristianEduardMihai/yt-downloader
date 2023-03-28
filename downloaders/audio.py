import yt_dlp

def download_audio(URLS):
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }],
        'outtmpl': '%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)
        # Get the filename of the downloaded file
        filename = ydl.prepare_filename(ydl.extract_info(URLS[0], download=False))
    
    return ydl_opts['postprocessors'][0]['preferredcodec']