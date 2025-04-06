from flask import Flask, jsonify, request
import threading

app = Flask(__name__)

# Global variable to store volume data
volume_data = {"total_volume": 0, "timestamp": 0}
lock = threading.Lock()

@app.route('/volume', methods=['GET'])
def get_volume():
    with lock:
        return jsonify(volume_data)

@app.route('/update_volume', methods=['POST'])
def update_volume():
    data = request.get_json()
    with lock:
        volume_data["total_volume"] = data.get("total_volume", 0)
        volume_data["timestamp"] = data.get("timestamp", 0)
    return "", 204  # No content response

if __name__ == "__main__":
    # Render uses PORT environment variable; default to 5000 locally
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
