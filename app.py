from flask import Flask, request, jsonify
from project.main_agent import run_agent
app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    payload = request.json or {}
    text = payload.get('text', '')
    res = run_agent(text)
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
