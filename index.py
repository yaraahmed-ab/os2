from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Docker Flask App!"

@app.route("/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello, {name}! Welcome to Docker Flask App."})

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)