import os
from flask import Flask

app = Flask(__name__)

DATABASE_URL: str = os.environ.get("DATABASE_URL")

@app.route("/")
def home() -> str:
    return "<p>Hello aurenith__server</p>"

@app.route("/health")
def healthCheck() -> str:
    return "<p>healthCheck </p>"

@app.route("/user")
def user() -> str:
    return "<p>Hello aurenith__server user</p>"

@app.route("/super")
def superuser() -> str:
    return "<p>Hello aurenith__server super2 </p>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
