from flask import Flask,request,jsonify
from azure.cosmos import CosmosClient
import uuid


app = Flask(__name__)

ENDPOINT = "https://localhost:8081"
KEY = "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=="
DATABASE_NAME = "demodb"
CONTAINER_NAME = "Orders"

client = CosmosClient(url=ENDPOINT, credential=KEY)
container = client.get_database_client(DATABASE_NAME).get_container_client(CONTAINER_NAME)

@app.route(rule='/create_order', methods = ['POST'])

def create_order():
    data = request.get_json()
    id = str(uuid.uuid4())
    data['id'] = id

    try:
        container.create_item(body=data)
        response_data = {'message': 'Order created'}
        return jsonify(response_data)
    except Exception as e:
        response_data = {'message': 'Failed to create order', 'error': str(e)}
        return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
