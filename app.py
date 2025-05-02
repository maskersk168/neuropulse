from flask import Flask, request
from recieve_wp_msg import receive_whatsapp_message
from reply import send_pending_replies
from store_offline_msg import store_reply
from alert import check_new_messages

app = Flask(__name__)

# Route to receive WhatsApp messages
@app.route("/whatsapp-webhook", methods=["POST"])
def handle_whatsapp_message():
    return receive_whatsapp_message()

# Route to check and send alerts for new messages when offline
@app.route("/check-alerts", methods=["GET"])
def trigger_alerts():
    return check_new_messages()

# Route to store offline replies
@app.route("/store-reply", methods=["POST"])
def handle_reply():
    return store_reply()

# Route to send pending replies when online
@app.route("/send-pending-replies", methods=["GET"])
def process_pending_replies():
    return send_pending_replies()

if __name__ == "__main__":
    app.run(port=5000)