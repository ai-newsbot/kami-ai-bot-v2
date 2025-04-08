import datetime
import os
from run_post_job import run_post_job

def log_message(message):
    now = datetime.datetime.now()
    log_dir = "log"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, now.strftime("%Y-%m-%d") + ".txt")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{now.strftime('%H:%M:%S')}] {message}\n")

def main():
    log_message("===== 神AI起動 =====")
    try:
        run_post_job()
        log_message("投稿処理 正常終了 ✅")
    except Exception as e:
        log_message(f"投稿処理でエラー発生 ❌: {str(e)}")

if __name__ == "__main__":
    main()
