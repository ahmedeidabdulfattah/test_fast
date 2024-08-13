# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask with Uvicorn!"
import os
if __name__ == '__main__':
     import uvicorn
     port = int(os.getenv("PORT", 8000))
     uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
