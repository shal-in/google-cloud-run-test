from flask import Flask
import os

app = Flask(__name__)

cred =  os.getenv("GOOGLE_CREDENTIALS")
password = os.getenv("PASSWORD")

@app.route("/")
def index():
    return f'{cred}\n\n{password}'

if __name__ == '__main__':
    app.run(debug=True)