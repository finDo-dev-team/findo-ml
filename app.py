from flask import Flask

app = Flask(__name__)

@app.route("/")
def discover_events():
    
    return {
        "value" : 7
    }