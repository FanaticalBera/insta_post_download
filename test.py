import instaloader
import os
import streamlit as st
import time


st.title('Instagram Downloader')
st.subheader('Do you have an Instagram post in mind? Enter the URL and download it!')

# Initialize Instaloader
L = instaloader.Instaloader(
                            download_pictures=True,
                            download_video_thumbnails=False,
                            download_videos=True,
                            download_geotags=False,
                            download_comments=False,
                            save_metadata=True,
                            compress_json=False,
                            post_metadata_txt_pattern="",
                            max_connection_attempts=0,
                            )

# The directory where we will store all downloads
download_dir = "downloads"

# Ensure the directory exists
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

def download_instagram_post(url):
    if 'instagram.com/p/' not in url:
        st.error("Invalid URL. Please make sure it's an Instagram post URL.")
        return

    post_code = url.split("/")[-2]
    post = instaloader.Post.from_shortcode(L.context, post_code)

    progress_bar = st.progress(0)
    for i in range(100):
        # Download the post with a simulated progress incremented in each iteration
        L.download_post(post, download_dir)
        progress_bar.progress(i + 1)

    st.success("Download complete.")

def main():
    url = st.text_input("Enter the URL of the Instagram post you want to download:")
    if st.button('Download'):
        download_instagram_post(url)

if __name__ == '__main__':
    main()