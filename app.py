from flask import Flask
import os


app = Flask(__name__)

print('This is a test!!!!!!!')

@app.route('/')
def hello():
    print('we have been hit')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))