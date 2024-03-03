
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
  return "200"

if __name__ == "__main__":
  app.run(debug=True, port=5001) 
