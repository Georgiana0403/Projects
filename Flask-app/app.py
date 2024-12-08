from flask import Flask, render_template, request, redirect, url_for
import boto3
from boto3.dynamodb.conditions import Key

app = Flask(__name__)

# DynamoDB setup
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table_name = 'ItemsTable'
table = dynamodb.Table(table_name)

@app.route('/')
def home():
    # Fetch all items from DynamoDB
    response = table.scan()
    items = response.get('Items', [])
    return render_template('display_items.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        # Add item to DynamoDB
        item = {
            'id': request.form['id'],
            'name': request.form['name'],
            'category': request.form['category'],
            'description': request.form['description']
        }
        table.put_item(Item=item)
        return redirect(url_for('home'))
    return render_template('add_item.html')

@app.route('/update/<string:id>', methods=['GET', 'POST'])
def update_item(id):
    if request.method == 'POST':
        # Update item in DynamoDB
        table.update_item(
            Key={'id': id},
            UpdateExpression="set #n = :n, category = :c, description = :d",
            ExpressionAttributeValues={
                ':n': request.form['name'],
                ':c': request.form['category'],
                ':d': request.form['description']
            },
            ExpressionAttributeNames={
                '#n': 'name'
            }
        )
        return redirect(url_for('home'))
    
    # Get the item details for pre-filling the form
    response = table.get_item(Key={'id': id})
    item = response.get('Item', {})
    return render_template('update_item.html', item=item)

@app.route('/delete/<string:id>', methods=['GET'])
def delete_item(id):
    # Delete item from DynamoDB
    table.delete_item(Key={'id': id})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
