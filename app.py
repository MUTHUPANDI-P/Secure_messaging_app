from flask import Flask, render_template, request, redirect, url_for
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

# Key generation or loading (simplified for prototype)
if not os.path.exists("secret.key"):
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
else:
    with open("secret.key", "rb") as key_file:
        key = key_file.read()

cipher = Fernet(key)

# Store messages (in-memory for now)
# Each message will be a dict: {sender: "User A" or "User B", message: <encrypted>}
messages = []

@app.route('/')
def index():
    message_pairs = [
        {
            "sender": msg["sender"],
            "encrypted": msg["message"],
        }
        for msg in messages
    ]
    return render_template("index.html", messages=message_pairs)

@app.route('/send', methods=['POST'])
def send():
    sender = request.form['sender']
    message = request.form['message']
    encrypted_message = cipher.encrypt(message.encode()).decode()
    messages.append({"sender": sender, "message": encrypted_message})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
