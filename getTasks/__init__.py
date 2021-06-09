func_DBimport logging

import azure.functions as func
import pymongo
import os
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        client = pymongo.MongoClient(os.environ.get('MongoDB_conn'))
        database = client['func_DB']
        collection = database['tasks']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", status_code=200)
    
    except:
        return func.HttpResponse("Something went wrong!", status_code=500)
