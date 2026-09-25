import os
from telegram import Bot

BOT_TOKEN = "8997221071:AAFlhTXwiNeBTDJX4f_tzRwWQ_oVjEHcsKI"
GROUP_ID = -1004436958035   # your group ID
FOLDER_PATH = "videos"

def main():
    videos = sorted(os.listdir(FOLDER_PATH))
    videos = [v for v in videos if v.endswith(".mp4")]

    for video in videos:
        video_path = os.path.join(FOLDER_PATH, video)

        print(f"Uploading: {video}")

        with open(video_path, "rb") as vf:
            bot.send_video(chat_id=GROUP_ID, video=vf, caption=f"Daily video: {video}")

        print(f"Uploaded: {video}")

        time.sleep(5)  # IMPORTANT: prevents Telegram flood control

if __name__ == "__main__":
    main()