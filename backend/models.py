from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = 'person'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Person: {self.name}>"


class Plate(db.Model):
    __tablename__ = 'plate'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    plate_number = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, plate_number, start_date, end_date):
        self.plate_number = plate_number
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"<Plate: {self.plate_number}, Start date: {self.start_date}, End date: {self.end_date}>"


class PersonPlate(db.Model):
    __tablename__ = 'person_plate_mapping'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    person_id = db.Column(UUID(as_uuid=True), db.ForeignKey('person.id'), default=uuid.uuid4)
    plate_id = db.Column(UUID(as_uuid=True), db.ForeignKey('plate.id'), default=uuid.uuid4)

    def __init__(self, person_id, plate_id):
        self.person_id = person_id
        self.plate_id = plate_id

    def __repr__(self):
        return f"<Person: {self.person_id}, Plate: {self.plate_id}>"
