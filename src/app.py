from flask import Flask, request
app = Flask(__name__)

todos = [
    {"label": "My first task", "done": False},
    {"label": "my second task", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'





























if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)