from flask import Flask, request
import sqlite3

app = Flask(__name__)


from flask import request
import sqlite3

def receive_whatsapp_message():
    try:
        data = request.json
        if not data:
            return "Invalid request: No JSON data received", 400

        sender = data.get("From", "Unknown Sender")
        message = data.get("Body", "No message received")

        # Store message in database
        conn = sqlite3.connect("messages.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO whatsapp_messages (sender, message) VALUES (?, ?)", (sender, message))
        conn.commit()
        conn.close()

        return f"Message received from {sender}: {message}", 200
    except Exception as e:
        return f"Server Error: {str(e)}", 500
@app.route("/whatsapp-webhook", methods=["POST"])
def whatsapp_webhook():
    data = request.json  # Twilio sends messages as JSON
    sender = data["From"]
    message = data["Body"]

    # Store message in the database
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO whatsapp_messages (sender, message) VALUES (?, ?)", (sender, message))
    conn.commit()
    conn.close()

    print(f"Message received from {sender}: {message}")
    return "Message stored", 200

if __name__ == "__main__":
    app.run(port=5000)