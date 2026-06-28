from flask import Flask, json

app = Flask(__name__)

@app.route('/')  # ETO YUNG PANGPAWALA NG 404
def home():
    return "✅ Attendance App is Live! Try /api/test"

@app.route('/api/test')
def test():
    return json.jsonify({"status": "ok", "message": "API works"})

if __name__ == "__main__":
    app.run(debug=True)