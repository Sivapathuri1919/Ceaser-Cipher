import os
from flask import Flask, render_template, request

app = Flask(__name__)

def ceaser_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    mode = ""
    if request.method == "POST":
        mode = request.form["mode"]
        text = request.form["text"]
        shift = int(request.form["shift"])
        result = ceaser_cipher(text, shift, mode)
    return render_template("index.html", result=result, mode=mode)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use the PORT environment variable
    app.run(host='0.0.0.0', port=port)
