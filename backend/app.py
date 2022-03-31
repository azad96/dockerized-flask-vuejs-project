from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from config import user, password
from models import db, Person, Plate, PersonPlate
import json
import re

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
            "owner_name": person_obj.name,
            "plate_number": plate_obj.plate_number,
            "start_date": plate_obj.start_date,
            "end_date": plate_obj.end_date
        } for _, person_obj, plate_obj in parking_permits]

        return jsonify(list_of_permits)

    if request.method == 'POST':
        req = json.loads(list(dict(request.form).keys())[0])
        plate_pattern = re.compile(r"[a-zA-Z]{1,3}-[a-zA-Z]{1,2}[1-9][0-9]{0,3}")
        print(req['plate_number'])
        print(req['owner_name'])
        print(req['start_date'])
        print(req['end_date'])
        if 'plate_number' not in req:
            print('plate number is not in request')
            return {'response': 400}
        elif not plate_pattern.match(req['plate_number']):
            print('plate number is not valid')
            return {'response': 422}
        else:
            print('plate number is valid')
            new_person = Person(req['owner_name'])
            new_plate = Plate(req['plate_number'], req['start_date'], req['end_date'])
            db.session.add(new_person)
            db.session.add(new_plate)
            db.session.commit()
            new_person_plate_mapping = PersonPlate(new_person.id, new_plate.id)
            db.session.add(new_person_plate_mapping)
            db.session.commit()
            return {'response': 200}





# Start the app
if __name__ == '__main__':
    app.run(debug=True)
