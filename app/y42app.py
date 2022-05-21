from flask import Flask
import time
import os

app = Flask(__name__)

@app.route('/')

def funwithy42():

    payload = {
        "hello": "world",
        "built_at": os.environ.get('build_date'),
        "deployed_at": os.environ.get('deployed_at')
    }

    return payload

if __name__ == '__main__':
    os.environ["deployed_at"] = (str(time.time()).split('.')[0])
    app.run(host='0.0.0.0', port='80', debug=False)
