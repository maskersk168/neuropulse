from twilio.rest import Client
import sqlite3
from plyer import notification  # For local notifications

# Twilio credentials
account_sid = "AC10a4a21e5a164976f171b60844fc735a"
auth_token = "dc91fd029a69ca2bfa0f4508c1c133cc"
twilio_client = Client(account_sid, auth_token)

def check_new_messages():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("SELECT sender, message FROM whatsapp_messages WHERE status = 'received'")
    new_messages = cursor.fetchall()
    conn.close()

    if new_messages:
        for sender, msg in new_messages:
            alert_message = f"New Msg from {sender}: {msg}"
            
            # Send SMS notification
            twilio_client.messages.create(
                from_="+1XXXXXXXXXX",
                body=alert_message,
                to="+91XXXXXXXXXX"
            )
            
            # Send local notification
            notification.notify(
                title="New WhatsApp Message",
                message=alert_message,
                timeout=10
            )

    return "Alerts sent", 200