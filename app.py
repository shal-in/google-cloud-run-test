from flask import Flask
import os
import json

app = Flask(__name__)

cred_json = os.getenv("GOOGLE_CREDENTIALS")
cred = json.loads(cred_json)

password = os.getenv("PASSWORD")

@app.route("/")
def index():
    return f'{cred}\n\n\n\n\n\n{password}'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
