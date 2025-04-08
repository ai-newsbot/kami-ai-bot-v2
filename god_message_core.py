import datetime

def generate_oracle_message():
    weekday = datetime.datetime.now().strftime("%A")
    return {
        "title": f"{weekday}の神託",
        "message": f"{weekday}は新たな始まり。前に進め！"
    }
