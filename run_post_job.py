from utils.post_to_webhook import post_to_webhook
from shared.god_message_core import generate_oracle_message

def run_post_job():
    oracle = generate_oracle_message()
    post_to_webhook(oracle)
