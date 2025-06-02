from flask import Flask, request, jsonify
from handlers import insert_mcp, fetch_mcp

app = Flask(__name__)

@app.route('/mcp', methods=['POST'])
def add_mcp():
    data = request.json
    response = insert_mcp(data)
    print(f"Inserted MCP data: {data}")  # Confirmation print
    return jsonify(response)

@app.route('/mcp/<record_id>', methods=['GET'])
def get_mcp(record_id):
    response = fetch_mcp(record_id)
    print(f"Fetched MCP data for ID: {record_id}")  # Confirmation print
    return jsonify(response)

if __name__ == '__main__':
    print("MCP Server is starting...")  # Initial confirmation print
    app.run(debug=True)