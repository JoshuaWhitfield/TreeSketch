from flask import Flask, request, send_file, abort
import os
import hashlib
import time

app = Flask(__name__)

# Simple in-memory token store
tokens = {
    "abc123": {
        "file": "premium/agents/smart_agent.py",
        "expires": time.time() + 3600  # 1 hour
    }
}

@app.route("/download", methods=["GET"])
def download():
    token = request.args.get("token")
    if not token or token not in tokens:
        return abort(403)

    info = tokens[token]
    if time.time() > info["expires"]:
        return abort(403)

    filepath = info["file"]
    if not os.path.exists(filepath):
        return abort(404)

    return send_file(filepath, as_attachment=True)

if __name__ == "__main__":
    app.run(port=5050)
