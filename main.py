import os
from telegram import Bot

BOT_TOKEN = "8997221071:AAFlhTXwiNeBTDJX4f_tzRwWQ_oVjEHcsKI"
GROUP_ID = -1004436958035   # your group ID
FOLDER_PATH = "videos"

def main():
    bot = Bot(token=BOT_TOKEN)

    # Get all video files in folder
    videos = [f for f in os.listdir(FOLDER_PATH) if f.lower().endswith((".mp4", ".mkv", ".mov"))]

    # Sort videos alphabetically
    videos.sort()

    # Send each video
    for video in videos:
        video_path = os.path.join(FOLDER_PATH, video)
        with open(video_path, "rb") as vf:
            bot.send_video(chat_id=GROUP_ID, video=vf, caption=f"Daily video: {video}")
            print(f"Uploaded: {video}")

if __name__ == "__main__":
    main()
