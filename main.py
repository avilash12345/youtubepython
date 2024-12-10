import streamlit as st
from pytubefix import YouTube
import os




# Create a folder to save the files if it doesn't exist
DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)
# Function to download video
def download_video(url, resolution):
    try:
        # Initialize YouTube object using the URL
        yt = YouTube(url)
        
        # Get video stream filtered by resolution and file type
        video_stream = yt.streams.filter(res=resolution, file_extension="mp4").first()

        if video_stream:
            st.info(f"Downloading {yt.title} video in {resolution}...")
            # Download the video
            file_path = video_stream.download(DOWNLOAD_FOLDER)
            st.success(f"Download complete! The video '{yt.title}' has been saved at '{file_path}'.")
        else:
            st.error(f"No video found with the resolution {resolution}. Try another one.")
    except Exception as e:
        st.error(f"Error: {e}")

# Function to download audio
def download_audio(url):
    try:
        # Initialize YouTube object using the URL
        yt = YouTube(url)
        
        # Get the first available audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        if audio_stream:
            st.info(f"Downloading audio of {yt.title}...")
            # Download the audio
            file_path=audio_stream.download(DOWNLOAD_FOLDER)
            st.success(f"Download complete! The audio of '{yt.title}' has been saved. at '{file_path}'")
        else:
            st.error("No audio stream available.")
    except Exception as e:
        st.error(f"Error: {e}")

# Function to download both video and audio
def download_both(url, resolution):
    try:
        # Initialize YouTube object using the URL
        yt = YouTube(url)
        
        # Download video
        video_stream = yt.streams.filter(res=resolution, file_extension="mp4").first()
        if video_stream:
            st.info(f"Downloading {yt.title} video in {resolution}...")
            file_path = video_stream.download(DOWNLOAD_FOLDER)
            st.success(f"Download complete! The video '{yt.title}' has been saved at '{file_path}'.")
        else:
            st.error(f"No video found with the resolution {resolution}. Try another one.")
        
        # Download audio
        audio_stream = yt.streams.filter(only_audio=True).first()
        if audio_stream:
            st.info(f"Downloading audio of {yt.title}...")
            file_path=audio_stream.download(DOWNLOAD_FOLDER)
            st.success(f"Download complete! The audio of '{yt.title}' has been saved. at '{file_path}'")
        else:
            st.error("No audio stream available.")
    except Exception as e:
        st.error(f"Error: {e}")

# Streamlit UI
st.title("YouTube Video & Audio Downloader")
st.markdown("### Enter the URL of the YouTube video you want to download")

# URL input
url = st.text_input("YouTube URL:")

# Resolution options for video download
resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p"]
resolution = st.selectbox("Select Video Resolution", resolutions)

# Option to select download type (video, audio, or both)
download_type = st.radio(
    "Select Download Type",
    ("Video", "Audio", "Both Video and Audio")
)

# Download button
if st.button("Download"):
    if url:
        if download_type == "Video":
            download_video(url, resolution)
        elif download_type == "Audio":
            download_audio(url)
        else:
            download_both(url, resolution)
    else:
        st.error("Please enter a valid YouTube URL.")