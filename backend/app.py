from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import user, password

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@localhost:5432/park_tickets"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Person, Plate, PersonPlate

# Start the app
if __name__ == '__main__':
    app.run(debug=True)