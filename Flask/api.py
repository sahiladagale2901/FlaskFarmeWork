'''
Put and DELETE - Http verbs
Wprking with API's - JSON
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

### Initial Data in my to do list
items = [
    {'id': 1, 'name': 'Item 1', 'description': 'This is the item 1'},
    {'id': 2, 'name': 'Item 2', 'description': 'This is the item 2'}
]


@app.route('/')
def home():
    return str.capitalize("Welcome to the sample to Do list App.")


### GET: Retrieve all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


### GET: Retrieve specific items by Id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not Found"})
    return jsonify(item)


### POST: Create a new Item
@app.route('/items', methods=['POST'])
def create_items():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "unable to create an Item"})
    new_tem = {
        'id': items[-1]['id'] + 1 if items else 1,
        'name': request.json['name'],
        'description': request.json['description']
    }
    items.append(new_tem)
    return jsonify(new_tem)


### PUT: Update existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_items(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "unable to create an Item"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])

    return jsonify(item)


### DELETE:
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_items(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result': 'Item deleted'})


if __name__ == "__main__":
    app.run(debug=True)
