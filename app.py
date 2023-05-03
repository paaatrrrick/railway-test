from flask import Flask

app = Flask(__name__)

print('This is a test!!!!!!!')

@app.route('/')
def hello():
    print('we have been hit')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)