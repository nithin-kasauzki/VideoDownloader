from pytube import YouTube
import tkinter as tk

# to download YouTube video
def download_video(url, output_path):
    try:
        # Create a YouTube object
        video = YouTube(url)

        # Get the highest resolution video stream
        stream = video.streams.get_highest_resolution()

        # Download the video to the specified output path
        stream.download(output_path)
        print("Video downloaded successfully!")
        status_label.config(text="Video downloaded successfully!")
    except Exception as e:
        print("Error:", str(e))

# Example usage
output_folder = "/Users/nithinkumar/Coding/util/videoDownloader"
''' eg link : 
https://www.youtube.com/watch?v=dQw4w9WgXcQ
'''
# Create the GUI window
window = tk.Tk()
window.title("YouTube Video Downloader")

# Create the URL input field
url_label = tk.Label(window, text="Enter YouTube URL:")
url_label.pack()
entry = tk.Entry(window)
entry.pack()

# Create the download button
def handle_download():
    video_url = entry.get()
    entry.delete(0, tk.END)
    download_video(video_url, output_folder)
    
download_button = tk.Button(window, text="Download", command=handle_download)
download_button.pack()

# Create the status label
status_label = tk.Label(window, text="")
status_label.pack()

# Start the GUI event loop
window.mainloop()