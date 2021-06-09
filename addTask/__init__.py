import logging

import azure.functions as func
import pymongo
import os
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.get_json()
    try:
        client = pymongo.MongoClient(os.environ.get('MongoDB_conn'))
        database = client['func_DB']
        collection = database['tasks']
        new = {
                "title": data['title'],
                "body": data['body'],
                "completed": False
            }
        if "title" and "body" in data:
            collection.insert_one(new)
            return func.HttpResponse(dumps(new), mimetype="json/application", status_code=201)
        return func.HttpResponse('Unable to add new Task!', status_code=400)

        
    except:
        return func.HttpResponse("Something went wrong!", status_code=500)
