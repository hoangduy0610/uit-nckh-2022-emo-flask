from flask import Flask
from flask_cors import CORS

# Initializing flask application
app = Flask(__name__)
cors = CORS(app)

@app.route("/health-check")
def main():
    return """
        Application is working
    """

import routes.auth
import routes.image

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8933, debug=True)