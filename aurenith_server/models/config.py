import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    _db = os.environ.get("DATABASE_URL")
    if _db:
        # SQLAlchemy + psycopg adapter expectation
        if _db.startswith("postgres://"):
            _db = _db.replace("postgres://", "postgresql+psycopg://", 1)
        SQLALCHEMY_DATABASE_URI = _db
    else:
        basedir = os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "aurenith.db")