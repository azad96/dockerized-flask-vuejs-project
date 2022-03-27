from flask import Flask
from flask_migrate import Migrate
from config import user, password
from models import db, Person, Plate, PersonPlate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@localhost:5432/park_tickets"

db.init_app(app)
migrate = Migrate(app, db)


# Start the app
if __name__ == '__main__':
    app.run(debug=True)
