import os
from flask import Flask, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud import storage

app = Flask(__name__)

# # LOCAL DEVELOPMENT ONLY (comment out for deployment)
# cred_path = "test-flask-427711-3c172516044b.json"
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred_path
# cred = credentials.Certificate(cred_path)

# DEPLOYMENT ONLY (comment out for local development)
cred = credentials.ApplicationDefault()

# Initialize Google Cloud Storage
storage_client = storage.Client()
bucket = storage_client.get_bucket("shalin-test-bucket-123")

# Initialize Firebase Admin SDK for Firestore
firebase_admin.initialize_app(cred)
db = firestore.client()
collection_ref = db.collection("shalin-test-collection-123")

storage_client = storage.Client()
bucket = storage_client.get_bucket("shalin-test-bucket-123")

@app.route("/")
def index():
    return f'index'

@app.route("/add_data/<number>", methods = ["GET"])
def add_data(number):
    data_key = f'test_{number}'
    doc_ref = collection_ref.document(data_key)
    doc_ref.set({
        "value": int(number)
    })

    blob = bucket.blob(f'{data_key}.txt')
    blob.upload_from_string(f'This is example {number}.')

    return jsonify({"messages": "success"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
