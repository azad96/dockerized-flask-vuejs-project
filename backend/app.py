from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from config import user, password
from models import db, Person, Plate, PersonPlate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@localhost:5432/park_tickets"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, resources={r'/*': {'origins': '*'}})

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/plate', methods=['GET', 'POST'])
def plate():
    if request.method == 'GET':
        parking_permits = db.session.query(PersonPlate, Person, Plate).join(Person).join(Plate).all()

        list_of_permits = [{
            "owner": person_obj.name,
            "plate_number": plate_obj.plate_number,
            "start_date": plate_obj.start_date,
            "end_date": plate_obj.end_date
        } for _, person_obj, plate_obj in parking_permits]

        return jsonify(list_of_permits)

    if request.method == 'POST':
        return "PLATE GET REQUEST"


# Start the app
if __name__ == '__main__':
    app.run(debug=True)
