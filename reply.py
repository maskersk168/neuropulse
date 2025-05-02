from twilio.rest import Client
import sqlite3

account_sid = "AC10a4a21e5a164976f171b60844fc735a"
auth_token = "dc91fd029a69ca2bfa0f4508c1c133cc"
twilio_client = Client(account_sid, auth_token)
def send_pending_replies():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, recipient, message FROM reply_queue WHERE status = 'pending'")
    pending_replies = cursor.fetchall()

    if pending_replies:
        for msg_id, recipient, msg in pending_replies:
            twilio_client.messages.create(
                from_="whatsapp:+16402012336",
                body=msg,
                to=f"whatsapp:{recipient}"
            )
            cursor.execute("UPDATE reply_queue SET status='sent' WHERE id=?", (msg_id,))
            conn.commit()

    conn.close()

import sqlite3
from twilio.rest import Client

account_sid = "your_account_sid"
auth_token = "your_auth_token"
twilio_client = Client(account_sid, auth_token)

def send_pending_replies():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, recipient, message FROM reply_queue WHERE status = 'pending'")
    pending_replies = cursor.fetchall()

    if pending_replies:
        for msg_id, recipient, msg in pending_replies:
            # Send via Twilio
            twilio_client.messages.create(
                from_="whatsapp:+14155238886",
                body=msg,
                to=f"whatsapp:{recipient}"
            )
            cursor.execute("UPDATE reply_queue SET status='sent' WHERE id=?", (msg_id,))
            conn.commit()

    conn.close()
    return "Pending replies sent", 200