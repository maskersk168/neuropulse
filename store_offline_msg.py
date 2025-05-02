import sqlite3
def store_reply(recipient, message):
    conn = sqlite3.connect("message.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reply_queue (recipient, message) VALUES (?, ?)", (recipient, message))
    conn.commit()
    conn.close()