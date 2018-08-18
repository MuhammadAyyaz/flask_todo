from flask import Flask,\
request,session, redirect, jsonify

from flask_pymongo import PyMongo
app=Flask(__name__)

app.config['MONGO_DBNAME'] = 'miti'
app.config['MONGO_URI'] = 'mongodb://mayaz:ayaz31@ds263571.mlab.com:63571/axiomdt'

mongo = PyMongo(app)


@app.route('/todo/v1_v01/tasks/api/<string:id>', methods=['GET'])
def findone(id):
    frame=mongo.db.todo
    dt=frame.find_one({'ID':id})
    if dt:
        out = {'ID':dt['ID'],'Task':dt["Task"],'Description':dt['Description'],
               'Completion':dt['Completion']}
    else:
        out="No data found"
    return jsonify({'result':out})

@app.route('/todo/v1_v01/tasks/api', methods=['GET'])
def findall():
    frame=mongo.db.todo
    out=[]
    for dt in frame.find():
        out.append( {'ID':dt['ID'],'Task':dt["Task"],'Description':dt['Description'],'Completion':dt['Completion']})

    return jsonify({'result':out})

@app.route('/todo/v1_v01/tasks/add', methods=['POST','GET'])
def adding():
    frame=mongo.db.todo
    ID=request.json['ID']
    title=request.json["Task"]
    Description=request.json['Description']
    completion=request.json['Completion']
    frame.insert({"ID":ID,"Task":title,"Description":Description,"Completion":completion})

    out=[]
    for dt in frame.find():
        out.append( {'ID':dt["ID"],'Task':dt["Task"],'Description':dt['Description'],'Completion':dt['Completion']})

    return jsonify({'result':out})

@app.route('/todo/v1_v01/tasks/delete/<string:id>', methods=['DELETE','GET'])
def deletion(id):
    frame=mongo.db.todo
    dt=frame.find_one({'ID':id})
    frame.remove(dt)

    out=[]
    for data in frame.find():
        out.append( {'ID':data['ID'],
                     'Task':data["Task"],
                     'Description':data['Description'],
                     'Completion':data['Completion']})
    return jsonify({'after deletion':out})


@app.route('/todo/v1_v01/tasks/update/<string:id>',methods=['PUT'])
def updation(id):
    frame=mongo.db.todo
    dt=frame.find_one({'ID':id})
    dt['ID']=request.json['ID']
    dt["Task"]=request.json["Task"]
    dt["Description"]=request.json['Description']
    dt['Completion']=request.json['Completion']
    frame.save(dt)
    out=[]
    for data in frame.find():
        out.append( {'ID':data['ID'],'Task':data["Task"],'Description':data['Description'],'Completion':data['Completion']})
    return jsonify({'after editing':out})


if __name__ == '__main__':
    app.run(debug=True,port=8080)

