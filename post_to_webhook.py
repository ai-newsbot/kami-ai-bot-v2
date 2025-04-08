import os
import requests

def post_to_webhook(data):
    webhook_url = os.getenv("ZAPIER_WEBHOOK_URL")
    if not webhook_url:
        print("Webhook URL が設定されていません。")
        return
    response = requests.post(webhook_url, json=data)
    print("Webhook送信完了:", response.status_code)
