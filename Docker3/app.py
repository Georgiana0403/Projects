from flask import Flask, render_template_string
import importlib
import os

app = Flask(__name__)

# Load environment-specific settings
config_file = os.getenv('CONFIG_FILE', 'config.dev')
config = importlib.import_module(config_file)

@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Environment Variables</title>
    </head>
    <body>
        <h1>Environment Variables</h1>
        <ul>
            <li><strong>Environment Name:</strong> {{ env_name }}</li>
            <li><strong>User:</strong> {{ user }}</li>
            <li><strong>Database Connection:</strong> {{ db_connection }}</li>
        </ul>
    </body>
    </html>
    """
    return render_template_string(html, 
                                  env_name=config.env_name, 
                                  user=config.user, 
                                  db_connection=config.db_connection)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
