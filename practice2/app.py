from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Python Practice 2!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Bind to 0.0.0.0 to allow external access when running in a Docker container
    app.run(host='0.0.0.0', port=port)
