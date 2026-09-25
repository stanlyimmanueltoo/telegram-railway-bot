import os
import time
from telegram import Bot
from telegram.error import RetryAfter

BOT_TOKEN = "8997221071:AAFlhTXwiNeBTDJX4f_tzRwWQ_oVjEHcsKI"
GROUP_ID = -1004436958035   # your group ID
FOLDER_PATH = "videos"

# YOU FORGOT THIS LINE — this creates the bot object
bot = Bot(token=BOT_TOKEN)

def main():
    videos = sorted(os.listdir(FOLDER_PATH))
    videos = [v for v in videos if v.endswith(".mp4")]

    for video in videos:
        video_path = os.path.join(FOLDER_PATH, video)

        print(f"Uploading: {video}")

        try:
            with open(video_path, "rb") as vf:
                bot.send_video(chat_id=GROUP_ID, video=vf, caption=f"Daily video: {video}")

            print(f"Uploaded: {video}")

            time.sleep(12)  # safe delay for Telegram flood control

        except RetryAfter as e:
            wait_time = int(e.retry_after) + 5
            print(f"Flood control triggered. Waiting {wait_time} seconds...")
            time.sleep(wait_time)

            with open(video_path, "rb") as vf:
                bot.send_video(chat_id=GROUP_ID, video=vf, caption=f"Daily video: {video}")

            print(f"Uploaded after retry: {video}")

            time.sleep(12)

if __name__ == "__main__":
    main()