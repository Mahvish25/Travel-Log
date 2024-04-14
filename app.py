from flask import Flask, request, jsonify
from flask import Flask, request, jsonify

# initialize flask app
app = Flask(__name__)

# set up for sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# configure our database so that we can connect to it.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tripdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


# Define model for SQLAlchemy
class Travel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(80), unique=True, nullable=False)
    country = db.Column(db.String(255))
    total_cost = db.Column(db.String(255), nullable=False)
    weather = db.Column(db.String(80))


    def __repr__(self):
        return f"{self.id} - {self.city_name} - {self.total_cost} - {self.weather} - {self.country}"

# Create database tables based on defined models
db.create_all()


# end point to add a new book
@app.route('/api/travel', methods=['POST'])
def add_travel():
    data = request.get_json()
    if 'city_name' not in data or 'total_cost' not in data:
        return jsonify({'error': 'city_name and total_cost are required fields'}), 400

    new_travel = Travel(city_name=data['city_name'], country=data['country'], total_cost=data['total_cost'], weather=data['weather'])
    db.session.add(new_travel)
    db.session.commit()
    return jsonify({'message': 'Travel added successfully'}), 201

# Endpoint to get all books
@app.route('/api/travel', methods=['GET'])
def get_travel():
    travels = Travel.query.all()
    travel_list = [{'city_name': travel.city_name, 'country': travel.country, 'total_cost': travel.total_cost, 'weather': travel.weather} for travel in travels]
    return jsonify(travel_list)

@app.route('/api/travel/<int:travel_id>', methods=['DELETE'])
def del_travel(travel_id):
    travel = Travel.query.get(travel_id)
    if travel is None:
        return jsonify({"error": "Travel was not done"}), 404

    db.session.delete(travel)
    db.session.commit()

    return jsonify({"message": "Travel Record Deleted"}), 200

# running the flask app
if __name__ == '__main__':
    app.run(debug=True)
