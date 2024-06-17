import os
from flask import Flask
if os.path.exists("env.py"):
    import env


# creates an instance of Flask
app = Flask(__name__)

# Route for testing everything is connected. Forward slash refers to default route
@app.route("/")
def hello():
    return "Hello world!"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)