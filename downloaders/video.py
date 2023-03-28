import yt_dlp


def download_video(URLS):

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mkv',  # Change to 'mp4' for MP4 format
        'outtmpl': '%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS)
        # Get the filename of the downloaded file
        filename = ydl.prepare_filename(ydl.extract_info(URLS[0], download=False))

    return ydl_opts['merge_output_format']