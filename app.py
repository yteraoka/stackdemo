from flask import Flask
from redis import Redis

VERSION = '0.0.1'

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\nversion: {}'.format(count, VERSION)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
