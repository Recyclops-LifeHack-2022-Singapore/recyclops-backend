from app import app, engine
from flask import jsonify

from db.models import Item, Category, Note, Resource
from sqlalchemy.orm import Session

@app.route('/items/', methods=['GET'])
@app.route('/items/<ml_id>', methods=['GET'])
def items(ml_id=None):
    with Session(bind=engine) as session:

        query = session.query(Item)
        if ml_id:
            query = query.filter_by(ml_id=ml_id)

        return jsonify(query.all())

@app.route('/categories/', methods=['GET'])
@app.route('/categories/<obj_id>', methods=['GET'])
def categories(obj_id=None):
    with Session(bind=engine) as session:

        query = session.query(Category)
        if obj_id:
            query = query.filter_by(id=obj_id)

        return jsonify(query.all())

@app.route('/notes/', methods=['GET'])
@app.route('/notes/<obj_id>', methods=['GET'])
def notes(obj_id=None):
    with Session(bind=engine) as session:

        query = session.query(Note)
        if obj_id:
            query = query.filter_by(id=obj_id)

        return jsonify(query.all())

@app.route('/resources/', methods=['GET'])
@app.route('/resources/<obj_id>', methods=['GET'])
def resources(obj_id=None):
    with Session(bind=engine) as session:

        query = session.query(Resource)
        if obj_id:
            query = query.filter_by(id=obj_id)

        return jsonify(query.all())