
from flask import Flask, request, jsonify


app = Flask(__name__)

# In-memory data store for CRUD with test data
items = [
	{'id': 1, 'name': 'Test Item 1'},
	{'id': 2, 'name': 'Sample Item 2'},
	{'id': 3, 'name': 'Demo Item 3'}
]

# Create
@app.route('/items', methods=['POST'])
def create_item():
	data = request.get_json()
	if not data or 'name' not in data:
		return jsonify({'error': 'Name is required'}), 400
	item_id = len(items) + 1
	item = {'id': item_id, 'name': data['name']}
	items.append(item)
	return jsonify(item), 201

# Read all
@app.route('/items', methods=['GET'])
def get_items():
	return jsonify(items)

# Read one
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
	item = next((i for i in items if i['id'] == item_id), None)
	if item:
		return jsonify(item)
	return jsonify({'error': 'Item not found'}), 404

# Update
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
	data = request.get_json()
	item = next((i for i in items if i['id'] == item_id), None)
	if not item:
		return jsonify({'error': 'Item not found'}), 404
	if not data or 'name' not in data:
		return jsonify({'error': 'Name is required'}), 400
	item['name'] = data['name']
	return jsonify(item)

# Delete
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
	global items
	item = next((i for i in items if i['id'] == item_id), None)
	if not item:
		return jsonify({'error': 'Item not found'}), 404
	items = [i for i in items if i['id'] != item_id]
	return jsonify({'message': 'Item deleted'})

@app.route('/')
def home():
	return jsonify({'message': 'Flask CRUD API is running.'})

if __name__ == '__main__':
	app.run(debug=True)

