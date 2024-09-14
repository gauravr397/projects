import os
import time
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import googleapiclient.http
from googleapiclient.http import MediaFileUpload

# Define the API scopes for YouTube
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# OAuth 2.0 authentication process
def authenticate_youtube():
    # OAuth 2.0 client secrets file
    CLIENT_SECRETS_FILE = "client_secrets.json"
    
    # Initiate OAuth flow
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)

    return googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

# Upload the video to YouTube
def upload_video(youtube, video_file, title, description, tags, category_id="22"):
    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": "private"  # You can change this to "public" or "unlisted"
        }
    }

    # Prepare the video file for upload
    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)
    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploaded {int(status.progress() * 100)}%")

    print("Video uploaded successfully!")
    return response

# Function to traverse directories and upload videos
def upload_videos_from_directory(youtube, folder_path):
    # Walk through the folder and subdirectories in sorted order
    for root, dirs, files in sorted(os.walk(folder_path)):
        # Sort files alphabetically and filter only video files (you can adjust file extensions)
        video_files = sorted([f for f in files if f.lower().endswith(('.mp4', '.mov', '.avi', '.mkv'))])

        for video_file in video_files:
            video_path = os.path.join(root, video_file)

            # Extract the title from the file name (without extension)
            title = os.path.splitext(video_file)[0]
            description = f"Uploaded {title} from folder {root}"

            # Upload the video to YouTube
            print(f"Uploading {video_file}...")
            upload_video(youtube, video_path, title, description, tags=["sample", "video"])
            time.sleep(10)  # Wait between uploads to avoid exceeding quota limits

if __name__ == "__main__":
    # Specify the folder to search for videos
    folder_path = "C:/Users/GauravRaghav/Documents/VS_code/Python_prj/YoutubeUpload"

    # Authenticate and create YouTube API client
    youtube = authenticate_youtube()

    # Start uploading videos
    upload_videos_from_directory(youtube, folder_path)
