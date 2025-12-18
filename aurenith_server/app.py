from flask import Flask
from models.config import Config
from models.extensions import db, migrate

app = Flask(__name__)
# app.config.from_object(Config)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql+psycopg://postgres:mysecretpassword@localhost:5432/postgres2"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize extensions
db.init_app(app)
migrate.init_app(app, db)

# import models AFTER extensions are ready
from models.members import Members  # noqa

@app.route("/")
def home():
    return "<p>Hello aurenith__server</p>"

@app.route("/health")
def healthCheck():
    return "<p>healthCheck</p>"

@app.route("/user")
def user():
    return "<p>Hello aurenith__server user</p>"

@app.route("/super")
def superuser():
    return "<p>Hello aurenith__server super2</p>"

if __name__ == "__main__":
    app.run(debug=True)
