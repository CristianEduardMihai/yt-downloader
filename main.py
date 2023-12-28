import tkinter as tk
from tkinter import ttk
import os
from downloaders.audio import download_audio
from downloaders.video import download_video

# Make a TK UI representing a text box where the user can paste URLs separated by /n, a dropdown menu to select the type of download, and a button to start the download

# Create a window
window = tk.Tk()
window.title("YouTube Downloader")
window.configure(bg='#333')

# Create a text box
text_box = tk.Text(window, height=10, width=50, bg='#555', fg='#fff')
text_box.pack()

# Create a dropdown menu
OPTIONS = [ 'Audio', 'Video' ]
variable = tk.StringVar(window)
variable.set(OPTIONS[0])

style = ttk.Style(window)
style.configure('TCombobox', background='#555', foreground='#f00')
style.map('TCombobox', background=[('active', '#555'), ('!disabled', '#555')], foreground=[('active', '#f00'), ('!disabled', '#f00')])

dropdown = ttk.Combobox(window, values=OPTIONS, textvariable=variable, style='TCombobox')
dropdown.pack()

# if the `audio_downloads` folder doesn't exist, create it
if not os.path.exists('audio_downloads'):
    os.makedirs('audio_downloads')
# if the `video_downloads` folder doesn't exist, create it
if not os.path.exists('video_downloads'):
    os.makedirs('video_downloads')

# Create a button
def download():
    # Disable the button while downloading
    button.config(state='disabled')

    # Get the type of download
    download_type = variable.get()
    # Get the URLs from the text box
    urls = text_box.get("1.0", "end-1c").splitlines()
    # Download the URLs
    if download_type == 'Audio':
        format = download_audio(urls)
        # move all files ending in format to a folder called 'audio_downloads'
        for file in os.listdir():
            if file.endswith(format):
                os.rename(file, f'audio_downloads/{file}')
        # open the folder
        if os.name == 'nt':
            os.system("explorer .\\audio_downloads")
    elif download_type == 'Video':
        format = download_video(urls)
        # move all files ending in format to a folder called 'video_downloads'
        for file in os.listdir():
            if file.endswith(format):
                os.rename(file, f'video_downloads/{file}')
        # open the folder
        if os.name == 'nt':
            os.system("explorer .\\video_downloads")
    
    # Print DONE
    print('DONE')

    # Re-enable the button after downloading is finished
    button.config(state='normal')

# Create a button with a spinning animation
button_frame = tk.Frame(window, bg='#333')
button_frame.pack(pady=10)
button = tk.Button(button_frame, text='Download', command=download, bg='#f00', fg='#fff', relief='flat', activebackground='#f00', activeforeground='#fff')
button.pack()

canvas = tk.Canvas(button_frame, width=20, height=20, bg='#333', highlightthickness=0)
canvas.pack(side=tk.LEFT, padx=10)

x0, y0, x1, y1 = (5, 5, 15, 15)
arc = canvas.create_oval(x0, y0, x1, y1, fill='#fff')
def animate():
    canvas.move(arc, 2, 0)
    canvas.after(50, animate)
canvas.after(0, animate)

# Start the window
window.mainloop()
