from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Migrate
import os
from datetime import datetime


app = Flask(__name__)

# Capture the start time of the app
start_time = datetime.now()

# Конфигурация через переменные окружения
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'postgresql://postgres:postgres@postgres/postgres')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Migrate with the app and db

class Item(db.Model):
    name = db.Column(db.String(80), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}

@app.route('/')
def index():
    return f"Flask app started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)

