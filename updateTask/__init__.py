import logging

import azure.functions as func
import pymongo
import os
from bson.json_util import dumps
from bson import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    _id = req.params.get('id')
    data = req.get_json()
    try:
        client = pymongo.MongoClient(os.environ.get('MongoDB_conn'))
        database = client['func_DB']
        collection = database['tasks']
        try:
            if "title" in data:
                collection.update_one({"_id": ObjectId(_id)}, {"$set" :{"title": data.get("title")}})
            if "body" in data:
                collection.update_one({"_id": ObjectId(_id)}, {"$set" :{"body": data.get("body")}})
            if "completed" in data and type(data.get("completed")==bool):
                collection.update_one({"_id": ObjectId(_id)}, {"$set" :{"completed": data.get("completed")}})
            
            return func.HttpResponse(req.get_body(), mimetype="application/json", status_code=200)
        except:
            return func.HttpResponse('Unable to update!', status_code=400)
    
    except:
        return func.HttpResponse("Something went wrong!", status_code=500)
