from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Jesus'

if __name__ == '__main__':
    app.run(debug=True)
