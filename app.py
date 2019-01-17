from flask import Flask, jsonify, request
from pymongo import MongoClient


from data import insert_data, update_data, show_data


app = Flask(__name__)



@app.route("/shortlinks")
def lists():

	try:
		the_data_list = show_data()
	except:
		return jsonify({}),500
	if the_data_list == "not found":
		jsonify({"status":"failed","messege":"not found"}),404
		           
	return jsonify({"shortlinks": the_data_list}), 200


@app.route("/shortlinks", methods=["POST"])
def insert():
    data = request.get_json()
    try:
    	x = insert_data(data)
    except:
    	return jsonify({}),500
    if x == "inserted directly":
    	return jsonify({"status":"successful","messege":"inserted successfully"}),201
    
    return jsonify({"status":"successful","messege":"inserted successfully","slug":x}),201


@app.route("/shortlinks/<string:slug>", methods=["PUT"])
def update(slug):
    new_data = request.get_json()
    try:
    	x = update_data(new_data, slug)
    except:
    	return jsonify({}), 500
    if x == "not found":
    	return jsonify({"status":"failed","messege":"not found"}),404
    
    return jsonify({"status":"successful","messege": "updated successfully"}),201
