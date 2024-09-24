from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['employee_db']
collection = db['employees']

def format_employee(employee):
      employee['_id'] = str(employee['_id'])
      return employee

# GET method
# /api/employee --> all employee details
# /api/employee?empid=123 --> it will return details for the employee who has empid=123

@app.route('/api/employee', methods = ['GET'])
def get_employees():
      empid = request.args.get('empid')
      if empid:
            employee = collection.find_one({ 'empid' : int(empid) })
            if employee:
                  return jsonify(format_employee(employee)), 200
            return jsonify({'error' : 'No employee found'}), 404
      else:
            employees = list(collection.find())
            return jsonify([format_employee(emp) for emp in employees]), 200
      

# POST
# /api/employee --> [ { empid : 1, name : John, designation : SDE }, { empid : 1, name : John, designation : SDE } ] --> insert the record in the database

@app.route('/api/employee', methods = ['POST'])
def add_employees():
      data = request.json
      if isinstance(data, list):
            collection.insert_many(data)
      else:
            collection.insert_one(data)
      return jsonify({'message' : 'Employee details inserted'}), 201

# PUT
# MongoDB --> { empid=101, name=john, designation=SDE } <-- existing data
# /api/employee?empid=101
# { designation = QA Analyst } 
# hit GET --> { empid=101, name=john, designation=QA Analyst }

@app.route('/api/employee', methods = ['PUT'])
def update_employee():
      empid = request.args.get('empid')
      data = request.json
      
      if empid:
            result = collection.update_one({ 'empid' : int(empid) }, { '$set'  : data })
            if result.matched_count:
                  return jsonify({ 'message' : 'Employee details updated' }), 200
            return jsonify( { 'error' : 'Employee not found' } ), 404
      return jsonify({'error' : 'Provide an empid to update the details'}), 400


# DELETE
# MongoDB --> { empid=101, name=john, designation=SDE } <-- existing data
# /api/employee?empid=101 --> it is going to delete john's details

@app.route('/api/employee', methods = ['DELETE'])
def delete_employee():
      empid = request.args.get('empid')
      if empid:
            result = collection.delete_one({'empid' : int(empid)})
            if result.deleted_count:
                  return jsonify({'message' : 'Employee Deleted'}), 200
            return jsonify({'error' : 'Employee not found'}), 404
      return jsonify({'error' : 'Provide an empid to update the details'}), 400


if __name__ == '__main__':
      app.run(debug=True)